"""
generate_md_FRMP.py
----------------
Iterates through all the tables in the EA model (.qea) and generates one
.md file per table (MyST Markdown), including:

 - Table name and description
 - Table Quality Checks (t_objectconstraint)
 - For each field:
    - Guidance on completion
    - Field type
    - Properties (minOccurs/maxOccurs)
    - Field Quality Checks (t_attributeconstraints)

All queries are resolved here, with access to the .qea, and written as
static MyST list-table blocks. No live database connection is needed at
build time, so the generated .md files can be built by sphinx-build on
any machine — including a GitHub Actions runner with no access to the .qea.

Usage:

python generate_md_FRMP.py
"""

import os
import sqlite3

# --------------------------------------------------------------------------
# CONFIGURATION — adjust this path
# --------------------------------------------------------------------------
QEA_PATH_DESCRIPTIVE = r"data/Floods2018_RN3_UML_Descriptive.qea"

OUTPUT_DIR = "docs/FRMP/tables"


def slug(name: str) -> str:
    """Converts a table name into a safe filename."""
    return "".join(c if c.isalnum() else "_" for c in name)


def md_escape(value) -> str:
    """Escapes Markdown special characters so free text from the .qea
    (which may contain things like 'APSFR_' or '*note*') renders as
    literal text instead of being interpreted as Markdown emphasis/code."""
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\\", "\\\\")
    for ch in ("_", "*", "`"):
        text = text.replace(ch, "\\" + ch)
    return text


def clean(value) -> str:
    """Prepares a DB value for embedding inside a list-table cell:
    escapes Markdown markup, collapses newlines/whitespace, and provides
    a placeholder if empty."""
    if value is None:
        return "\\-"
    text = md_escape(value).strip()
    if not text:
        return "\\-"
    return " ".join(text.split())


def get_tables(cursor):
    cursor.execute(
        """
        SELECT Object_ID, Name, Note
        FROM t_object
        WHERE Object_Type = 'Class'
        ORDER BY Name
        """
    )
    return cursor.fetchall()


def get_fields(cursor, object_id):
    cursor.execute(
        """
        SELECT ID, Name, Notes, Type, LowerBound, UpperBound
        FROM t_attribute
        WHERE Object_ID = ?
        ORDER BY Pos
        """,
        (object_id,),
    )
    return cursor.fetchall()


def get_table_constraints(cursor, object_id):
    cursor.execute(
        """
        SELECT [Constraint], Notes
        FROM t_objectconstraint
        WHERE Object_ID = ?
        ORDER BY [Constraint]
        """,
        (object_id,),
    )
    return cursor.fetchall()


def get_field_constraints(cursor, field_id):
    cursor.execute(
        """
        SELECT [Constraint], Notes
        FROM t_attributeconstraints
        WHERE ID = ?
        ORDER BY [Constraint]
        """,
        (field_id,),
    )
    return cursor.fetchall()


def render_list_table(title, header, rows, widths):
    """Builds a static MyST `{list-table}` block from already-resolved rows."""
    widths_str = " ".join(str(w) for w in widths)
    lines = []
    opening = f"```{{list-table}} {title}" if title else "```{list-table}"
    lines.append(opening)
    lines.append(f":widths: {widths_str}")
    lines.append(":header-rows: 1")
    lines.append("")
    lines.append("* - " + "\n  - ".join(header))
    for row in rows:
        lines.append("* - " + "\n  - ".join(clean(v) for v in row))
    lines.append("```")
    lines.append("")
    return lines


def render_table_header(cursor, table_id, table_name, table_note):
    lines = [f"# {table_name}", ""]
    lines += ["## Description", ""]
    lines.append(md_escape(table_note).strip() if table_note else "*(no description)*")
    lines.append("")
    lines += ["## Table Quality Checks", ""]

    constraints = get_table_constraints(cursor, table_id)
    if constraints:
        lines += render_list_table(
            None, ["Code", "Description"], constraints, widths=[15, 85]
        )
    else:
        lines.append("*(no table QCs)*")
        lines.append("")
    return lines


def render_field_block(cursor, field_id, field_name, field_notes, field_type, lower, upper):
    lines = [f"### {field_name}", ""]

    props_rows = [
        ("Guidance on completion", field_notes),
        ("Field type", field_type),
        ("minOccurs", lower),
        ("maxOccurs", upper),
    ]
    lines += render_list_table(None, ["Property", "Value"], props_rows, widths=[30, 70])

    field_constraints = get_field_constraints(cursor, field_id)
    if field_constraints:
        lines += render_list_table(
            "Quality Checks", ["Code", "Description"], field_constraints, widths=[15, 85]
        )
    else:
        lines.append("**Quality Checks:** *(no field QCs)*")
        lines.append("")

    return lines


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(QEA_PATH_DESCRIPTIVE)
    cursor = conn.cursor()

    tables = get_tables(cursor)
    if not tables:
        print("No descriptive tables found with Object_Type = 'Class'.")
        print("Check whether your model uses a different criterion "
              "(e.g. Stereotype = 'class').")
        conn.close()
        return

    toc_entries = []

    for table_id, table_name, table_note in tables:
        fields = get_fields(cursor, table_id)

        content = render_table_header(cursor, table_id, table_name, table_note)
        for field_id, field_name, field_notes, field_type, lower, upper in fields:
            content += render_field_block(
                cursor, field_id, field_name, field_notes, field_type, lower, upper
            )

        filename = slug(table_name) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

        toc_entries.append(f"tables/{slug(table_name)}")
        print(f"Generated: {filepath}  ({len(fields)} fields)")

    conn.close()

    print("\nEntries are picked up automatically by the {toctree} :glob: in docs/FRMP/index.md\n")
    for entry in toc_entries:
        print(f"   {entry}")


if __name__ == "__main__":
    main()
