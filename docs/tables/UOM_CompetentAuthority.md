# UOM_CompetentAuthority

## Descripción

Prime Competent Authority of UOM

Uniqueness:  euFloodsUnitOfManagementCode + euCACode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - RF0001
  - If WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'yes', all wfdCompetentAuthorities in reference data needs to be reported.
* - RF0002
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'yes', all wfdRiverBasinDistricts in reference data needs to be reported.
* - TU0002
  - The combination euCACode, euFloodsUnitOfManagementCode must be unique.
* - XC0009
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'yes', all wfdRiverBasinDistricts in reference data needs to be reported.
* - XC0011
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'No', all euFloodsUnitOfManagementCode reported in UnitOfManagement must be reported in UOM\_CompetentAuthority.
* - XC0017
  - The table UOM\_CompetentAuthority does not contain any record when the record in table dcMetadata has "reportingStructuredData" equal to 'yes'.
* - XC0019
  - The table UOM\_CompetentAuthority contains records when the record in table dcMetadata has "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique EU code for the Unit of Management or WFD River Basin District following the WISE identifier syntax. Add the two-letter ISO Country code to the Member State unique id - up to 42 characters in total.
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
* - V0007
  - The length must be less than or equal to 42
* - V0010
  - The value does not match the pattern to be used. Two-letter ISO Country code followed by the Member State unique ID
* - V0033
  - The value must not be missing or empty
* - XC0005
  - The value euFloodsUnitOfManagementCode must exist on table UnitOfManagement if WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'No'
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
* - V0001
  - The length must be less than or equal to 42
* - V0005
  - The value does not match the pattern to be used. Two-letter ISO Country code followed by the Member State unique ID.
* - V0032
  - The value must not be missing or empty
* - XC0004
  - If WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'No', euCACode must exist on table CompetentAuthorities
* - XC0012
  - If WFDCompetentAuthoritiesAndUOMs.wfdCompetentAuthorities is 'Yes', euCACode must exist on table UoM Reference Data Descriptive WFDCompetentAuthorities
```

### roleCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'RoleCode' codelist values. Core Roles undertaken by the Competent Authority in the implementation of the Floods Directive. A competent authority is defined as being the authority with the responsibility for either the implementation of the different stages of the Floods Directive or for reporting to the European Commission. A Competent Authority can have a minimum of one and maximum of three roles under the Floods Directive, so more than one can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - RoleCode
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
* - R0002
  - Same roleCode for the same combination of euFloodsUnitOfManagementCode and euCACode
* - V0022
  - The value does not exist in codelist RoleCode
* - V0031
  - The value must not be missing or empty
```
