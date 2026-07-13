# UnitOfManagement

## Descripción

Unit of Management.
Uniqueness: euFloodsUnitOfManagementCode

## Table Quality Checks

```{list-table}
:widths: 15 85
:header-rows: 1

* - Código
  - Descripción
* - T0005
  - Table UnitOfManagement must have at least one record if WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'No'
* - T0006
  - Table UnitOfManagement must not have any record if WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'Yes'
* - TU0004
  - The euFloodsUnitOfManagementCode must be unique.
* - XC0010
  - WFDCompetentAuthoritiesAndUOMs.wfdRiverBasinDistricts is 'No', table UnitOfManagement must include as euFloodsUnitOfManagementCode all thematicIdentifier of the table UnitOfManagement of the Spatial dataset and only those
* - XC0020
  - The table UnitOfManagement contains records when the record in table dcMetadata has "reportingStructuredData" equal to 'no'.
```

### euFloodsUnitOfManagementCode

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
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

* - Código
  - Descripción
* - V0003
  - The length must be less than or equal to 42
* - V0004
  - The value does not match the pattern to be used
* - V0029
  - The value must not be missing or empty
```

### nationalRelationshipsReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Reference or references will be required on the institutional relationships established in order to ensure co-ordination where the competent authority acts as co-coordinating body for other competent authorities, or when more than one competent authority is established. This should include a list showing the coordinating body and the authorities whose activities it is coordinating, and relationships with other bodies carrying out tasks linked to implementation of the plans including for example civil protection agencies and early warning systems. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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

* - Código
  - Descripción
* - V0028
  - The value must not be missing or empty
* - V0050
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0007
  - The document reference does not exist
```

### international

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Required. Choose from the 'YesNo' codelist values. Is the Unit of Management part of an International Unit of Management?
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

* - Código
  - Descripción
* - V0015
  - The value does not exist in codelist YesNo
* - V0030
  - The value must not be missing or empty
```

### internationalRelationshipsReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. If the answer to International is Yes, provide a reference to the institutional relationships established to ensure coordination where a Unit of Management covers the territory of more than one Member State or includes the territories of non-Member States. Include reference to international agreements, if they exist, and links to further information. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - R0003
  - UnitOfManagement.internationalRelationshipsReference must be reported if international is 'Yes'
* - V0051
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0006
  - The document reference does not exist
```

### otherRelevantRolesReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Conditional. The core responsibilities of the relevant competent authority must be specified for each river basin district or other unit of management. If other relevant roles (such as spatial planning, flood forecasting, flood warning, civil protection) are fulfilled by organisations not defined as competent authorities for the purposes of reporting, reference(s) should be provided identifying these authorities and the roles that they perform. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0052
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0008
  - The document reference does not exist
```

### changeReference

```{list-table}
:widths: 30 70
:header-rows: 1

* - Propiedad
  - Valor
* - Guidance on completion
  - Optional. Reference(s) should be provided to cover any changes in the UoM since the previous cycle of reporting under the Floods Directive, for example covering possible changes in roles and responsibilities in the relevant Competent Authorities to changes in the area of the UoM itself. This should include information on the reasons for the changes and how the changes will support the improved implementation of the FD. Only actual UoMs need to be reported. More than one option can be selected. If more than one, values need to be separated by a semicolon followed by a whitespace. e.g., "value1; value2; value3".
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
* - V0053
  - Duplicate document references exist. The list of values needs to be distinct.
* - XC0003
  - The document reference does not exist
```
