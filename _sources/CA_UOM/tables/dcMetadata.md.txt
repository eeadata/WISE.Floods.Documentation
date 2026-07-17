# dcMetadata

## Description

Metadata

One record per country

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - T9002
  - Mandatory table has no records
* - T9003
  - The table dcMetadata must have one and only one record
```

### created

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Date of creation of the dataset.
* - Field type
  - WiseDatetime
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
* - V9016
  - The created value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss)
```

### creatorElectronicMailAddress

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Email address of the point of contact in the organisation responsible for the dataset.
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
* - V9017
  - The value must not be missing or empty
* - V9018
  - The length must be less than or equal to 250
* - V9034
  - The value must follow the expected syntax for a valid email.
```

### creatorOrganisationName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Required. Name of the organisation doing the reporting.
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
* - V9019
  - The value must not be missing or empty
* - V9020
  - The length must be less than or equal to 4000
```

### description

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Optional. Description of the dataset.
* - Field type
  - String
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
* - V9021
  - The length must be less than or equal to 4000
```

### language

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose the code of the dataset's language from the 'LanguageCode' codelist values.
* - Field type
  - LanguageCode
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
* - V9024
  - The value must not be missing or empty
* - V9025
  - The value does not exist in codelist LanguageCode
```

### license

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. A legal document giving official permission to do something with the resource. Provide the URL to the licence text of a CC BY compatible licence. Use a persistent identifier to an English or multilingual version of the licence agreement.
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
* - V9026
  - The value must not be missing or empty
* - V9027
  - The length must be less than or equal to 250
* - V9035
  - The value must follow the expected syntax for a valid URL.
```

### rights

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Optional. Information about rights held in and over the resource. If necessary, provide the attribution text required by the licence, or other relevant information.
* - Field type
  - String
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
* - V9031
  - The length must be less than or equal to 4000
```

### rightsHolder

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Optional. A person or organization owning or managing rights over the resource. This element can be provided if the rights holder reserved rights (e.g. should to be contacted for specific uses), or if the rights holder is not the organisation responsible for the dataset.
* - Field type
  - String
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
* - V9032
  - The length must be less than or equal to 4000
```

### title

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Optional. Name given to the dataset.
* - Field type
  - String
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
* - V9033
  - The length must be less than or equal to 4000
```

### reportingStructuredData

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values, depending on if structure data is being reported.
* - Field type
  - YesNo
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
* - V9028
  - The value must not be missing or empty
* - V9029
  - The value does not exist in codelist YesNo
```

### reportingDocument

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - Document
* - minOccurs
  - 0
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - XC9004
  - The value is not a valid member of the Document table
```
