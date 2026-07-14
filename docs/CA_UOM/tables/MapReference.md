# MapReference

## Description

References to map viewers, services or pdf documents containing maps.

Uniqueness: mapReferenceCode

## Table Quality Checks

*(no table QCs)*

### mapReferenceCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 50 characters. Required. Unique code for the map reference.
* - Field type
  - FeatureUniqueEUCodeType
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
* - TU0807
  - The field mapReferenceCode must be unique within table
* - V0953
  - The value must not be missing or empty
* - V0994
  - The length must be less than or equal to 50
* - V1808
  - The value does not match the pattern to be used
```

### title

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Required. Title of the map or map service.
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
* - V0959
  - The value must not be missing or empty
* - V0995
  - The length must be less than or equal to 254
```

### description

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 4000 characters. Optional. Give a short description of the map content, e.g., flood scenarios, exposed elements...
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
* - V0996
  - The length must be less than or equal to 4000
```

### creatorElectronicMailAddress

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Contact information for the email.
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
* - V0921
  - The length must be less than or equal to 250
* - V0954
  - The value does not follow the expected syntax for a valid email
* - V0955
  - The value must not be missing or empty
```

### creatorOrganisationName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Required. Organisation name of the point of contact.
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
* - V0956
  - The value must not be missing or empty
* - V0997
  - The length must be less than or equal to 254
```

### created

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Date when the map was published. Can be in the format 'yyyy' , 'yyyy-mm' or 'yyyy-mm-dd'.
* - Field type
  - WiseDateTime
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
* - V1804
  - The created value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).
```

### language

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'LanguageCode' codelist values. Language of the map.
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
* - V0952
  - The value must not be missing or empty
* - V0960
  - The values does not exist in codelist LanguageCode
```

### hyperlink

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2100 characters. ULR to connect the service with the Flood Hazard Risk Map.
* - Field type
  - URL
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
* - V0950
  - The value must not be missing or empty
* - V0951
  - The value does not follow the expected syntax for a valid URL
* - V0999
  - The length must be less than or equal to 2100
```

### resourceType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose the type of resource from the 'ResourceType' codelist values.
* - Field type
  - ResourceType
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
* - V0957
  - The value must not be missing or empty
* - V0958
  - The value doesn't exist in codelist ResourceType
```

### category

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. The map category that the URL is displaying. Choose between the overall categories or specify other value from the 'MapCategory' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - MapCategory
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - V0946
  - The value must not be missing or empty
* - V0947
  - The value doesn't exist in codelist MapCategory
* - V0992
  - Duplicate values for category exist. The list of values needs to be distinct in each record.
```
