# WFDCompetentAuthoritiesAndUOMs

## Descripción

WFDCompetentAuthoritiesAndUOMs 

One record per country.

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - T0003
  - There must be a maximum of one record at WFDCompetentAuthoritiesAndUOMs.
* - T0007
  - If WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'yes', table UOM\_CompetentAuthority cannot be empty.
* - T0008
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'yes', table UOM\_CompetentAuthority cannot be empty.
* - XC0014
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'Yes',The table UnitOfManagement of the Spatial datasemust be empty .
* - XC0016
  - The table WFDCompetentAuthoritiesAndUOMs does not contain any record when the record in table dcMetadata has "reportingStructuredData" equal to 'yes'.
* - XC0018
  - The table WFDCompetentAuthoritiesAndUOMs contains records when the record in table dcMetadata has "reportingStructuredData" equal to 'no'.
```

### url

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 2100 characters. Optional. URL for integration of your own internet-based information.
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

* - Código
  - Descripción
* - V0037
  - The value does not follow the expected syntax for a valid URL
* - V0067
  - The url value must be less than 2100 characters
```

### wfdCompetentAuthorities

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Are the competent authorities the same as reported under the Water Framework Directive?
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

* - Código
  - Descripción
* - V0008
  - The value does not exist in codelist YesNo
* - V0035
  - The value must not be missing or empty.
```

### wfdRiverBasinDistricts

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Select 'Yes' if the RBDs reported under the Water Framework Directive are being used (if a Member State has reported Sub-units then it's assumed these are the scale of management).
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

* - Código
  - Descripción
* - V0009
  - The value does not exist in codelist YesNo.
* - V0036
  - The value must not be missing or empty.
```
