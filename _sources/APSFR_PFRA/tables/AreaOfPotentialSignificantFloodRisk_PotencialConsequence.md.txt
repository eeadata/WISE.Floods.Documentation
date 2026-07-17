# AreaOfPotentialSignificantFloodRisk_PotencialConsequence

## Description

Area of Potential Significant Flood Risk - Potencial Consequence
This dataset provides information on the impact consequences of flooding
Uniqueness: euFloodsUnitOfManagementCode, euFloodsRiskZoneCode, typeImpactConsequence, impactConsequence and otherImpactConsequence

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0202
  - The combination euFloodsUnitOfManagementCode, euFloodsRiskZoneCode, typeImpactConsequence, impactConsequence and otherImpactConsequence must be unique
* - XC0292
  - There must be at least one record for every euFloodsRiskZoneCode in table AreaOfPotentialSignificantFloodRisk\_Data
* - XC0303
  - The table AreaOfPotentialSignificantFloodRisk\_PotencialConsequence contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
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

* - Code
  - Description
* - V0210
  - The value must not be missing or empty
* - V0243
  - The length must be less than or equal to 42
* - V0244
  - The value does not match the pattern to be used
* - XC0207
  - euFloodsUnitOfManagementCode must exist on table AreaOfPotentialSignificantFloodRisk\_Data
```

### euFloodsRiskZoneCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 42 characters. Required. Unique EU code for the area of potential significant flood risk. Add the two-letter ISO Country code to the Member State unique id - up to 42 characters in total.
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
* - V0211
  - The value must not be missing or empty
* - V0245
  - The length must be less than or equal to 42
* - V0246
  - The value does not match the pattern to be used
* - XC0208
  - euFloodsRiskZoneCode must exist on table AreaOfPotentialSignificantFloodRisk\_Data
```

### typeImpactConsequence

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose a type of impacting consequence from the 'TypeImpactConsequence' codelist values.
* - Field type
  - TypeImpactConsequence
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
* - R0212
  - The selected type is not correct according to the selected Impact Consequence.
* - V0212
  - The value must not be missing or empty
* - V0247
  - The value does not exist in codelist TypeImpactConsequence
```

### impactConsequence

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'ImpactConsequence' codelist values. Define a relevant consequence impacting based on the chosen 'typeImpactConsequence' value.
* - Field type
  - ImpactConsequence
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
* - V0213
  - The value must not be missing or empty
* - V0248
  - The value does not exist in codelist ImpactConsequence
```

### otherImpactConsequence

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters Conditional. Other consequence of the impacts not available in the 'ImpactConsequence' codelist. Must be reported if and only if 'impactConsequence' is 'other'.
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
* - R0208
  - otherImpactConsequence must be reported if and only if impactConsequence is 'other'
* - V0290
  - The length must be less than or equal to 1000
```
