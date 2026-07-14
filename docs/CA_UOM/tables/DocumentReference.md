# DocumentReference

## Description

Document references

Uniqueness: documentCode + referenceCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU9001
  - The field referenceCode must be unique within table
* - XC9008
  - The table must contain one record at least for each record of table Document with the same documentCode.
```

### referenceCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 50 characters. Required. Unique identifier of the reference to a document. The value must contain only latin characters, digits, underscores, hyphens and dots. No consecutive underscores, hyphens and dots are allowed.
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
* - V9004
  - The value must not be missing or empty
* - V9005
  - The length must be less than or equal to 50
* - V9006
  - The value must contain only latin characters, digits, underscores, hyphens and dots. No consecutive underscores, hyphens and dots are allowed
```

### documentCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Link to the document the reference belongs to.
* - Field type
  - Document
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
* - V9003
  - The value must not be missing or empty
* - XC9001
  - The value does not exist on table Document
```

### bookmark

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Bookmark within the document.
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
* - V9001
  - The value must not be missing or empty
* - V9002
  - The length must be less than or equal to 250
```

### subject

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Subject of the reference.
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
* - V9007
  - The value must not be missing or empty
* - V9008
  - The length must be less than or equal to 250
```
