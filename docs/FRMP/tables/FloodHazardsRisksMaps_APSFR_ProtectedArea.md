# FloodHazardsRisksMaps_APSFR_ProtectedArea

## Description

Flood Hazard and Risk Maps - Probabilities for an euFloodsRiskZoneCode- Protected Areas
Description: APSFR\_ProtectedArea
Information on the potentially affected protected areas identified in Annex IV(1)(i), (iii) and (v) to Directive 2000/60/EC. 
Uniqueness: euFloodsUnitOfManagementCode, euFloodsRiskZoneCode, protectedAreaType, euProtectedAreaCode and probabilityScenario

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0803
  - The combination euFloodsUnitOfManagementCode, euFloodsRiskZoneCode, protectedAreaType, euProtectedAreaCode and probabilityScenario must be unique.
* - XC0841
  - The table FloodHazardsRisksMaps\_APSFR\_ProtectedArea contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0842
  - The value does not match the pattern to be used
* - V0844
  - The length must be less than or equal to 42
* - V0919
  - The value must not be missing or empty
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
* - R0815
  - euFloodsUnitOfManagementCode + euFloodsRiskZoneCode must exist on table FloodHazardsRisksMaps\_APSFR\_ProbabilityScenario
* - V0846
  - The value does not match the pattern to be used
* - V0918
  - The value must not be missing or empty
```

### probabilityScenario

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'ProbabilityType' codelist values.
* - Field type
  - ProbabilityType
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
* - V0848
  - The value does not exist in codelist ProbabilityType
* - V0920
  - The value must not be missing or empty
* - XC0814
  - euFloodsUnitOfManagementCode + euFloodsRiskZoneCode + probabilityScenario must exist on table FHRM\_APSFR\_ProbabilityScenario
```

### protectedAreaType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'ProtectedAreaType' codelist values. Potentially affected protected areas identified in Annex IV(1)(i), (iii) and (v) to Directive 2000/60/EC.
* - Field type
  - ProtectedAreaType
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
* - V0836
  - The value does not exist in codelist ProtectedAreaType
* - V0923
  - The value must not be missing or empty
```

### euProtectedAreaCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Required. The ProtectedAreaID (uniqueID) as this has been reported under relevant directives.
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
* - RF0800
  - euProtectedAreaCode must exist as a thematicIdIdentifier in the Reference dataset, ProtectedArea table
* - V0922
  - The value must not be missing or empty
* - V0993
  - The length must be less than or equal to 254
```
