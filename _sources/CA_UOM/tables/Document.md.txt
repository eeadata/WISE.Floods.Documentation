# Document

## Description

Documents to be referenced to.

Uniqueness: documentCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - T9001
  - Mandatory table has no records
* - TU9002
  - The field documentCode must be unique within table
```

### documentCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 50 characters. Required. Unique identifier of the document. The value must contain only latin characters, digits, underscores, hyphens and dots. No consecutive underscores, hyphens and dots are allowed.
* - Field type
  - String
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V9009
  - The value must not be missing or empty
* - V9010
  - The length must be less than or equal to 50
* - V9011
  - The value must contain only latin characters, digits, underscores, hyphens and dots. No consecutive underscores, hyphens and dots are allowed
```

### documentName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Name of the document.
* - Field type
  - String
* - minOccurs
  - 1
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V9012
  - The value must not be missing or empty
* - V9013
  - The length must be less than or equal to 250
```

### hyperlink

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2100 characters. Conditional. URL of the document if available on the internet. Either URL or document file as an attachment. The size of the file can be up to 100 MB and the valid file extensions are: 'xlsx' (Excel), 'docx' (Word) and 'pdf'. Either URL or documentFile must be reported, but not both.
* - Field type
  - URL
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R9002
  - Either hyperlink or documentFile must be reported, but not both
* - V9014
  - The value does not follow the expected syntax for a valid URL
* - V9015
  - The Hyperlink value must be less than 2100 characters
```

### documentFile

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. Document file as an attachment. The size of the file can be up to 100 MB and the valid file extensions are: 'xlsx' (Excel), 'docx' (Word) and 'pdf'. Either URL or documentFile must be reported, but not both.
* - Field type
  - Attachment
* - minOccurs
  - 0
* - maxOccurs
  - 1
```

**Quality Checks:** *(no field QCs)*
