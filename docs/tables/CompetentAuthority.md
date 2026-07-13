# CompetentAuthority

## Descripción

Competent Authority.
Uniqueness: euCACode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - T0002
  - Table CompetentAuthority must have one record at least if WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'No'
* - T0004
  - Table CompetentAuthority must not have any record if WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'Yes'
* - TU0003
  - euCACode must be unique.
* - XC0021
  - The table CompetentAuthority contains records when the record in table dcMetadata has "reportingStructuredData" equal to 'no'.
* - XC0022
  - If WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'no', euCACode must exist on table UOM\_CompetentAuthority.
```

### euCACode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique EU code for the Competent Authority. Add the Two-letter ISO Country code followed by the Member State unique ID.
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

* - Código
  - Descripción
* - V0023
  - The length must be less than or equal to 42
* - V0024
  - The value must not be missing or empty
* - V0025
  - The value does not match the pattern to be used. Two-letter ISO Country code followed by the Member State unique ID.
```

### competentAuthorityName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 250 characters. Required. Official name of the Competent Authority in English.
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

* - Código
  - Descripción
* - V0011
  - The length must be less than or equal to 250
* - V0039
  - The value must not be missing or empty
* - V0045
  - Valid characters are any of the latin alphabet, digits and "'(),-./:;\_ only
```

### competentAuthorityNameNL

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 250 characters. Required. Official name of the Competent Authority in the Member State’s national language.
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

* - Código
  - Descripción
* - V0012
  - The length must be less than or equal to 250
* - V0072
  - The value must not be missing or empty
```

### competentAuthorityNameNLLanguage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'LanguageCode' codelist values. Language used for reporting the name of the Competent Authority in a national language.
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

* - Código
  - Descripción
* - V0013
  - The value does not exist in codelist LanguageCode
* - V0073
  - The value must not be missing or empty
```

### acronym

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 100 characters. Optional. Acronym for the Competent Authority (if it exists).
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

* - Código
  - Descripción
* - V0002
  - The length must be less than or equal to 100
```

### legalStatusReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Provide a reference or references to document(s) that explain the legal status of each competent authority. This should include: <ul> <li>the legislation establishing the competent authority,</li> <li>the legislation laying down the duties of the competent authority in relation to the Floods Directive and</li> <li>the legislation laying down other duties of the competent authority relevant (but not directly related) to the Floods Directive.</li> </ul> More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 1
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - V0044
  - The value must not be missing or empty
* - V0047
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0002
  - The document reference does not exist
```

### reference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to any additional supporting or background documents that are considered relevant to the Competent Authortity ( As a reminder, if providing a document describe the: <ul> <li>Subject (describe in a few words the subject matter of the reference provided)</li> <li>Document name (Provide the name of the reference document, the name should identify the document unequivocally)</li> <li>Bookmark (For each document provide the chapters, sections and page ranges where the relevant information can be found)</li> <li>If the file containing the reference is uploaded to WISE, provide the file name of the uploaded document. If the document has not been uploaded to WISE, provide a hyperlink to the relevant background document. (The Member State must guarantee that the hyperlink will remain stable and active for a period of 6 years after reporting).</li> </ul> More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 0
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - V0048
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0013
  - The document reference does not exist
```

### street

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 100 characters. Required. Street name where Competent Authority is located in latin characters.
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

* - Código
  - Descripción
* - V0027
  - The length must be less than or equal to 100
* - V0040
  - The value must not be missing or empty
```

### city

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 100 characters. Required. City where Competent Authority is located in latin characters.
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

* - Código
  - Descripción
* - V0006
  - The length must be less than or equal to 100
* - V0041
  - The value must not be missing or empty
* - V0046
  - Valid characters are any of the latin alphabet, digits and "'(),-./:;\_ only
```

### country

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 100 characters. Required. Country where the Competent Authority is located in English.
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

* - Código
  - Descripción
* - V0014
  - The length must be less than or equal to 100
* - V0042
  - The value must not be missing or empty
```

### postCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 100 characters. Optional. Postcode address of the Competent Authority.
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

* - Código
  - Descripción
* - V0026
  - The length must be less than or equal to 100
```

### url

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 2100 characters. Required. Website address of the Competent Authority.
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

* - Código
  - Descripción
* - V0038
  - The value does not follow the expected syntax for a valid URL
* - V0043
  - The value must not be missing or empty
* - V0068
  - The url value must be less than 2100 characters
```

### changeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide a reference or references to document(s) if the Competent Authorities, or their roles, have changed since the previous cycle of reporting under the Floods Directive. This should include information on the reasons for the change(s) and how the change(s) will support the improved implementation of the FD. Only actual Competent Authorities need to be reported, explanation should also be provided if a Competent Authority is a successor of another one. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - DocumentReference
* - minOccurs
  - 0
* - maxOccurs
  - \*
```

```{list-table} Quality Checks
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - V0049
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0001
  - The document reference does not exist
```
