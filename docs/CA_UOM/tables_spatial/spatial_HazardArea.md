# HazardArea

## Description

HazardArea: Preliminary Flood Risk Assessment - Events (it includes past and future events)
Reporting of spatial elements is no longer mandatory. The QC XC004 requirement is no longer a BLOCKER, and it is now possible to report a Unit of Management containing only the mandatory descriptive tables: PreliminaryFloodRiskAssessment &amp; PreliminaryFloodRiskAssessment\_TypeOfFlood
Uniqueness: thematicIdIdentifier + thematicIdIdentifierScheme
It is not required to delete previously reported Future Events. For Future events, only the latest submission will be taken into account. Past Events from previous reporting cycles will still remain active unless a new version of the same past event (with the same thematicIdIdentifier) is reported in newer reporting cycles.

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - R047
  - Only one geometry type can be reported for each record [R047]
* - TU002
  - The inspireIdLocalId and inspireIdNamespace combination must be unique for each object. [TU002]
* - TU003
  - The thematicIdIdentifier and thematicIdIdentifierScheme combination must be unique for any HazardArea [TU003]
* - XC004
  - At least one Hazard Area must be reported for those related zones (RBDs or UOMs) for which structured data is being reported (reprotingStructuredData='Yes') in dcMetadata table [XC004]
* - XC006
  - The are {%NUMBEROFRECORDS%} records that have a relatedZoneIdentifier for which no structured data is being reported (reprotingStructuredData='No') in dcMetadata table: {%RECORDS%} [XC006]
```

### geometry_polygon

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. The polygon geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
* - Field type
  - geometry
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
* - S002
  - Unsupported SRID [S002]
* - S005
  - The coordinate reference system (CRS) is not valid.[S005]
* - S006
  - The geometry must not have anomalous geometric points, such as self-intersections.[S006]
* - S010
  - The value does not follow the expected syntax for a valid multipolygon {%reason%} [S010]
* - S011
  - Geometry is not valid. Reason: {%reason%} [S011]
* - S012
  - The transformation of the geometry has not worked because of: {%reason%} [S012]
* - S013
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon).[S013]
* - S014
  - The geometry of the HazardArea must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
* - S016
  - The geometry must be reported
```

### geometry_lineString

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. The line geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
* - Field type
  - geometry
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
* - S002
  - Unsupported SRID [S002]
* - S005
  - The coordinate reference system (CRS) is not valid.[S005]
* - S006
  - The geometry must not have anomalous geometric points, such as self-intersections.[S006]
* - S010
  - The value does not follow the expected syntax for a valid multilinestring {%reason%} [S010]
* - S011
  - Geometry is not valid. Reason: {%reason%} [S011]
* - S012
  - The transformation of the geometry has not worked because of: {%reason%} [S012]
* - S013
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon).[S013]
* - S014
  - The geometry of the HazardArea must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
* - S016
  - The geometry must be reported
```

### geometry_point

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Conditional. The point geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
* - Field type
  - geometry
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
* - S002
  - Unsupported SRID [S002]
* - S005
  - The coordinate reference system (CRS) is not valid.[S005]
* - S006
  - The geometry must not have anomalous geometric points, such as self-intersections.[S006]
* - S010
  - The value does not follow the expected syntax for a valid multipoint {%reason%} [S010]
* - S011
  - Geometry is not valid. Reason: {%reason%} [S011]
* - S012
  - The transformation of the geometry has not worked because of: {%reason%} [S012]
* - S013
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon).[S013]
* - S014
  - The geometry of the HazardArea must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
* - S016
  - The geometry must be reported
```

### inspireIdLocalID

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. A local identifier, assigned by the data provider. The local identifier is unique within the namespace. It is recommended to use the same value used in the thematicIdIdentifier. The element is required.The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, a polyline or a point geometry. Only one type of geometry can be used for a given object. Only one type of geometry can be reported in a given data set.
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
* - V002
  - The inspireIdLocalId value must be less than 255 characters.[V002]
* - V015
  - The value must not be missing or empty [V015]
```

### inspireIdNamespace

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Namespace, assigned by the data provider, uniquely identifying the data source of the spatial object.Use country code, if no INSPIRE namespace is defined at national level.
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
* - V003
  - The inspireIdNamespace value must be less than 255 characters.[V003]
* - V019
  - The value must not be missing or empty [V019]
```

### inspireIdVersionId

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 25 characters. The identifier of the particular version of the spatial object, with a maximum length of 25 characters. If the specification of a spatial object type with an external object identifier includes life-cycle information, the version identifier is used to distinguish between the different versions of a spatial object. Within the set of all versions of a spatial object, the version identifier is unique.
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
* - V004
  - The inspireIdVersionId value must be less than 26 characters. [V004]
```

### thematicIdIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 42 characters. Unique identifier used to identify the spatial object within the specified identification scheme. European identifier, must follow WISE syntax rules.
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
* - V005
  - The thematicIdIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hyphen and the underscore can be used as non-consecutive separators).[V005]
* - V024
  - The value must not be missing or empty [V024]
```

### thematicIdIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Identifier defining the scheme used to assign the identifier.
* - Field type
  - IdentifierScheme
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
* - V016
  - The value must not be missing or empty [V016]
* - V032
  - The thematicIdIdentifierScheme must be ‘euFloodsHazardAreaCode'. [V032]
```

### beginLifespanVersion

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Date and time at which this version of the spatial object was inserted or changed in the spatial data set.
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
* - R002
  - The beginLifespanVersion value must be reported, if the inspireVersionId value is reported.[R002]
* - R013
  - The beginLifespanVersion value must be reported, if the endLifespanVersion value is reported.[R013]
* - V006
  - The beginLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V006]
```

### endLifespanVersion

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Date and time at which this version of the spatial object was superseded or retired in the spatial data set.
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
* - R003
  - The beginLifespanVersion date must not be after the endLifespanVersion.[R003]
* - V039
  - The endLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V039]
```

### relatedZoneIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 42 characters. Reference to a related management, regulation or restriction zone.
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
* - RF009
  - The object has an 'eu' related zone that does not exist in the register. [RF009]
* - V042
  - The relatedZoneIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hyphen and the underscore can be used as non-consecutive separators).[V042]
* - V070
  - The value must not be missing or empty [V070]
* - XC001
  - The relatedZoneIdentifier must be present in dcMetadata table of Document dataset and 'reportingStructuredData' set to 'Yes'. [XC001]
```

### relatedZoneIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Identifier defining the scheme used to assign the identifier value in the relatedZoneIdentifier element.
* - Field type
  - IdentifierScheme
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
* - V030
  - The relatedZoneIdentifierScheme must be ‘euFloodsUnitOfManagementCode' or 'euRBDCode'. [V030]
* - V071
  - The value must not be missing or empty [V071]
```

### validityPeriodBegin

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - [Beginning of] the future finite time frame where the hazard applies. The same hazard assessment can be valid for a specific period, or even for several specific periods: the hazard assessment of forest fires may actually be valid only in summer, or maybe in summer or in winter (but not all year long). This attribute can also be used for multi-temporal hazard analysis.
* - Field type
  - WiseDateTime
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
* - V009
  - The validityPeriodBegin value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V009]
* - V031
  - The value must not be missing or empty [V031]
* - V079
  - validityPeriodBegin cannot be in the future. BLOCKER
```

### validityPeriodEnd

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - [End of] the future finite time frame where the hazard applies. The same hazard assessment can be valid for a specific period, or even for several specific periods: the hazard assessment of forest fires may actually be valid only in summer, or maybe in summer or in winter (but not all year long). This attribute can also be used for multi-temporal hazard analysis.
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
* - R004
  - The validityPeriodBegin date must not be after the validityPeriodEnd.[R004]
* - V010
  - The validityPeriodEnd value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V010]
```

### hazardCategory

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - \-
* - Field type
  - NaturalHazardCategoryValue
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
* - V073
  - The value must not be missing or empty [V073]
* - V075
  - The value is not a valid member of the referenced list. [V075]
```

### specificHazardType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - \-
* - Field type
  - SpecificHazardTypeValue
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
* - V072
  - The value must not be missing or empty [V072]
* - V078
  - The specificHazardType must be 'preliminaryFloodRiskAssessmentPastEvent' or 'preliminaryFloodRiskAssessmentFutureEvent'. [V078]
```

### likelihoodQuantitativeReturnPeriod

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - A number range representing the return period in years. E.g. 1-10.
* - Field type
  - NumberRange
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
* - V065
  - The likelihoodQuantitativeReturnPeriod value must be a positive integer, or a range of integers expressed by a separating double hyphen (e..g 1--100) . If it is a range, the first value must be lower than the second one.[V065]
* - V076
  - The value must not be missing or empty [V076]
```

### determinationMethod

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Specifies if the Preliminary Flood Risk Area result is delineated after modelling or determined after interpretation. There are several ways to delineate the perimeter of a hazard: to compute it according to a model, or to define it by interpretation of available data and/or information. This is modelled using the DeterminationMethod data type.
* - Field type
  - DeterminationMethodValue
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
* - R043
  - DeterminationMethod should be reported if specificHazardType is 'preliminaryFloodRiskAssessmentFutureEvent' [R043]
* - V077
  - Checks if the record based on criteria is valid LINK [V077]
```

### sizeValue

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - The area of the reference geometry (in square kilometre) or length of the reference geometry (in kilometre).
* - Field type
  - float
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
* - R005
  - If sizeUOM is reported then sizeValue must also be reported. If sizeValue is reported then sizeUOM must also be reported.[R005]
* - R049
  - If lines or points are reported SizeValue must be reported.
* - V013
  - The sizeValue value must be a positive number.[V013]
* - V057
  - The value is not a valid whole or decimal number [V057]
```

### sizeUom

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Unit of measure of the value provided in the 'sizeValue' attribute. Allowable units of measure is 'km2'.
* - Field type
  - UomSize
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
* - V037
  - The sizeUOM must have 'km2' value.[V037]
```
