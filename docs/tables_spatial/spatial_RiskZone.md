# RiskZone

## Descripción

RiskZone: Area of Potential Significant Flood Risk
Reporting of spatial elements is no longer mandatory. The QC XC005 requirement is no longer a BLOCKER, and it is now possible to report a Unit of Management containing only the mandatory descriptive table: AreaOfPotentialSignificantFloodRisk\_Methodology.
levelOrIntensity is presumed always 'significant'
Uniqueness: thematicIdIdentifier + thematicIdIdentifierScheme

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - R048
  - Only one geometry type can be reported for each record [R047]
* - S015
  - The geometry must be reported unless the wiseEvolutionType is 'deletion' [S015]
* - TU002
  - The inspireIdLocalId and inspireIdNamespace combination must be unique for each object. [TU002]
* - TU003
  - The thematicIdIdentifier and thematicIdIdentifierScheme combination must be unique for any RiskZone [TU003]
* - XC005
  - At least one Risk Zone must be reported for those related zones (RBDs or UOMs) for which structured data is being reported (reprotingStructuredData='Yes') in dcMetadata table [XC005]
* - XC007
  - The are {%NUMBEROFRECORDS%} records that have a relatedZoneIdentifier for which no structured data is being reported (reprotingStructuredData='No') in dcMetadata table: {%RECORDS%} [XC007]
```

### geometry_polygon

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. The polygon geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
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

* - Código
  - Descripción
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
  - The geometry of the RiskZone must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
```

### geometry_lineString

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. The line geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
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

* - Código
  - Descripción
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
  - The geometry of the RiskZone must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
```

### geometry_point

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. The point geometry representing the spatial extent of the spatial object. The element is required. The geometry of a Management Area, Restriction or Regulation Zone can be reported using a polygon, line or point geometry. Only one type of geometry can be used for a given object. At least one type of geometry must be reported.
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

* - Código
  - Descripción
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
  - The geometry of the RiskZone must be intersected by the geometry of the associated Unit of Management or River Basin District (with a 200 metre tolerance buffer).[S014]
```

### inspireIdLocalId

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V002
  - The inspireIdLocalId value must be less than 255 characters.[V002]
* - V015
  - The value must not be missing or empty [V015]
```

### inspireIdNamespace

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V003
  - The inspireIdNamespace value must be less than 255 characters.[V003]
* - V019
  - The value must not be missing or empty [V019]
```

### inspireIdVersionId

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R022
  - The inspireIdVersionId value must be reported, if the wiseEvolutionType value is 'change'.[R022]
* - V004
  - The inspireIdVersionId value must be less than 26 characters. [V004]
```

### thematicIdIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R023
  - The thematic identifier must be a valid identifier in the register, if the wiseEvolutionType value is 'deletion', 'noChange' or 'change'.[R023]
* - RF001
  - A valid 'eu' thematic identifier exists in the register but was not reported in the geopackage file (either as a spatial object or as a predecessor).[RF001]
* - RF002
  - The thematic identifiers that replace this object must exist in the register, or be the thematic identifier of another object reported in the spatial data set.[RF002]
* - RF004
  - The thematic identifier must not exist in the register, unless the wiseEvolutionType value is 'deletion', 'noChange', 'change', 'changeReducedArea', 'changeBothAggregationAndSplitting', or 'changeExtendedArea'. [RF004]
* - RF019
  - A valid 'eu' thematic identifier exists in the register for a relatedZone reported under dcMetadata in the Documents dataset, but was not reported in the geopackage file (either as a spatial object or as a predecessor). The missing thematicididentifiers are: {%RECORDS%} [RF019]
* - V005
  - The thematicIdIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators).[V005]
* - V024
  - The value must not be missing or empty [V024]
```

### thematicIdIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V016
  - The value must not be missing or empty [V016]
* - V032
  - The thematicIdIdentifierScheme must be ‘euFloodsRiskZoneCode'. [V032]
```

### beginLifespanVersion

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R002
  - The beginLifespanVersion value must be reported, if the inspireVersionId value is reported.[R002]
* - R013
  - The beginLifespanVersion value must be reported, if the endLifespanVersion value is reported.[R013]
* - R024
  - The beginLifespanVersion value must be reported, unless the wiseEvolutionType is 'creation' or 'noChange'.[R024]
* - V006
  - The beginLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V006]
```

### endLifespanVersion

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R003
  - The beginLifespanVersion date must not be after the endLifespanVersion.[R003]
* - R025
  - The endLifespanVersion value must be reported, if the wiseEvolutionType is 'deletion'.[R025]
* - V039
  - The endLifespanVersion value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V039]
```

### predecessorsIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R011
  - The object must have zero predecessors, if the wiseEvolutionType value is 'creation'.[R011]
* - R014
  - The predecessorsIdentifier value must be reported, if the predecessorsIdentifierScheme value is reported.[R014]
* - R015
  - The predecessorsIdentifier and predecessorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself).[R015]
* - R026
  - The object must have one and only one predecessor, if the wiseEvolutionType value is 'changeCode' or 'splitting'.[R026]
* - R027
  - The object must have two or more predecessors, if the wiseEvolutionType value is 'aggregation' or 'changeBothAggregationAndSplitting'.[R027]
* - R028
  - The object must have zero predecessors, if the wiseEvolutionType value is 'change' or 'noChange'.[R028]
* - R029
  - If an identifier is the predecessor of 2 or more objects, then those objects must have wiseEvolution in ('splitting','changeBothAggregationAndSplitting') [R029]
* - R032
  - At least one predecessor of an object with wiseEvolutionType value equal to 'splitting' or 'changeBothAggregationAndSplitting' must be reported as predecessor of another spatial object. [R032]
* - RF005
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF005]
* - RF006
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object . [RF006]
* - RF008
  - The object has a predecessor that does not exist in the register. [RF008]
* - RF011
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object . [RF011]
* - V040
  - The predecessorsIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators).[V040]
```

### predecessorsIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R016
  - The predecessorsIdentifierScheme value must be reported, if the predecessorsIdentifier value is reported.[R016]
* - V044
  - The predecessorsIdentifierScheme must be ‘euFloodsRiskZoneCode'. [V044]
```

### successorsIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R018
  - The successorsIdentifier value must be reported, if the successorsIdentifierScheme value is reported.[R018]
* - R019
  - The successorsIdentifier and successorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself).[R019]
* - R033
  - The object has wiseEvolutionType = 'deletion' and is a predecessor to other objects reported in the data set. The identifiers of the successors must be reported consistently. [R033]
* - RF003
  - The thematic identifier that is replacing this object has been superseded, deprecated or is invalid.[RF003]
* - V041
  - The successorsIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators).[V041]
```

### successorsIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R020
  - The successorsIdentifierScheme value must be reported, if the successorsIdentifier value is reported.[R020]
* - V045
  - The successorsIdentifierScheme must be ‘euFloodsRiskZoneCode'. [V045]
```

### wiseEvolutionType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Type of event that produced or modified the version of the object being reported (creation, change, deletion, aggregation, splitting). This attribute is required to explicitly report changes and update the current status of the object in the Water Information System for Europe.
* - Field type
  - WiseEvolutionType
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
* - R012
  - wiseEvolutionType = 'deletion' is the only valid option if the element has a successor.[R012]
* - R031
  - The spatial object must have wiseEvolutionType value equal to 'deletion' if it is also reported as predecessor to another spatial object (this applies across the polygon, line and point files). [R031]
* - V017
  - The value must not be missing or empty [V017]
* - V061
  - Invalid wiseEvolutionType value for this spatial object type. [V061]
```

### nameTextInternational

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V007
  - The nameTextInternational value must be a non-empty string with less than 255 characters. Upper case letters (A to Z) and digits (0 to 9) are allowed (spaces and hiphens can be used as separators).[V007]
* - V023
  - The value must not be missing or empty [V023]
```

### nameText

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V001
  - The used encoding is not correct. Strange characters in nameText field.[V001]
* - V008
  - The nameText value must be a string with less than 255 characters.[V008]
* - V022
  - The value must not be missing or empty [V022]
```

### nameLanguage

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Language code of the language used in the nameText attribute value.
* - Field type
  - NameLanguage
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
* - V018
  - The value must not be missing or empty [V018]
* - V028
  - The nameLanguage value is not a valid ISO 639-2/B language code [V028]
```

### relatedZoneIdentifier

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - RF009
  - The object has an 'eu' related zone that does not exist in the register. [RF009]
* - RF017
  - The relatedZoneIdentifier is deprecated (only objects with wiseEvolutionType = 'deletion' can be have a deprecated relatedZone). [RF017]
* - V042
  - The relatedZoneIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators).[V042]
* - V070
  - The value must not be missing or empty [V070]
* - XC001
  - The relatedZoneIdentifier must be present in dcMetadata table of Document dataset and 'reportingStructuredData' set to 'Yes'. [XC001]
```

### relatedZoneIdentifierScheme

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V030
  - The relatedZoneIdentifierScheme must be ‘euFloodsUnitOfManagementCode' or 'euRBDCode'. [V030]
* - V071
  - The value must not be missing or empty [V071]
```

### validityPeriodBegin

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R034
  - If wiseEvolutionType = 'deletion' and the object has successors, the validityPeriodEnd of the object must be equal to the validityPeriodBegin of the successors. [R034]
* - R035
  - Objects with the same predecessor must have the same validityPeriodBegin value. [R035]
* - RF013
  - If wiseEvolutionType in ('splitting','aggregation','changeBothAggregationAndSplitting','changeExtendedArea','changeReducedArea'), the validityPeriodBegin value must be higher than the validityPeriodBegin value of the predecessor. [RF013]
* - RF014
  - If wiseEvolutionType = 'changeCode', the validityPeriodBegin value must be equal to the validityPeriodBegin value of the predecessor. [RF014]
* - RF015
  - if wiseEvolutionType is in (''change'',''noChange'') then, the validityPeriodBegin cannot be lower than the one stored in the registry for the same element. [RF015]
* - RF016
  - if wiseEvolutionType is in (''changeCode'') then, the validityPeriodBegin cannot be lower than the one stored in the registry for the same element. [RF016]
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

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - R004
  - The validityPeriodBegin date must not be after the validityPeriodEnd.[R004]
* - R030
  - The validityPeriodEnd date must be reported, if the wiseEvolutionType value is 'deletion'.[R030]
* - V010
  - The validityPeriodEnd value must be a valid date in the ISO 8601 extended format value (e.g. YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDTHH:mm:ss).[V010]
```

### hazardCategory

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V073
  - The value must not be missing or empty [V073]
* - V075
  - The value is not a valid member of the referenced list. [V075]
```

### specificHazardType

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V072
  - The value must not be missing or empty [V072]
* - V078
  - The specificHazardType must be 'areaOfPotentialSignificantFloodRisk'. [V078]
```

### sizeValue

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
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

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V037
  - The sizeUOM must have 'km2' value.[V037]
```
