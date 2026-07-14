# PreliminaryFloodRiskAssessment_FloodEvent

## Description

PreliminaryFloodRiskAssessment- Flood Event

Uniqueness: floodEventCode (it is a unique code at national level)

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0422
  - Checks if floodEventCode is unique within table
* - XC0432
  - The table PreliminaryFloodRiskAssessment\_FloodEvent does not contain a record for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'yes'.
* - XC0435
  - The table PreliminaryFloodRiskAssessment\_FloodEvent contains records for the following {%NUMBEROFRECORDS%} euFloodsUnitOfManagementCode values: {%RECORDS%} in table dcMetadata with "reportingStructuredData" equal to 'no'.
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
* - V0414
  - The length must be less than or equal to 42
* - V0415
  - The value does not match the pattern to be used
* - V0470
  - The value must not be missing or empty
* - XC0417
  - The value is not a valid member of thePreliminaryFloodRiskAssessment table.
```

### floodEventCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 85 characters. Required. Unique code for the flood event.The expected syntax for this field is:euFloodsUnitOfManagementCode + '.' + floodEventCode By using this convention, the same floodEventCode can be reported across different euFloodsUnitOfManagement areas.
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
* - R0422
  - If floodEventCode is a combination of UOM/RBD + floodEventCode, the UOM/RBD must match the value in euFloodsUnitOfManagementCode
* - V0416
  - The length must be less than or equal to 85
* - V0417
  - The value does not match the pattern to be used
* - V0469
  - The value must not be missing or empty
```

### floodEventName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 200 characters. Optional. Name of the flood event.
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
* - V0418
  - The length must be less than or equal to 200
```

### eventTypePastFuture

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'EventTypePastFuture' codelist values. Is the event a past event or a future event?
* - Field type
  - EventTypePastFuture
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
* - V0419
  - The value does not exist in codelist EventTypePastFuture
* - V0471
  - The value must not be missing or empty
```

### dateOfCommencement

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. If the answer to 'CategoryFlood' is 'past flood', then give the date of commencement of the flood. Can be in the format 'yyyy' , 'yyyy-mm' or 'yyyy-mm-dd'
* - Field type
  - WiseDateTime
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
* - R0421
  - dateOfCommencement must be reported if and only if eventTypePastFuture is set to 'past'
* - V0546
  - The value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss)
* - V1809
  - dateOfCommencement contains a date earlier than 1900.
* - V1810
  - dateOfCommencement date cannot be in the future.
```

### durationOfFlood

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. If the answer to 'CategoryFlood' is 'past flood', then give the number of days (duration) of the flood. The exemption types -9999 = 'Unknown', -8888 = 'Yet to be measured' and -7777 = 'Not Applicable' can be used.
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
* - R0412
  - durationOfFlood must only be reported if eventTypePastFuture is equal to 'past'
* - V0420
  - If reported, the value must be an integer greater than zero or one of the exception values: -9999, -8888 or -7777
* - V0467
  - The value is not a valid whole number
```

### returnPeriod

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 50 characters. Optional. The average number of years between floods of a certain size. Can also be reported as a range. The exemption types -9999 = 'Unknown', -8888 = 'Yet to be measured' and -7777 = 'Not Applicable' can be used.
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
* - V0422
  - The length must be less than or equal to 50
* - V0423
  - If reported, must be a positive integer, or a range of integers expressed by a separating double hyphen (e..g 1--100) or one of the exception values: -9999, -8888 or -7777
* - V0545
  - When a range is reported, the first value needs to be smaller than the second one
```

### crossBorderRelationship

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Please indicate 'Yes' if the flood location cross the national border or the unit of management.
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
* - V0421
  - The value does not exist in codelist YesNo
* - V0468
  - The value must not be missing or empty
```

### floodEventReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Optional. Provide Optionalocument(s) or link(s) to any other relevant information relating to the details of the specific flood event. This could include links to specific reports or articles and/or specific details of the particular event.
* - Field type
  - DocumentReference
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
* - XC0414
  - The document reference does not exist
```
