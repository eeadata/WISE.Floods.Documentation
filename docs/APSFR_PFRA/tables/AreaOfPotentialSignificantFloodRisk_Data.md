# AreaOfPotentialSignificantFloodRisk_Data

## Description

Area of Potential Significant Flood Risk - Data
This dataset provides data on source, mechnaism and characteristics of flooding 
Uniqueness: euFloodsUnitOfManagementCode and euFloodsRiskZoneCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - T0201
  - For each reported euFloodsRiskZoneCode in AreaOfPotentialSignificantFloodRisk\_Data, at least one Potential Consequence must be reported.
* - TU0200
  - The combination euFloodsUnitOfManagementCode and euFloodsRiskZoneCode must be unique.
* - TU0205
  - euFloodsRiskZoneCode must be unique within table
* - XC0302
  - The table AreaOfPotentialSignificantFloodRisk\_Data contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0200
  - The length must be less than or equal to 42
* - V0201
  - The value does not match the pattern to be used
* - V0206
  - The value must not be missing or empty
* - XC0200
  - euFloodsUnitOfManagementCode must exist on table AreaOfPotentialSignificantFloodRisk\_Methodology
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
* - V0202
  - The length must be less than or equal to 42
* - V0203
  - The value does not match the pattern to be used
* - V0207
  - The value must not be missing or empty
* - XC0291
  - euFloodsRiskZoneCode must exist on table RiskZone Spatial - RiskZone
```

### crossBorderRelationship

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose an option from the 'YesNo' codelist values. Please indicate whether the APSFR crosses the national border.
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
* - V0204
  - The value does not exist in codelist YesNo
* - V0208
  - The value must not be missing or empty
```

### generalAdditionalCommentsReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Provide a reference or references to document(s) that will be helpful to explain the data and information provided. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Code
  - Description
* - XC0201
  - The document reference does not exist
```

### sourceOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'SourceOfFlooding' codelist. For each APSFR, indicate the source of floods from the enumeration list that are considered relevant. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - SourceOfFlooding
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
* - V0222
  - The value does not exist in codelist SourceOfFlooding
* - V0223
  - The value 'none' cannot be selected
* - V0280
  - Duplicate values for sourceOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherSourceFloodingDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list provide a description of the other source(s).
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
* - R0200
  - otherSourceFloodingDescription must be reported if sourceOfFlooding is 'other'
* - V0224
  - The length must be less than or equal to 1000
```

### mechanismOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'MechanismOfFlooding' codelist values. Indicate the mechanism of flooding from the enumeration list. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - MechanismOfFlooding
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
* - R0209
  - mechanismOfFlooding must be reported if sourceOfFlooding and characteristicsOfFlooding are not reported
* - V0225
  - The value does not exist in codelist MechanismOfFlooding
* - V0281
  - Duplicate values for mechanismOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherMechanismFloodingDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list provide a description of the other mechanism(s).
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
* - R0201
  - otherMechanismFloodingDescription must be reported if mechanismOfFlooding is 'other'
* - V0226
  - The length must be less than or equal to 1000
```

### characteristicsOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'CharacteristicsOfFlooding' codelist values. Define the relevant characteristics of flooding. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - CharacteristicsOfFlooding
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
* - R0210
  - characteristicsOfFlooding must be reported if sourceOfFlooding and mechanismOfFlooding are not reported
* - V0227
  - The value does not exist in codelist CharacteristicsOfFlooding
* - V0282
  - Duplicate values for characteristicsOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherCharacteristicsFloodingDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If ‘Other’ selected from enumeration list provide a description of the other characteristics or state whether there are no special characteristics.
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
* - R0202
  - otherCharacteristicsFloodingDescription must be reported if characteristicsOfFlooding is 'other'
* - V0228
  - The length must be less than or equal to 1000
```
