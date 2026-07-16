# FloodHazardsRisksMaps_APSFR

## Description

Flood Hazard and Risk Maps - Relationship with euFloodsRiskZoneCode
Description: APSFR (Areas identified as being at potentially significant flood risk)
Information on the areas identified as being at potentially significant flood risk (APSFR) under Article 5, based on the maps prepared under Article 6, including details on the source, mechanism and characteristics of flooding at the Unit of Management level.
Uniqueness: euFloodsUnitOfManagementCode and euFloodsRiskZoneCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0800
  - The combination euFloodsUnitOfManagementCode and euFloodsRiskZoneCode must be unique.
* - XC0821
  - There must be at least one record for every euFloodsUnitOfManagement reported in table FloodsHazardsRisksMaps
* - XC0834
  - The table FloodHazardsRisksMaps\_APSFR does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0839
  - The table FloodHazardsRisksMaps\_APSFR contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0816
  - The length must be less than or equal to 42
* - V0817
  - The value does not match the pattern to be used
* - V0917
  - The value must not be missing or empty
* - XC0810
  - euFloodsUnitOfManagementCode must exist on table FHRM
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
* - V0819
  - The value does not match the pattern to be used
* - V0913
  - The value must not be missing or empty
* - XC0811
  - euFloodsRiskZoneCode must exists in reference table with that euFloodsUnitOfManagementCode as relatedZoneIdentifier
```

### mapUpdateReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to information that give an update on any changes to the maps or to the process used to develop the maps since the last reporting cycle. This element is focused on updates or changes to the maps or approaches specifically. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0977
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0812
  - The document reference does not exist
```

### sourceOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'SourceOfFlooding' codelist values. Define relevant source of flooding. Indicate source of floods from enumeration list. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - SourceOfFlooding
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
* - V0820
  - The value does not exist in codelist SourceOfFlooding
* - V0915
  - The value must not be missing or empty
* - V0978
  - Duplicate values for sourceOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherSourceDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. Provide a description if type is set to 'Other' under Source in the enumeration list.
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
* - R0801
  - otherSourceDescription must be reported if and only if sourceOfFlooding is 'other'
* - V0821
  - The length must be less than or equal to 1000
```

### mechanismOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'MechanismOfFlooding' codelist values. Indicate the mechanism of flooding that has been included in the FHRMs from the enumeration list. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0822
  - The value does not exist in codelist MechanismOfFlooding
* - V0979
  - Duplicate values for mechanismOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherMechanismDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. Provide a description if type is set to 'Other' under Mechanism in the enumeration list.
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
* - R0802
  - otherMechanismDescription must be reported if and only if mechanismOfFlooding is 'other'
* - V0823
  - The length must be less than or equal to 1000
```

### characteristicsOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'CharacteristicsOfFlooding' codelist values. Define relevant characteristics of flooding included in the FHRMs. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0824
  - The value does not exist in codelist CharacteristicsOfFlooding
* - V0980
  - Duplicate values for characteristicsOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherCharacteristicsDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters Conditional. Provide a description if type is set to 'Other' under Characteristics in the enumeration list.
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
* - R0803
  - otherCharacteristicsDescription must be reported if and only if characteristicsOfFlooding is 'other'
* - V0825
  - The length must be less than or equal to 1000
```

### sourcesMapped

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'FloodSourcesMapped' codelist values. Provide clarification of the sources presented on the map at the APSFR level. The flood sources which are included in the map should be clearly indicated on it. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - FloodSourcesMapped
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
* - V0826
  - The value does not exist in codelist FloodSourcesMapped
* - V0916
  - The value must not be missing or empty
* - V0981
  - Duplicate values for sourcesMapped exist. The list of values needs to be distinct in each record.
```

### sourcesMappedReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. Where multiple sources have been selected in SourcesMapped explain which sources have been combined in the maps and how these sources were modelled i.e. modelling individually and overlain or modelled in combination. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0804
  - sourcesMappedReference element must be reported if more than one option is selected for sourcesMapped
* - V0982
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0813
  - The document reference does not exist
```

### article_6_6_Applied

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Has Article 6(6) been applied or not?
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
* - V0812
  - The value does not exist in codelist YesNo
* - V0911
  - The value must not be missing or empty
```

### article_6_6_Justification

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. Choose from the 'Article6\_6Justification' codelist values. For medium probability floods indicate the justification for applying Article 6.6 from the enumeration list. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - Article6\_6Justification
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
* - R0805
  - article\_6\_6\_Justification must be reported if article\_6\_6\_Applied = 'yes'
* - V0827
  - The value does not exist in codelist article\_6\_6\_Justification
* - V0983
  - Duplicate values for article\_6\_6\_Justification exist. The list of values needs to be distinct in each record.
```

### article_6_6_JustificationOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other justification' is selected in 'Article6.6Justification', provide a description.
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
* - R0806
  - article\_6\_6\_JustificationOther must be reported if and only if article\_6\_6\_Justification = 'other'
* - V0814
  - The length must be less than or equal to 1000
```

### article_6_7_Applied

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Has Article 6(7) been applied?
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
* - V0813
  - The value does not exist in codelist YesNo
* - V0912
  - The value must not be missing or empty
```

### article_6_7_Justification

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Required. Choose from the 'Article6\_7Justification' codelist values. For medium probability floods indicate the justification for applying Article 6.7 from the enumeration list. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - Article6\_7Justification
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
* - R0807
  - article\_6\_7\_Justification must be reported if article\_6\_7\_Applied = 'yes'
* - V0828
  - The value does not exist in codelist article\_6\_7\_Justification
* - V0984
  - Duplicate values for article\_6\_7\_Justification exist. The list of values needs to be distinct in each record.
```

### article_6_7_JustificationOther

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. If 'Other' is selected in 'article6\_7\_Justification', provide a description.
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
* - R0808
  - article\_6\_7\_JustificationOther must be reported if and only if article\_6\_7\_Justification = 'other'
* - V0815
  - The length must be less than or equal to 1000
```

### mapReferenceCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Code of the map reference pointing to map services, web apps, etc., reported under 'MapReference' table.
* - Field type
  - MapReferenceCode
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
* - V0914
  - The value must not be missing or empty
* - V1800
  - Duplicate values for mapReferenceCode exist. The list of values needs to be distinct in each record.
* - XC0828
  - The value must be a member of the MapReference table
```
