# FloodRiskManagementPlans_MeasureLocation

## Description

Flood Risk Management Plans - Measures - Location
Information on the geographical location of flood risk management measures, to be reported at the most relevant level (e.g. Unit of Management, Flood Risk Zone, River Basin District, or Surface Water Body).
Uniqueness: measureCode + euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Code
  - Description
* - TU0608
  - The combination of measureCode and euFloodsUnitOfManagementCode must be unique
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
* - V0716
  - The value must not be missing or empty
* - XC0633
  - The value of measureCode must exist in table FloodRiskManagementPlans\_Measure
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Unique EU code for the Unit of Management. The identifier must follow the syntax of the WISE (see the guidance for the CA\_UOM element). Required.
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
* - V0714
  - The value must not be missing or empty
* - XC0634
  - The value of euFloodsUnitOfManagementCode must exist in table dcMetadata where reportingStructuredData = 'yes'
```

### euSurfaceWaterBodyCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Unique code for the Surface Water Body used under the WFD.
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

* - Code
  - Description
* - RF0603
  - The value of euSurfaceWaterBodyCode must exist in reference table WFDSurfaceWaterBody
```

### euFloodsRiskZoneCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Unique EU code for the area (or areas) of potential significant flood risk. The identifier must follow the syntax of the WISE.
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

* - Code
  - Description
* - RF0602
  - The value of euFloodsRiskZone must exist in reference table FloodsRiskZone
```

### euRBDCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Property
  - Value
* - Guidance on completion
  - Unique EU code for WFD River Basin District used under the WFD.
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

* - Code
  - Description
* - RF0604
  - The value of euRBDCode must exist in reference table WFDRiverBasinDistrict
```
