# FloodHazardsRisksMaps_APSFR_ProbabilityScenario

## Description

Flood Hazard and Risk Maps - Probabilities for an euFloodsRiskZoneCode
Description: APSFR\_ APSFR\_ProbabilityScenario
This table records information required under Article 6.3 of the Floods Directive on the probability scenarios, including a reference describing the probability type and how it is derived, as well as information on potential consequences such as impacts on the environment, types of economic activity, cultural heritage, and the population affected.

Uniqueness: euFloodsUnitOfManagementCode,  euFloodsRiskZoneCode and probabilityScenario

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0802
  - The combination euFloodsUnitOfManagementCode, euFloodsRiskZoneCode and probabilityScenario must be unique.
* - XC0822
  - There must be at least one record for every euFloodsRiskZoneCode + euFloodsUnitOfManagementCode in table FloodHazardsRisksMaps\_APSFR
* - XC0835
  - The table FloodHazardsRisksMaps\_APSFR\_ProbabilityScenario does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0840
  - The table FloodHazardsRisksMaps\_APSFR\_ProbabilityScenario contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0840
  - The length must be less than or equal to 42
* - V0841
  - The value does not match the pattern to be used
* - V0930
  - The value must not be missing or empty
* - XC0830
  - euFloodsUnitOfManagementCode must exist in FloodHazardsRisksMaps table
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
* - V0845
  - The value does not match the pattern to be used
* - V0929
  - The value must not be missing or empty
* - XC0829
  - euFloodsRiskZoneCode must exist in FloodHazardsRisksMaps\_APSFR table
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
* - V0847
  - The value does not exist in codelist ProbabilityType
* - V0937
  - The value must not be missing or empty
```

### descriptionOfProbabilityReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide a reference as to what level of probably is considered to be medium, for example = 100 year return period. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Code
  - Description
* - V0924
  - The value must not be missing or empty
* - V0985
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0816
  - The document reference does not exist
```

### returnPeriod

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Max length: 50 characters. The average number of years between floods of a certain size. Can also be reported as a range. The exemption types -9999 = 'Unknown', -8888 = 'Yet to be measured', -7777 = 'Not Applicable' can be used.
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
* - V0849
  - The length must be less than or equal to 50
* - V0851
  - If reported, must be a positive integer, or a range of integers expressed by a separating double hyphen (e..g 1--100) or one of the exception values: -9999, -8888 or -7777
* - V0852
  - When a range is reported, the first value needs to be smaller than the second one
```

### consequencesAffectedEnvironmentType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Indicate consequence from the 'EnvironmentType' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - EnvironmentType
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
* - V0855
  - The value does not exist in codelist EnvironmentType
* - V0928
  - The value must not be missing or empty
* - V0986
  - Duplicate values for consequencesAffectedEnvironmentType exist. The list of values needs to be distinct in each record.
```

### consequencesOtherEnvironmentDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Conditional. Only to be used if the type is set to 'Other' in the enumeration list.
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
* - R0812
  - consequencesOtherEnvironmentDescription must be reported if and only if consequencesAffectedEnvironmentType is equal to 'other'
* - V0856
  - The length must be less than or equal to 250
```

### consequencesAffectedIEDInstallationNumber

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Number of IED installations potentially affected. The exception types -9999 = 'Unknown', -8888 = 'Yet to be measured' and -7777 = 'Not Applicable' can be used.
* - Field type
  - Integer
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
* - V0838
  - The value must be zero, greater than zero or one of the exception values: -9999, -8888 or -7777
* - V0925
  - The value is not a valid whole number
* - V0926
  - The value must not be missing or empty
```

### consequencesAffectedIEDInstallationType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Identify type from the 'IEDInstallationType' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - IEDInstallationType
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
* - V0857
  - The value does not exist in codelist IEDInstallationType
* - V0987
  - Duplicate values for consequencesAffectedIEDInstallationType exist. The list of values needs to be distinct in each record.
```

### consequencesEnvironmentReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Reference(s) to information relevant for the reported information on IED installations and/or protected areas. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0988
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0817
  - The document reference does not exist
```

### residentPopulationAffected

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Estimated number of resident populations potentially affected
* - Field type
  - Integer
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
* - V0859
  - The value must be zero, greater than zero or one of the exception values: -9999, -8888 or -7777
* - V0934
  - The value is not a valid whole number
* - V0935
  - The value must not be missing or empty
```

### populationAffectedDayTime

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Estimated number of people affected during daytime.
* - Field type
  - Integer
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
* - V0860
  - The value must be zero or greater than zero
* - V0931
  - The value is not a valid whole number
```

### populationAffectedNightTime

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Estimated number of people affected during night time.
* - Field type
  - Integer
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
* - V0861
  - The value must be zero or greater than zero
* - V0932
  - The value is not a valid whole number
```

### populationAffectedTotal

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Estimated number of people affected in the area.
* - Field type
  - Integer
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
* - V0862
  - The value must be zero or greater than zero
* - V0936
  - The value is not a valid whole number
```

### populationIndirectlyAffected

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Estimated number of people indirectly affected. This includes local business owners, investors, and others connected to the area's residents and visitors.
* - Field type
  - Integer
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
* - V0863
  - The value must be zero or greater than zero
* - V0933
  - The value is not a valid whole number
```

### consequenceEconomicActivityType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Indicate consequence from 'EconomicActivityType' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - EconomicActivityType
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
* - V0865
  - The value does not exist in codelist EconomicActivityType
* - V0990
  - Duplicate values for consequenceEconomicActivityType exist. The list of values needs to be distinct in each record.
```

### consequenceOtherEconomicActivityDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Conditional. If 'Other Source' is selected from enumeration list, provide a description (this may relate to one other source or several other sources).
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
* - R0813
  - consequenceOtherEconomicActivityDescription must be reported if and only if consequenceEconomicActivityType is equal to 'other'
* - V0866
  - The length must be less than or equal to 250
```

### consequenceCulturalHeritageType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Indicate consequence from 'CulturalHeritageType' codelist values. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - CulturalHeritageType
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
* - V0867
  - The value does not exist in codelist CulturalHeritageType
* - V0991
  - Duplicate values for consequenceCulturalHeritageType exist. The list of values needs to be distinct in each record.
```

### consequenceOtherCulturalHeritageDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Conditional. Only to be used if the type is set to 'Other' in the enumeration list.
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
* - R0814
  - consequenceOtherCulturalHeritageDescription must be reported if and only if consequenceCulturalHeritageType is equal to 'other'
* - V0868
  - The length must be less than or equal to 250
```

### otherTypeOfPotentialConsequencesDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters Optional. Type in a potential consequence if not part of provided under enumeration lists for 'InhabitantsAffected', 'EconomicActivity', 'Environment' or 'OtherInformation'.
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
* - V0864
  - The length must be less than or equal to 250
```

### otherTypeOfPotentialConsequencesExplanationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Please provide a reference to any newly defined potential consequence. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0989
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0815
  - The document reference does not exist
```
