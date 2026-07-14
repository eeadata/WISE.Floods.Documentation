# FloodRiskManagementPlans_Measure

## Description

Flood Risk Management Plans - Measures
This table records information on measures for flood risk management, including measure types, key aspects, prioritisation, geographical coverage, timetable, reference progress, and progress review. 
Uniqueness: measureCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0609
  - The combination of measureCode must be unique
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
* - V0600
  - The length must be less than or equal to 42
* - V0650
  - The value must not be missing or empty
* - V0715
  - The value does not match the pattern to be used
```

### measureType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'MeasureType' codelist values.
* - Field type
  - MeasureType
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
* - R0629
  - If [FloodRiskmanagemenPlans\_Measure].[measureType] is 'other', [FloodRiskmanagemenPlans\_Measure].[measureDescription] must be reported.
* - V0605
  - The value does not exist in codelist MeasureType
* - V0653
  - The value must not be missing or empty
* - V0711
  - Duplicate values for measureType exist. The list of values needs to be distinct in each record.
```

### measureName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 250 characters. Required. Short descriptive name for the measure.
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
* - V0601
  - The length must be less than or equal to 250
* - V0651
  - The value must not be missing or empty
```

### measureAspect

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'MeasureAspect' codelist values, whether this measure is aggregated or individual.
* - Field type
  - MeasureAspect
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
* - V0602
  - The value does not exist in codelist MeasureAspect
* - V0654
  - The value must not be missing or empty
```

### measureDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2000 characters Optional. Provide a description of the measure.
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
* - V0608
  - The length must be less than or equal to 2000
```

### geographicCoverage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'GeographicScale' codelist values. Indicate the geographic coverage of expected effect of the measure(s). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
* - Field type
  - GeographicScale
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
* - R0630
  - If [FloodRiskmanagemenPlans\_Measure].[geographicCoverage] is 'national' or 'other', [FloodRiskmanagemenPlans\_Measure].[measureDescription] must be reported.
* - V0604
  - The value does not exist in codelist GeographicScale
* - V0655
  - The value must not be missing or empty
* - V0703
  - Duplicate values for geographicCoverage exist. The list of values needs to be distinct in each record.
* - XC0636
  - If [FloodRiskmanagemenPlans\_Measure].[geographicCoverage] is 'riverBasinDistrict', [FloodRiskmanagemenPlans\_MeasureLocation].[euRBDCode] must be reported.
* - XC0637
  - If [FloodRiskmanagemenPlans\_Measure].[geographicCoverage] is 'floodsRiskZone', [FloodRiskmanagemenPlans\_MeasureLocation].[euFloodsRiskZone] must be reported.
* - XC0638
  - If [FloodRiskmanagemenPlans\_Measure].[geographicCoverage] is 'surfaceWaterBody', [FloodRiskmanagemenPlans\_MeasureLocation].[euSurfaceWaterBodyCode] must be reported.
* - XC0639
  - If [FloodRiskmanagemenPlans\_Measure].[geographicCoverage] is not 'national', [FloodRiskmanagemenPlans\_MeasureLocation] must be reported.
```

### cost

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2000 characters. Optional. Cost and benefits of the measure(s) (expressed in monetary terms(in €/national currency), quantitative and/or qualitative terms).
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
* - V0606
  - The length must be less than or equal to 2000
```

### costExplanationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Provide document(s) or link(s) to relevant documentation explaining what is included in the cost calculation and/or for providing further details (e.g. whether figures refer to budget allocated or to expenditure to date). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0704
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0601
  - The value is not a valid member of the DocumentReference table
```

### otherCommunityAct

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2000 characters. Optional. Other Community Act under which the measure has been implemented (where relevant) (AnnexA.I.4).
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
* - V0607
  - The length must be less than or equal to 2000
```

### otherRelevantInformationReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Reference providing additional useful information of clarification related to the measure. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0705
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0602
  - The value is not a valid member of the DocumentReference table
```

### progressReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Provide references/links to relevant documentation (clearly pointing to the precise location of the information, e.g. chapter and page range) explaining progress with implementation of measures towards achievement of objectives. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0652
  - The value must not be missing or empty
* - V0706
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0603
  - The value is not a valid member of the DocumentReference table
```

### progressReview

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'MeasureCodesProgress' codelist values. Please indicate progress made with implementation of measures.
* - Field type
  - MeasureCodesProgress
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
* - V0609
  - The value does not exist in codelist MeasureCodesProgress
* - V0656
  - The value must not be missing or empty
```

### progressDescription

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 1000 characters. Optional. This field must be reported if in 'progressReview', 'AB - Abandoned/interrupted' is selected.
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
* - R0624
  - progressDescription must not be reported if progressReview is not 'abandonedInterrupted'
* - R0625
  - progressDescription must be reported if progressReview is 'abandonedInterrupted'
* - V0610
  - The length must be less than or equal to 1000
```

### timetableReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Timetable for implementation (Annex Part A.II.1 and A.I.4). More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0707
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0604
  - The value is not a valid member of the DocumentReference table
```

### categoryOfPriority

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Choose from the 'CategoryOfPriority' codelist values.
* - Field type
  - CategoryOfPriority
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
* - V0611
  - The value does not exist in codelist CategoryofPriority
```

### isInternational

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Indication of whether the geographical coverage of the measure’s expected effect is international.
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
* - R0628
  - If [FloodRiskmanagemenPlans\_Measure].[isInternational] is 'yes', [FloodRiskmanagemenPlans\_Measure].[measureDescription] must be reported.
* - V0709
  - The value does not exist in codelist YesNo
* - V0710
  - The value must not be missing or empty
```
