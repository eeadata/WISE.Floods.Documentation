# PreliminaryFloodRiskAssessment_TypeOfFlood

## Descripción

Preliminary Flood Risk Assessment - Type of flood

Uniqueness: euFloodsUnitOfManagementCode + sourceOfFlooding (enforced by QC)

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - TU0420
  - The combination euFloodsUnitOfManagementCode and sourceOfFlooding must be unique.
* - XC0433
  - The table PreliminaryFloodRiskAssessment\_TypeOfFlood does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0436
  - The table PreliminaryFloodRiskAssessment\_TypeOfFlood contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0439
  - The length must be less than or equal to 42
* - V0440
  - The value does not match the pattern to be used
* - V0478
  - The value must not be missing or empty
* - XC0421
  - The value is not a valid member of the PreliminaryFloodRiskAssessment table.
```

### sourceOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'SourceofFlooding' codelist values. Provide information on the specific sources of flooding to which Article 4 has been applied. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - SourceofFlooding
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
* - V0441
  - The value does not exist in codelist SourceOfFlooding
* - V0477
  - The value must not be missing or empty
* - V0530
  - Duplicate values for sourceOfFlooding exist. The list of values needs to be distinct in each record.
* - V0553
  - The option 'none' is not compatible with any other option.
```

### otherSourceDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other: Flooding of land by water due to other sources, can include other tsunamis' is selected from enumeration list, provide a description of the other source(s).
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
* - R0418
  - otherSourceDescription must be reported if sourceOfFlooding is 'other'
* - V0442
  - The length must be less than or equal to 1000
```
