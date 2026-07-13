# PreliminaryFloodRiskAssessment_FloodEventLocation

## Descripción

Preliminary Flood Risk Assessment - Flood Event Location

Uniqueness: floodEventCode + euFloodsHazardAreaCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - TU0423
  - The combination floodEventCode, euFloodsHazardAreaCode must be unique within table
* - XC0424
  - There must be at least one record for every floodEventCode in table PreliminaryFloodRiskAssessment\_FloodEvent
```

### floodEventCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 85 characters. Required. Unique code for the flood event. The expected syntax for this field is:euFloodsUnitOfManagementCode + '.' + floodEventCode By using this convention, the same floodEventCode can be reported across different euFloodsUnitOfManagement areas.
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
* - V0424
  - The length must be less than or equal to 85
* - V0425
  - The value does not match the pattern to be used
* - V0474
  - The value must not be missing or empty
* - XC0419
  - The value is not a valid member of the PreliminaryFloodRiskAssessment\_FloodEvent table
* - XC0437
  - If the floodEventCode is a combination of UOM/RBD + floodEventCode, the UOM/RBD must match with the value in euFloodsUnitOfManagementCode from the PreliminaryFloodRiskAssessment\_FloodEvent with the same floodEventCode
```

### euFloodsHazardAreaCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Required. Unique code for the flood location - up to 42 characters in total. Can also be used as an identifier for multiple surface water bodies designated under the WFD which the flood location is represented by. A polygon must be reported as a representation of the flood location to establish link between spatial feature and information in xml schema.
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
* - V0435
  - The length must be less than or equal to 42
* - V0436
  - The value does not match the pattern to be used
* - V0472
  - The value must not be missing or empty
* - XC0426
  - The value is not a valid member of the spatial Hazard Area table.
```

### euFloodsRiskZoneCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 42 characters. Optional. Unique EU code for the area of potential significant flood risk. Add the two-letter ISO Country code to the Member State unique id - up to 42 characters in total.
* - Field type
  - FeatureUniqueEUCodeType
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
* - XC0418
  - The value is not a valid member of the spatial Risk Zone table.
```

### euSurfaceWaterBodyCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Unique code for the Water Body used under the WFD. If the EUSurfaceWaterBodyCode is reported as a representation of the flood location no spatial data needs to be reported as this information is already reported under the WFD. If several Water Bodies are affected by one flood location they should be reported here (hence this element is unbounded). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - FeatureUniqueEUCodeType
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
* - V0523
  - Duplicate values for euSurfaceWaterBodyCode exist. The list of values needs to be distinct in each record.
* - V0556
  - The length must be less than or equal to 42
```

### floodEventLocationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to any other relevant information relating to location if the flood event. This may include details of multiple flood locations covering large flood event scenarios. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0524
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0420
  - The document reference does not exist
```

### sourceOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'SourceOfFlooding' codelist values. Provide information on the specific flood types to which Article 4 applies. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0426
  - The value does not exist in codelist SourceOfFlooding
* - V0427
  - The value 'none' cannot be selected
* - V0473
  - The value must not be missing or empty
* - V0525
  - Duplicate values for sourceOfFlooding exist. The list of values needs to be distinct in each record.
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
* - R0415
  - otherSourceDescription must be reported if sourceOfFlooding is 'other'
* - V0428
  - The length must be less than or equal to 1000
```

### mechanismOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. Choose from the 'MechanismOfFlooding' codelist values. For each flood event indicate the mechanism of flooding. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - R0413
  - mechanismOfFlooding must be reported if sourceOfFlooding and characteristicsOfFlooding are not reported
* - V0429
  - The value does not exist in codelist MechanismOfFlooding
* - V0526
  - Duplicate values for mechanismOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherMechanismDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' is selected from enumeration list, provide a description of the other mechanism(s).
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
* - R0416
  - otherMechanismDescription must be reported if mechanismOfFlooding is 'other'
* - V0430
  - The length must be less than or equal to 1000
```

### characteristicsOfFlooding

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R0414
  - characteristicsOfFlooding must be reported if sourceOfFlooding and mechanismOfFlooding are not reported
* - V0431
  - The value does not exist in codelist CharacteristicsOfFlooding
* - V0527
  - Duplicate values for characteristicsOfFlooding exist. The list of values needs to be distinct in each record.
```

### otherCharacteristicsDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Max length: 1000 characters. Conditional. If 'Other' selected from enumeration list, provide a description of the other characteristics or state whether there are no special characteristics.
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
* - R0417
  - otherCharacteristicsDescription must be reported if characteristicsOfFlooding is 'other'
* - V0432
  - The length must be less than or equal to 1000
```

### typeOfFloodReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to any other relevant information relating to location if the flood event. This may include details of multiple flood locations covering large flood event scenarios. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0528
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0415
  - The document reference does not exist
```
