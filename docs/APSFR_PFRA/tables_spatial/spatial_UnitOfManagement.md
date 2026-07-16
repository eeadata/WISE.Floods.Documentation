# UnitOfManagement

## Description

Units of Management

Uniqueness: thematicIdIdentifier + thematicIdIdentifierScheme

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU002
  - The inspireIdLocalId and inspireIdNamespace combination must be unique for each object. [TU002]
* - TU003
  - The thematicIdIdentifier and thematicIdIdentifierScheme combination must be unique for each object.[TU003]
* - XC002
  - The table must be empty if UoM Descriptive/WFDCompetentAuthoritiesAndUOMs/wfdRiverBasinDistricts = 'Yes'. [XC002]
* - XC003
  - If WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'No', all thematicIdentifier of the table UnitOfManagement of the Spatial dataset must be included in the table UnitOfManagement as euFloodsUnitOfManagementCode. [XC003]
```

### geometry

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - The geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon geometry. Only one type of geometry can be used for a given object. Only one type of geometry can be reported in a given data set.
* - Field type
  - geometry
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
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon). [S013]
* - S016
  - The geometry of the units of management must not overlap each other.[S016]
* - S018
  - The Unit of management must be within the National territory, with a 200 meters tolerance distance. [S018]
* - V067
  - The value must not be missing or empty [V067]
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
  - The inspireIdLocalId value must be less than 255 characters. [V002]
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
  - The inspireIdNamespace value must be less than 255 characters. [V003]
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
* - R022
  - The inspireIdVersionId value must be reported, if the wiseEvolutionType value is 'change'.[R022]
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
* - R023
  - The thematic identifier must be a valid identifier in the register, if the wiseEvolutionType value is 'deletion', 'noChange' or 'change'.[R023]
* - RF001
  - A valid 'eu' thematic identifier exists in the register but was not reported in the Geopackage file (either as a spatial object or as a predecessor).[RF001] The missing thematicididentifiers are: {%RECORDS%} [RF001]
* - RF002
  - The thematic identifiers that replace this object must exist in the register, or be the thematic identifier of another object reported in the spatial data set.[RF002]
* - RF004
  - The thematic identifier must not exist in the register, unless the wiseEvolutionType value is 'deletion', 'noChange' or 'change'.[RF004]
* - RF018
  - thematicIdIdentifier cannot be identical to the thematicIdIdentifier of another RiverBasinDistrict reported under WFD.[RF018]
* - V005
  - The thematicIdIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators). [V005]
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
* - V049
  - The thematicIdIdentifierScheme must be ‘euFloodsUnitOfManagementCode'. [V049]
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
  - The beginLifespanVersion value must be reported, if the endLifespanVersion value is reported. [R013]
* - R024
  - The beginLifespanVersion value must be reported, unless the wiseEvolutionType is 'creation' or 'noChange'.[R024]
* - V006
  - The beginLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss). [V006]
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
  - The beginLifespanVersion date must not be after the endLifespanVersion. [R003]
* - V039
  - The endLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V039]
```

### predecessorsIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. In a genealogy, the object(s) that has(have) been deactivated/replaced by another one.
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
* - R011
  - The object must have zero predecessors, if the wiseEvolutionType value is 'creation'.[R011]
* - R014
  - The predecessorsIdentifier value must be reported, if the predecessorsIdentifierScheme value is reported. [R014]
* - R015
  - The predecessorsIdentifier and predecessorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself). [R015]
* - R026
  - The object must have one and only one predecessor, if the wiseEvolutionType value is 'changeCode' or 'splitting'.[R026]
* - R027
  - The object must have two or more predecessors, if the wiseEvolutionType value is 'aggregation' or 'changeBothAggregationAndSplitting'. [R027]
* - R028
  - The object must have zero predecessors, if the wiseEvolutionType value is 'change' or 'noChange'.[R028]
* - R029
  - If an identifier is the predecessor of 2 or more objects, then those objects must have wiseEvolution in ('splitting','changeBothAggregationAndSplitting')[R029]
* - R032
  - At least one predecessor of an object with wiseEvolutionType value equal to 'splitting' or 'changeBothAggregationAndSplitting' must be reported as predecessor of another spatial object. [R032]
* - R045
  - Units Of Management must have predecessors if the wiseEvolutionType is not ‘change’ or ‘noChange’ or 'creation'. [R043]
* - RF005
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF005]
* - RF006
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object. [RF006]
* - RF008
  - The object has a predecessor that does not exist in the register. [RF008]
* - V040
  - The predecessorsIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators). [V040]
```

### predecessorsIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Identifier defining the scheme used to assign the identifier value(s) in the predecessorsIdentifier element.
* - Field type
  - IdentifierScheme
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
* - R016
  - The predecessorsIdentifierScheme value must be reported, if the predecessorsIdentifier value is reported. [R016]
* - V050
  - The predecessorsIdentifierScheme must be ‘euFloodsUnitOfManagementCode'. [V050]
```

### successorsIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. In a genealogy, the newly active object(s) that replaces(replace) the current one.
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
* - R018
  - The successorsIdentifier value must be reported, if the successorsIdentifierScheme value is reported.[R018]
* - R019
  - The successorsIdentifier and successorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself). [R019]
* - R033
  - The object has wiseEvolutionType = 'deletion' and is a predecessor to other objects reported in the data set. The identifiers of the successors must be reported consistently.[R033]
* - RF003
  - The thematic identifier that is replacing this object has been superseded, deprecated or is invalid.[RF003]
* - V041
  - The successorsIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators).[V041]
```

### successorsIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Identifier defining the scheme used to assign the identifier value(s) in the successorsIdentifier element.
* - Field type
  - IdentifierScheme
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
* - R020
  - The successorsIdentifierScheme value must be reported, if the successorsIdentifier value is reported. [R020]
* - V051
  - The successorsIdentifierScheme must be ‘euFloodsUnitOfManagementCode'. [V051]
```

### wiseEvolutionType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Type of event that produced or modified the version of the object being reported (creation, change, deletion, aggregation, splitting). This attribute is required to explicitly report changes and update the current status of the object in the Water Information System for Europe.
* - Field type
  - WiseEvolutionTypeValue
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
* - R031
  - The spatial object must have wiseEvolutionType value equal to 'deletion' if it is also reported as predecessor to another spatial object.[R031]
* - V017
  - The value must not be missing or empty [V017]
* - V027
  - The value must be one of ('creation','aggregation','splitting','change','changeCode','changeBothAggregationAndSplitting','noChange', 'changeExtendedArea', 'changeReducedArea').[V027]
* - V068
  - Units Of Management cannot be reported as deletions [V068]
```

### nameTextInternational

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Name, in English. English exonym or an understandable English version of the name of the geographical feature or spatial object.
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
* - V007
  - The nameTextInternational value must be less than 255 characters. Upper case letters (A to Z) and digits (0 to 9) are allowed (spaces and hifens can be used as separators). [V007]
* - V023
  - The value must not be missing or empty [V023]
```

### nameText

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Name, in the national language. National language endonym, or national language version of the name of the geographical feature or spatial object.
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
* - V001
  - The used encoding is not correct. Strange characters in nameText field. [V001]
* - V008
  - The nameText value must be a string with less than 255 characters.[V008]
* - V022
  - The value must not be missing or empty [V022]
```

### nameLanguage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Language code of the language used in the nameText attribute value.
* - Field type
  - WiseLanguageCode
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
* - V018
  - The value must not be missing or empty [V018]
* - V028
  - The nameLanguage value is not a valid ISO 639-2/B language code. [V028]
```

### designationPeriodBegin

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Beginning of the time period defining when the management, restriction or regulation zone was legally designated or became effective in the real world.
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
* - R034
  - If wiseEvolutionType = 'deletion' and the object has successors, the designationPeriodEnd of the object must be equal to the designationPeriodBegin of the successors.
* - R046
  - Objects with the same predecessor must have the same designationPeriodBegin value. [R046]
* - RF012
  - If wiseEvolutionType in ('deletion','change','noChange'), the designationPeriodBegin must be equal to the designationPeriodBegin of the object in the register.[RF012]
* - RF013
  - If wiseEvolutionType in ('splitting','aggregation','changeBothAggregationAndSplitting','changeExtendedArea','changeReducedArea'), the designationPeriodBegin value must be higher than the designationPeriodBegin value of the predecessor.[RF013]
* - RF014
  - If wiseEvolutionType = 'changeCode', the designationPeriodBegin value must be equal to the designationPeriodBegin value of the predecessor. [RF014]
* - RF015
  - if wiseEvolutionType is in (''change'',''changeCode'',''noChange'',''reactivation'') then, the designationPeriodBegin cannot be lower than the one stored in the registry for the same element.[RF015]
* - V009
  - The designationPeriodBegin value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss). [V009]
* - V021
  - The value must not be missing or empty [V021]
```

### designationPeriodEnd

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - [End of the] time period defining when the management, restriction or regulation zone was legally designated or became effective in the real world.
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
  - The designationPeriodBegin date must not be after the designationPeriodEnd.[R004]
* - R030
  - The designationPeriodEnd date must be reported, if the wiseEvolutionType value is 'deletion'.[R030]
* - V010
  - The designationPeriodEnd value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss). [V010]
```

### zoneType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - High-level classification defining the type of Management, Restriction or Regulation Zone.
* - Field type
  - ZoneTypeCode
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
* - V020
  - The value must not be missing or empty [V020]
* - V029
  - The zoneType value is not valid. [V029]
```

### legalBasisName

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 254 characters. Name of the document.
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
* - V011
  - The legalBasisName value must be a string with less than 255 characters.[V011]
```

### legalBasisLink

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2100 characters. Link to an online version of the document.
* - Field type
  - url
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
* - V012
  - The legalBasisLink value must be a valid URL [V012]
* - V069
  - The legalBasisLink value must be less than 2100 characters.[V069]
```

### legalBasisLevel

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - The level at which the legislative instrument is adopted. Allowable values are {'european','international','national','sub-national'}.
* - Field type
  - LegislationLevelValue
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
* - V033
  - The legalBasisLevel value is not valid (see http://dd.eionet.europa.eu/vocabulary/inspire/LegislationLevelValue). [V033]
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
* - V013
  - The sizeValue value must be a positive number. [V013]
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
* - V048
  - The sizeUom value must be a valid unit of measure (see http://dd.eionet.europa.eu/vocabulary/wise/UomSize). [V048]
```

### link

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Max length: 2100 characters.
* - Field type
  - url
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
* - V014
  - The value does not follow the expected syntax for a valid URL [V014]
* - V043
  - The link value must be an URL with less than 2100 characters. [V043]
```
