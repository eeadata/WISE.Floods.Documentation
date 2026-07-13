import sqlite3

conn = sqlite3.connect(r"[# Adjust this path]")
cursor = conn.cursor()

for tabla in ["t_object", "t_attribute", "t_objectconstraint", "t_attributeconstraints", "t_attributetag"]:
    print(f"\n--- {tabla} ---")
    try:
        cursor.execute(f"PRAGMA table_info({tabla})")
        for col in cursor.fetchall():
            print(col[1], col[2])  # nombre de columna, tipo
    except Exception as e:
        print("ERROR:", e)

conn.close()