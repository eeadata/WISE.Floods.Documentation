# FloodRiskManagementPlans_MeasureResponsibleAuthority

## Description

Flood Risk Management Plans - Measures - Responsible Authorities
Information on the Authority responsible for implementing the measures for flood risk management.
Uniqueness: measureCode + levelOfResponsability + nameResponsabilityAuthority

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R0600
  - Either levelOfResponsibility or nameResponsibleAuthority must be reported, but not both
* - T0601
  - The table must contain one record at least for each record of table FRMP\_Measure with the same measureCode
* - TU0607
  - The combination of measureCode, levelOfResponsibility and nameResponsibleAuthority must be unique
```

### measureCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 42 characters. Required. Unique code for the measures.
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
* - V0657
  - The value must not be missing or empty
* - XC0607
  - The value of measureCode must exist in table FloodRiskManagementPlans\_Measure
```

### levelOfResponsibility

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Optional. Authority responsible - level of responsibility (e.g., 'national authority', 'RBD/UoM authority', 'regional authorities', 'municipality/ies', other...) or name of authority.
* - Field type
  - LevelOfResponsibility
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
* - V0717
  - The value does not exist in codelist LevelOfResponsibility
```

### nameResponsibleAuthority

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Optional. Provide the international name of responsible authority.
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
* - V0620
  - The length must be less than or equal to 250
```
