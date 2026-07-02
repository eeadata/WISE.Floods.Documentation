# Floods Directive Reportnet3

## FLOODS INITIAL OVERVIEW 

**3rd reporting**

Units of Management and Competent Authorities:  

 - **[Master dataflow]:** [https://reportnet.europa.eu/dataflow/1052](https://reportnet.europa.eu/dataflow/1052)

 - **[Reporting dataflow]:** [https://reportnet.europa.eu/dataflow/1473](https://reportnet.europa.eu/dataflow/1473)

  

Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk 

 - **[Master dataflow]:** [https://reportnet.europa.eu/dataflow/1186](https://reportnet.europa.eu/dataflow/1186)

 - **[Reporting dataflow]:** [https://reportnet.europa.eu/dataflow/1509](https://reportnet.europa.eu/dataflow/1509) 

  

Floods Risk Management Plans 

 - **[Master dataflow]:** [https://reportnet.europa.eu/dataflow/1243](https://reportnet.europa.eu/dataflow/1243)

 - **[Reporting dataflow]:** To be created 

 

Floods Directive - Floods Hazard and Risk Maps 

 - **[Master dataflow]:** [https://reportnet.europa.eu/dataflow/1252](https://reportnet.europa.eu/dataflow/1252) 

 - **[Reporting dataflow]:** [https://reportnet.europa.eu/dataflow/1587](https://reportnet.europa.eu/dataflow/1587)

  

**2nd Report [Late Reporters]** 

 

Floods Hazard and Risk Maps [2020] 

 - **[Reporting dataflow]:** [https://reportnet.europa.eu/dataflow/1419](https://reportnet.europa.eu/dataflow/1419)

 

Floods Risk Management Plans [2022] 

 - **[Reporting dataflow]:** [https://reportnet.europa.eu/dataflow/1252](https://reportnet.europa.eu/dataflow/1454)

  

**Reporting Order**

Reporting must follow a specific order, as the data released in the first dataflow serves as a reference for subsequent dataflows. As shown in the image, reporting must begin with the Units of Management and Competent Authorities dataflow, followed by Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk. The order of the remaining two dataflows can be chosen freely. 

![Flood Risk](img/Flood_RiskAssessment.PNG)


 

**Unit of management incremental reporting approach**  

The Units of Management and Competent Authorities dataflow must be reported first, as it defines the units of management used in the reporting process. It is the only dataflow where incremental reporting is not allowed. Subsequent dataflows will use the units defined in this initial dataflow to report their data. Users can choose to report data for a single unit of management. The next reporter must append their data to the previously reported data to complete the release (Incremental reporting). 

 

**Access to FHRM & FRMP**

It was decided by the commission that only countries that have reported completely APSFR/PFRA will have access to FHRMP & FRMP dataflows. Only the countries that have reported structuredData in all the RBD/UoM will have access to the dataflows. 

 

**Reporting PDF approach**

All dataflows include the option to generate a PDF report instead of an electronic report. As previously mentioned, reporting must follow a specific sequence due to dependencies between them. If PDF reporting is chosen the following dataflows are going to be blocked 

![Flood Risk](img/Reporting_PDF.PNG)

**Reference Data**

 

- Units of Management and Competent Authorities: 

    - **UoM Spatial:** This dataset contains the descriptive reference data used for validation. Reference data is data that was submitted by MS in this or other directives. In this case, the data shown is from the Water Framework Directive, 3rd River Basin Management plans (for the list of River Basin Districts), the Floods Directive, 2nd cycle (for the list of floods Units of Management) and the country boundaries published by GISCO. 

        - **ReferenceData:** [SOURCE: Wigeon.Floods_Import.reference.v_FloodsUOM_and_WFDRBD] This table list all WFD River Basin Districts reported for the 3rd RBMPs .and all the floods’ Units of Management reporting during the 2nd cycle, to be used as reference in validation. 

        - **CountryBoundaries:** [SOURCE: Wigeon.Wise_Spatial.reference.Country] GISCO country boundaries for validation 

    - **UoM Descriptive:** Reference data is data that was submitted by MS in this or other directives. In this case, the data shown is from the Water Framework Directive, 3rd River Basin Management plans. 

        - **WFDCompetentAuthorities:** [SOURCE: Wigeon.Floods_Import.reference.v_WFDCompetentAuthorities] 

  

- Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk 

    - This dataset contains the descriptive reference data used for validation. Reference data is data that was submitted by MS in this or other directives. 

        - **RelatedZones:** [SOURCE: Wigeon.Floods_Import.reference.v_FloodsUOM_or_WFDRBD_reporting] This table contains either the River Basin Districts reported to the 3rd RBMPs in WFD or the Floods Units of Management reported to the 3rd reporting cycle of Floods Directive. Depending the values reporting under the Competent Authorities and Units of management dataflow, the RBDs or UoMs will be listed. 

        - **ReferenceData:** [SOURCE: Wigeon.Floods_Import.reference.V_FloodsRiskZone_reporting] This table contains the list of Areas of Potential Significant Flood Risk were reported to the 1st and 2nd cycles of the Floods Directive and that are still active. 

  

- Floods Risk Management Plans 

    - This dataset contains the descriptive reference data used for validation. Reference data is data that was submitted by MS in this or other directives. 

        - **WFDMeasureCode:** [SOURCE: Wigeon.Floods_import].reference.v_WFDMeasureCodes ] 

        - **FloodsUnitsOfManagement_WFDRBD:** [SOURCE: Wigeon.Floods_import.reference.v_FloodsUOM_or_WFDRBD_reporting] 

        - **FloodsRiskZone:** [SOURCE: Wigeon.Floods_Import.reference.V_FloodsRiskZone_reporting] 

  

- Floods Hazard and Risk Maps 

    - This dataset contains the descriptive reference data used for validation. Reference data is data that was submitted by MS in this or other directives. 

        - **ProtectedArea:** [SOURCE: Wigeon.Floods_Import.reference.v_ProtectedArea] 

        - **FloodsUnitsOfManagement_WFDRBD:** [SOURCE: Wigeon.Floods_import.reference.v_FloodsUOM_or_WFDRBD_reporting] 

        - **FloodsRiskZone: FloodsRiskZone:** [SOURCE: Wigeon.Floods_Import.reference.V_FloodsRiskZone_reporting] 

  

- Floods Risk Management Plans [2022]:  

    - This dataset includes all the reference data used for QCs in the reporting datasets. WFD reference data comes from the 2nd River Basin Management Plans. The list of Floods Risk Zones (Areas of Potential Significant Flood Risk) come from the list of APSFRs provided in both 1st and 2nd Flood Directive reporting. 

        - **WFDMeasureCode:** [SOURCE: Wigeon.Floods_Import.reference.v_WFDMeasureCodes_lateReporters] 

        - **FloodsUnitsOfManagement_WFDRBD:** Wigeon.Floods_Import.reference.v_FloodsUOM_or_WFDRBD_lateReporters] 

        - **FloodsRiskZone:** [SOURCE: Wigeon.Floods_Import.reference.FloodsRiskZone] 

  

- Floods Hazard and Risk Maps [2020]  

    - This dataset contains all the reference data used for the QC processes. Reference data has been loaded using previously reported data to the Floods and Water Framework Directives. For WFD, data reported in the 2nd River Basin Management Plans has been loaded. 

        - **ProtectedArea:** [SOURCE: Floods_Import.reference.v_ProtectedArea_lateReporters] 

        - **FloodsUnitsOfManagement_WFDRBD:** [SOURCE: Wigeon.Floods_Import.reference.v_FloodsUOM_or_WFDRBD_lateReporters ] 

        - **FloodsRiskZone:** [SOURCE: Wigeon.Floods_Import.reference.FloodsRiskZone] 

 **Directive Overview**

 ![Flood Risk](img/DirectiveOverview.PNG)

 **General information** 


```{table} Urls of the project 
:width: 100%
  
| Repository | Path |
|---|---|
| CWS Folder | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3` |
| SVN Repositories | [Floods_ReportNet3](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/) |
| Taskman | [260913](https://taskman.eionet.europa.eu/issues/260913)  |
| Reportnet3 (production environment [MASTER]) | [dataflow/1052](https://reportnet.europa.eu/dataflow/1052)<br>[dataflow/1186](https://reportnet.europa.eu/dataflow/1186 ) |
| Reportnet3 sandbox (testing environment for developers)  |  |
| Reportnet3 (MS Testing phase environment) |  |
| Reportnet3 final dataflow for reporting | |
```


```{table} Data model  
:width: 100%

| Repository | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Enterprise Architect|
| SVN | [FloodDirective_ReportNet3_EnterpriseArchitect](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Enterprise%20Architect/) <br/> [BWD_ReportNet3_EnterpriseArchitech](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/BathingWaterReporting/BWD_ReportNet3/Enterprise%20Architect/BWD_Data_Model.qea) |
| Taskman | [262860](https://taskman.eionet.europa.eu/issues/262860)<br>[262417](https://taskman.eionet.europa.eu/issues/262417)<br>[261344](https://taskman.eionet.europa.eu/issues/261344)<br>[262463](https://taskman.eionet.europa.eu/issues/262463)|
```
```{table} Decision log  
:width: 100%
| Repository | Path |
|---|---|
| Taskman | [https://taskman.eionet.europa.eu/projects/wise/wiki/Decision_log](https://taskman.eionet.europa.eu/projects/wise/wiki/Decision_log)  
Entries with Category Floods to RN3  |
```


```{table} Contact list 
:width: 100%

| |
|---|
| **EEA** |
| • [Fernanda Néry](mailto:Fernanda.Nery@eea.europa.eu) |
| **EC** |
| • ?? |
```

 ## Helpdesk
 
 It is a dedicated platform where countries can report questions and request access to RN3, and where our team provides support. 
 
 ### Good practices
 
 - When a helpdesk come, we will rename the helpdesk adding to the subject the "[countrycode] - subject". This is done in "Miscellaneous – Free fields".
 ![Miscellaneous–Free fields](img/FreeField.PNG)
 - If questions about different QC are submitted through the same helpdesk ticket, we split the ticket into as many as unrelated questions there are. In this way we don't have to wait to answer when we have analized all the problems they have.
 - Once we have answered the questions, we close the ticket. If they have more related questions the ticket will be opened again when they answer. We cannot leave the ticket open if it has been solved.
 - We have to try to answer in less than 2 days. If it is impossible, we have to answer telling them that we are looking into it.
 
 A list of frequent questions that we can use as a template: 
 
 | FAQ | Answer |
 |---|---|
 | | |

 ## Floods Databases

| Server | Database | Purpose |
|---|---|---|
| WIGEON | Floods_Import | The harvested data, codelists and reference data for the reporting flows will go here. Eventually, if any automated QC is needed during the final feedback phase, it will run here too. Once everything is setup, we expected that only automated processes will write into the database (e.g. fmeservice). There won't be many human users requiring ddl_admin or write permissions there. |
| WIGEON | Floods_Production | The data processing will be done here. Most of the team will likely need ddl_admin and writer and reader permissions. |
| WIGEON | Floods | This database will contain the authoritative floods products. A very limited number of users will be able to write here, typically replacing the existing data with newer versions when available and approved. On the other hand, there will likely be a large number of user that will be able to read the data (but those users will likely already belong to other LDAP groups, say WFD_reader members might also need to use the floods data). |
| WIGEON | Floods_Archive | All archived data related to floods will be kept here. Team members will not be able to write in this database except owners. All team members will be able to read. |
| WIGEON | Floods2018 | Soon to be moved to Floods_Archive. It contains information reported by member states in the 2nd reporting cycle. |
| WIGEON | Floods2010 | Soon to be moved to Floods_Archive. It contains information reported by member states in the 1st reporting cycle. |
| WIGEON-DEV | Floods_Import | Test database. Will be used mainly to test harvest and postprocessing procedures. Does not contain any real data. |
| WIGEON-DEV | Floods_Production | Test database. Will be used mainly to test harvest and postprocessing procedures. Does not contain any real data. |

 ## Cloning a dataflow and creating data collections 

**Cloning dataflow**
1. In "RN3" -> "Dataflows", click on left menu option "+" sign
2. Set dataflow title (original, adding " [year]" at the end)
3. "Search obligation", insert it (this must be requested)
4. For cloning the schema, we have two options: (The experience has told us that is better importing than cloning)
   - a. "New schema" -> "Clone all schemas from dataflow"
   - b. Export the original dataflow and import it as a zip file
5. Rename each box, remove "CLONE_" (if 4.a has been chosen) or "IMPORTED_" (if 4.b has been chosen)
6. Review datasets' checks:
   - a. Codelist, reference data:
     - i. "Reference dataset": checked
     - ii. "Available in public view": checked
   - b. Reporting data (descriptive and spatial):
     - i. "Reference dataset": unchecked
     - ii. "Available in public view": unchecked
7. Review tables' checks (must coincide with original dataflow's ones)
8. Review tables' fields:
   - a. PK, Required, Read only checks
   - b. Names
   - c. Descriptions
   - d. Field types
   - e. Linked tables (in link type fields)
9. Review no. of QCs (must coincide with original dataflow's ones)
10. Check QCs codes from reporting data (descriptive and spatial), to make sure automatic ones haven't been reset
11. Make sure to have codelist and reference data records inserted and, if necessary, updated. Validate them (for refreshing materialized views)
12. Enable/disable corresponding QCs, if necessary (e.g. for late reporters)
13. Validate QCs through "QC rules" -> "Validate all QCs" in reporting data (descriptive and spatial)
14. Validate reporting data (descriptive and spatial) test cases through test files
15. Test import/export
16. Copy whatever information is in the Dataflow Help
17. Complete, if necessary:
    - a. Dataflow description
    - b. Tables descriptions
    - c. Fields descriptions
 

**Creating test data collection**

1. Create a "test" lead reporter. Click on "Manage lead reporters": 
    - a. Country: Spain 
    - b. Email address: you@yourdomain.com. Make sure that, when introducing the email address, a "✓" appears on the person emoticon, to make sure the email address exists in RN3 
    - Click on "Update permissions". 
2. "Create data collection" button will be enabled after step 1. Click on it. This step will take a while to complete. 
3. Get into every: 
    - **a. Blue with pencil & rule icon**
    - **b. Green book icon**
    - **c. Blue three sheets icon**
    - **d. Pink box icon** 
to make sure no RN3 error is thrown when loading them 
4. Validate reference data and codelist datasets in the blue (book icon) square. For the "Validate" button to be enabled, unblock it from the "Update status" button with a lock on the left menu. Be sure to block them again when the validations are done. 
5. Validate reporting data (descriptive and spatial) test cases through test files. 

 
**Create countries' data collections** 

1. Click on "Public status" button on the left menu and uncheck "Dataflow public info is available" 
2. Retrieve the countries which will need access to the dataflow (probably in the Taskman task; check the decision log, to make sure there are no changes) 
3. Get the lead reporters' email addresses either from:
    - [Helpdesk](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Helpdesk/FLOODS%20REPORTERS.xlsx)
    - the [TEST-DEV] or [TEST-MS] equivalent dataflow or  
    - https://www.eionet.europa.eu/ldap-roles/, filtering by "*-[countryCode]" and "Ctrl + F" -> "Floods" (in the "Users in Floods Directive Data Reporters [country]" part) 
4. **IMPORTANT: Create each countries' data collections separately. This is, for steps 5 -> 7 introduce only one countries' lead reporters (5), click on "Create data collections" (6) and check that the process was executed successfully (7). Repeat these three steps for each of them**
5. Create the lead reporters (make sure that, when introducing each email address, a "✓" appears on the person emoticon, to make sure the email address exists in RN3) through the "Manage lead reporters" button: 
    - a. Country: the corresponding one 
    - b. Email address: email address retrieved from step 3 
    Click on "Update permissions". 

6. Click on "Create data collections". This step will take a while to complete. 

7. **Get into each country's reporting (blue database icon) box and check that it shows the country name correctly after the dataflow's name (blue font) as, at some moment, RN3 didn't recognize it and was showing "null"**

8. Validate reference data and codelist datasets in the blue (book icon) square. For the validate button to be enabled, unblock it from the "Update status" button with a lock on the left menu. Be sure to block them again when the validations are done. 

9. When everything is checked and in its place, before informing the countries, click on "Public status" button on the left menu and check "Dataflow public info is available" 

## Harvesting 
Taskman 284310 - [APSFR + PFRA](https://taskman.eionet.europa.eu/issues/284310) Harvesting 

Taskman 284308 - [CA-UoM](https://taskman.eionet.europa.eu/issues/284308) Harvesting 

Taskman 284312 - [FHRM](https://taskman.eionet.europa.eu/issues/284312) Harvesting 

Taskman 284314 - [FRMP](https://taskman.eionet.europa.eu/issues/284314) Harvesting 

**Database**

Destination database: **[WIGEON].[Floods_Import]**

**Schemas** used in destination database: 

| | Data | Template |
|---|---|---|
| APSFR | harvestedData_APSFR | template_APSFR |
| PFRA | harvestedData_PFRA | template_PFRA |
| **APSFR/PFRA Documents** | harvestedData_APSFR_PFRA_Documents | template_APSFR_PFRA_Documents |
| CA_UOM | harvestedData_CAUOM | template_CAUOM |
| FHRM | harvestedData_FHRM | template_FHRM |
| FRMP | harvestedData_FRMP | template_FRMP |
| **[Late Reporters].[FHRM]** | harvestedData_FHRM_2020 | template_FHRM_2020 |
| **[Late Reporters].[FRMP]** | harvestedData_FRMP_2022 | template_FRMP_2022 |

User fmeservice created in destination database. 

**FME Server**

**Automation used:** [RN3_Floods_Harvesting](https://fme.discomap.eea.europa.eu/fmeserver/automations/db8e2836-f8ba-4b7c-9998-0f03de3ec182) 
**Generic harvesting workspace used:** [RN3_Generic_Harvesting](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/WISE/RN3_Generic_Harvesting.fmw) 
**Attachments' harvesting workspace used:** [RN3_Generic_Harvesting_Attachments](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Dataflows_RN3_Generic_Processes/RN3_Generic_Harvesting_Attachments.fmw)


**Attachments harvesting**

**Attachments' harvesting APSFR/PFRA**
Taskman 292409 - [APSFR + PFRA](https://taskman.eionet.europa.eu/issues/292409) Attachments Harvesting 
Attachments uploaded to \\cwsfileserver.eea.dmz1\system\RN3_attachment\872\1509 


**Attachments' harvesting CA_UOM**
Taskman 292407 - [CA-UoM](https://taskman.eionet.europa.eu/issues/292407) Attachments Harvesting 
Attachments uploaded to \\cwsfileserver.eea.dmz1\system\RN3_attachment\871\1473 


**Attachments' harvesting FHRM** 
Taskman 292398 - [FHRM](https://taskman.eionet.europa.eu/issues/292398) Attachments Harvesting 
Attachments uploaded to \\cwsfileserver.eea.dmz1\system\RN3_attachment\874\1587 


**Attachments' harvesting FRMP**
Taskman 292400 - [FRMP](https://taskman.eionet.europa.eu/issues/292400) Attachments Harvesting 
Attachments uploaded to  \\cwsfileserver.eea.dmz1\system\RN3_attachment\873\1909  


**Attachments' harvesting [Late Reporters].[FRMP]**
Taskman 292447 - [Late Reporters].[FRMP](https://taskman.eionet.europa.eu/issues/292447) Attachments Harvesting 
Attachments uploaded to \\cwsfileserver.eea.dmz1\system\RN3_attachment\778\1454 


**Attachments' harvesting [Late Reporters].[FHRM]**
Taskman 292448 - [Late Reporters].[FHRM](https://taskman.eionet.europa.eu/issues/292448) Attachments Harvesting 
Attachments uploaded to \\cwsfileserver.eea.dmz1\system\RN3_attachment\777\1419 

 

**Attachments' harvesting database parameters:**
- [RN3].[metadata].[HarvestingParameters].[attachmentParentPath] = '\\cwsfileserver.eea.dmz1\system\RN3_attachment' 
- [RN3].[metadata].[HarvestingParameters].[attachmentHarvestingJobs_Table] = 'AttachmentHarvestingJobs' 

## Harvesting V3

We use FME “RN3_Generic_Harvesting.fmw” to harvest data from RN3. It uses version 2 of RN3's API endpoint “etlExport”. It is a synchronous process that fails when harvesting some spatial data of Floods. The solution is using a Generic Harvesting FME that Marek is developing, “RN3_Generic_Harvesting_Data_and_Spatial_etlExport_v3_NR.fmw”, that uses version 3 of RN3’s API endpoint “etlExport”, that it is asynchronous. 

For the moment, Marek’s FME is not fully compatible with the harvesting FME we use now. The incompatibilities and changes are: 

 We use FME “RN3_Generic_Harvesting.fmw” to harvest data from RN3. It uses version 2 of RN3's API endpoint “etlExport”. It is a synchronous process that fails when harvesting some spatial data of Floods. The solution is using a Generic Harvesting FME that Marek is developing, “RN3_Generic_Harvesting_Data_and_Spatial_etlExport_v3_NR.fmw”, that uses version 3 of RN3’s API endpoint “etlExport”, that it is asynchronous. 

For the moment, Marek’s FME is not fully compatible with the harvesting FME we use now. The incompatibilities and changes are: 

1) Tables [RN3].[metadata].[DataflowTables] and [RN3].[metadata].[HarvestingParameters] contain database connections to SQL Server of type “JDBC” (their name ends with “_JDBC”). Marek’s FME expects non-JDBC database connections. Before using it, database connections involved in the harvesting need to be changed to non-JDBC connections. 


2) Table [RN3].[metadata].[DataflowTables] needs two additional columns of type ‘bit’: 
    - [flag_keep_geojson]: if equal to 1, the reported GeoJSON in RN3 will be harvested in SQL Server as ‘nvarchar(max)’ data type. 
    - [flag_update_geometry]: if equal to 1, the geometry reported in RN3 will be harvested in SQL Server as ‘geometry’ data type. 
For Floods’ spatial tables, [flag_keep_geojson] is set to 1 and [flag_update_geometry] is set to 0. 

 

3) New table [RN3]. [metadata].[DataflowTables_GeometryFields] that defines in what table columns to harvest the spatial data reported in RN3. 

CREATE TABLE [metadata].[DataflowTables_GeometryFields]( 
[dataflowId] [bigint] NULL, 
[dataflowName] [nvarchar] (255) NULL, 
[dataCollectionId] [bigint] NOT NULL, 
[table_RN3_Name] [nvarchar] (255) NOT NULL, 
[field_RN3_Geometry] [nvarchar] (255) NOT NULL, 
[field_SQL_Geometry] [nvarchar] (255) NOT NULL 
) 

Content of the table to harvest Floods’ spatial data:  

![Flood Harvest](img/Harvest.PNG)

4) Harvesting documents: Current harvester, "RN3_Generic_Harvesting.fmw", stores different values, separated by ':', in table columns corresponding to files reported in RN3. For example: 
"EL07_2RV_P6.7.pdf:1376:75915:2CBDD4B471EDBC6A73760D720D39B0E9" 
"RN3_Generic_Harvesting_Data_and_Spatial_etlExport_v3_NR.fmw" simply stores the name of the file. That means "RN3_Generic_Harvesting_Attachments.fmw" cannot harvest documents from RN3 if Marek’s FME to harvest is used. 

A future version of Marek’s FME will harvest documents as well as descriptive and spatial data. While we wait for it, we can harvest everything except spatial data with current FME harvester and spatial data using this new FME harvester. 

Marek's FME to harvest data from RN3 is at FME Flow Server, "Nature Directives" repository. When it is fully developed, it will be in repository "Dataflows_RN3_Generic_Processes": 
https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/NatureDirectives_RN3/RN3_Generic_Harvesting_Data_and_Spatial_etlExport_v3_NR.fmw 

 

Marek's TAskman task: 
**[RN3_Generic_Harvesting] Harvesting using etlexport v3**
https://taskman.eionet.europa.eu/issues/290765 

## Publication in Discodata

The publication on Discodata for the third cycle has been implemented and it is now automatic. 

First the views need to be created in [Floods_Import]  Database. They views need to be rceate using the Discodata approahc if a field can have multiple values then, the field needs to be shown in a new table.  

Once the views are correctly generated in [Floods_import] we need to populate the [Floods_Import].[metadata].[TableData_TableMetadata] table where we match the real name of the table with the name of the view in discodata schema to be able to join the metadata information corretcly.  

We also need to bulk the information metadata from Enterprise architect to the [Floods_Import] database. For example: [Floods_Import].[metadata_APSFR].[MetadataFromEA] 

 
Then we need to execute the stored Procedures in [Floods] database, first the one to create the tables [CreateTablesToPublish] and then the one for creating the views [CreateViewsToPublish] were we exclude certain fields due to confidentiality.  

 
Once the views are created, we published the first time creating a new version and revision and then we publish on Discodata using Automations: 

 
Taskman: https://taskman.eionet.europa.eu/issues/292606  

 
Automation FME CAUOM: [https://fme.discomap.eea.europa.eu/fmeserver/automations/aaf53552-3d10-44fc-918e-4ff7b3fe71c6](https://fme.discomap.eea.europa.eu/fmeserver/automations/aaf53552-3d10-44fc-918e-4ff7b3fe71c6) set to be running every Monday at 21.00 

Automation FME PFRA: [https://fme.discomap.eea.europa.eu/fmeserver/automations/2490c132-d8b9-4e3f-8538-a5caf650f01e](https://fme.discomap.eea.europa.eu/fmeserver/automations/2490c132-d8b9-4e3f-8538-a5caf650f01e) set to be running every Monday at 22.00 

Automation FME APSFR: [https://fme.discomap.eea.europa.eu/fmeserver/automations/2490c132-d8b9-4e3f-8538-a5caf650f01e](https://fme.discomap.eea.europa.eu/fmeserver/automations/39d17f5e-fa6c-4767-b98c-f5d4260971a2)   set to be running every Monday at 21.30 

Automation FME FHRM: [https://fme.discomap.eea.europa.eu/fmeserver/automations/2490c132-d8b9-4e3f-8538-a5caf650f01e](https://fme.discomap.eea.europa.eu/fmeserver/automations/63cb4b6a-0af9-4ee2-bd15-1475874ee6df)  set to be running every Monday at 23.00 

 
## Units of Management and Competent Authorities 

The Master dataflow is :  [https://reportnet.europa.eu/dataflow/1052](https://reportnet.europa.eu/dataflow/1052)
Testing dataflows are: 
Testing Dataflow Reportnet3: [https://reportnet.europa.eu/dataflow/1202](https://reportnet.europa.eu/dataflow/1202)
Testing Dataflow Reportnet3 sandbox: [https://sandbox.reportnet.europa.eu/dataflow/9952](https://sandbox.reportnet.europa.eu/dataflow/9952) 
Testing dataflow for reporting countries: [https://sandbox.reportnet.europa.eu/dataflow/1263](https://reportnet.europa.eu/dataflow/1263) 



And it is composed by: 

**Descriptive UoM:**  [https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926]

**Descriptive codelist:** [https://reportnet.europa.eu/dataflow/1052/datasetSchema/67309] 

**UoM Spatial :** [https://reportnet.europa.eu/dataflow/1052/datasetSchema/67542] 

**Spatial Codelist:** [https://reportnet.europa.eu/dataflow/1052/datasetSchema/67546]

**Spatial reference Data:** [https://reportnet.europa.eu/dataflow/1052/datasetSchema/67659]



**Spatial:**

Spatial report has three main datasets:  

 
UoM spatial: where the reporters will send the data.  

Reference data: composed by UoM reported in the previous reporting cycle, and all the RBD in wfd 

Codelist: all the codelist used in spatial  

 ### FME

 
#### Import - Spatial data 

**FME name** -Import_UoM_Spatial_data.fmw

**Descriptive Summary** 

This FME imports spatial data reported by the Member States to RN3. The FME currently supports Geopackages format.  

 
**Areas of impact in the dataflow**

The FME is called from the “External integrations” of the “Spatial data” dataset. 


```{table} Related resources 
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Spatial\IMPORT\IMPORT_UoM ` |
| SVN | [\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Spatial\IMPORT\IMPORT_UoM\Import_UoM_Spatial_data.fmw] |
| FME Server | [Import_UoM_Spatial_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_UoM_Spatial_data.fmw ) |
| Taskman | [issues/264752](https://taskman.eionet.europa.eu/issues/264752) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
| | FME_Authors | Full access |
| | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- Geopackage. 

**Output data**

The dataset of “Spatial data” will be filled in with the data reported in the uploaded files.  


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | [67542](https://reportnet.europa.eu/dataflow/1052/datasetSchema/67542) |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `67542/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | The url where the input file (geopackage, shapefile or GML) is. If it is a shapefile, the input file must be a zip file. If it is a GML, the inputfile must be a GML or a zip file. If it is a geopackage, it must be the geopackage (uncompressed). | `\\Serval\s\Common workspace\Water\DataFlows\BWD_ReportNet3\FME\ExportFiles\testIru.gpkg` |
```

#### Import - Descriptive data

**FME names** 

**Reporting dataset:** Import_CA_UOM_descriptive_data.fmw <br>
**Documents dataset:** Import_CA_UOM_descriptive_data_Documents.fmw 


**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "Descriptive Reporting" and "DOCUMENTS" datasets, located in the "Floods Directive - Units of Management and Competent Authorities" dataflow. 
The FME is called from the "External integrations" of the mentioned dataset. 



```{table} Related resources 
:width: 100%

| Type | Path |
|---|---|
| CWS | Reporting dataset:`\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_CA_UOM\Import_CA_UOM_descriptive_data` <br> Documents dataset:`\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive2018\ReportNet3\FME\Descriptive\IMPORT_CA_UOM\Import_CA_UOM_descriptive_data_Documents`  |
| SVN | Reporting dataset: [Import_CA_UOM_descriptive_data](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_CA_UOM/Import_CA_UOM_descriptive_data.fmw) <br> Documents dataset: [Import_CA_UOM_descriptive_data_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_CA_UOM/Import_CA_UOM_descriptive_data_Documents.fmw)  |
| FME Server | Reporting dataset: [Import_CA_UOM_descriptive_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_CA_UOM_descriptive_data.fmw)<br> Documents dataset:[Import_CA_UOM_descriptive_data_Documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Import_CA_UOM_descriptive_data_Documents.fmw)  |
| Taskman | [issues/264168](https://taskman.eionet.europa.eu/issues/264168)  |
```
 

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
| | FME_Authors | Full access |
| | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
 
**Input data**

- SQLite database (.db3 files). 

**Output data**

Zip file containing different csv files for each different table we will fill in RN3. 

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | Id for the dataflow we can find within the url, e.g.:[1052](https://reportnet.europa.eu/dataflow/1052)  | In the case of the example:1052  |
| DatasetId | id for the dataset we can find within the url, e.g.:[https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926]  | In the case of the example: 65926  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `65926/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | Path where the SQLite input file (db3) is stored. | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_CA_UOM\Floods_CA_UOM.db3` |
```
#### Prefill-Spatial reference data

FME name 

**Descriptive Summary**
The reference table created to generate the spatial reference table, which also can be used as prefill data to be used by the reporters, have two different source. 

**First source:** reference table created to join all the valid UoM reported in the previous Floods reporting. [https://taskman.eionet.europa.eu/issues/262823]
If they reported an UoM that is the same as RBD the code will be used as predeccesor and the thematicidentifier scheme will be replace with the code+UOM. 

**Secondsource:** [WFD2022_SPATIAL].[data].[RiverBasinDistrict_V] 

**Areas of impact in the dataflow**

 The reference table in the dataflow will be updated with the data storage in the Database from previous reportings 
```{table} Related resources  
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive2018\ReportNet3\Database\Spatial\Reference Data\UOM\View_UoM_reference.sql` |
| SVN | [View_UoM_reference](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Spatial/Reference%20Data/UOM/View_UoM_reference.sql) |
| Taskman | [issues/262823](https://taskman.eionet.europa.eu/issues/262823)&<br>[issues/265217](https://taskman.eionet.europa.eu/issues/265217) |
```
 
**Input data**
SQL data from previous reporting + WFDRBD 2022 and country boundaries geometries tables 

 
**Output data**
Refence tables uploaded in Reportnet 3 by country


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example. |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| countryCode | If a country code is passed as a parameter, the FME will act as a prefill of protected areas for the specific country | ES |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |

```
#### Export - Spatial data 

**FME name** - Uom_export.fwe 

**Descriptive Summary**

The fme created is an external integration for Repornet 3 with the aim to download as Geopackage all the information that they have uploaded into Repornet'3 Uoms spatial datatset.  

Note that if the first records does not have a geometry the geopackage will be create without any EPSG assigned. Since the geometry is mandatory is not  aproblem.  


**Areas of impact in the dataflow**
The FME is called from the “External integrations” of the “Spatial data” dataset. 

```{table} Related resources  
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Spatial\EXPORT\EXPORT_UOM\Export_UoM.fmw` |
| SVN | [Export_UoM](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Spatial/EXPORT/EXPORT_UOM/Export_UoM.fmw) |
| FME Server | [Export_UoM_Spatial_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_UoM.fmw/fmejobsubmitter) |
| Taskman | [issues/264752](https://taskman.eionet.europa.eu/issues/264752) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
| | FME_Authors | Full access |
| | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**
As we want a geopackage, it will receive 'gpkg'. 

 

**Output data**
A Geopackage will be downloaded in the local computer with all the data and geometries that were uploaded in Repornet3 dataset 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example. |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| countryCode | If a country code is passed as a parameter, the FME will act as a prefill of protected areas for the specific country | ES |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName  | The name that the exported file will have. | For instance:test_2024  |
| format  | The file type we want to export. | `gpkg` |

```

#### Export – Descriptive data 
**FME names:** 

Reporting dataset: Export_UoM_Descriptive.fmw 
Documents dataset: Export_UoM_Descriptive_Documents.fmw 

**Descriptive Summary** 

Generates a db3 SQLITE file with all the data included in the RN3 "Descriptive Reporting" and "DOCUMENTS" datasets, located in the "Floods Directive - Units of Management and Competent Authorities" dataflow, that you can download to your local computer.  
These FME are called from the "External integrations" of the mentioned datasets. 

**Areas of impact in the dataflow**

If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data  



```{table} Related resources 
:width: 100%

| Type | Path |
|---|---|
| CWS | Reporting dataset:`\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive2018\ReportNet3\FME\Descriptive\EXPORT_CA_UOM\Export_UoM_Descriptive` <br> Documents dataset:`\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive2018\ReportNet3\FME\Descriptive\EXPORT_CA_UOM\Export_UoM_Descriptive_Documents`  |
| SVN | Reporting dataset: [Export_UOM_descriptive_data](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_CA_UOM/Export_UoM_Descriptive.fmw)<br>Documents dataset:[Import_UOM_descriptive_data_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_CA_UOM/Export_UoM_Descriptive_Documents.fmw)  |
| FME Server | Reporting dataset: [Export_CA_UOM_descriptive_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_UoM_Descriptive.fmw)<br>Documents dataset:[Import_CA_UOM_descriptive_data_Documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Export_UoM_Descriptive_Documents.fmw)  |
| FME Server | Reporting dataset: [Export_CA_UOM_descriptive_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_UoM_Descriptive.fmw)<br>Documents dataset:[Import_CA_UOM_descriptive_data_Documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Export_UoM_Descriptive_Documents.fmw)  |
| Taskman | [issues/264168](https://taskman.eionet.europa.eu/issues/264168) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
| | FME_Authors | Full access |
| | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```


**Input data**
RN3 dataset database data. 

 

**Output data**
SQLite db3 file containing each different table existing in RN3. 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | In the case of the example: 9413  |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| countryCode | If a country code is passed as a parameter, the FME will act as a prefill of protected areas for the specific country | ES |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName  | The name that the exported file will have. | For instance:test_2024  |
| `SQLITE_TEMPLATE_CREATION_SCRIPT` | FME flow path where to get the database template from.  | `$(FME_SHAREDRESOURCE_DATA)/Floods/CA_UOM_Template_Database.sql` (reporting dataset)<br>`$(FME_SHAREDRESOURCE_DATA)/Floods/CA_UOM_Template_Database_Documents.sql` (documents dataset)  |
```

#### Export – Harvesting process 

The export of data from RN3 to SQL Server is done through a generic harvesting process which is documented in the following link: 
From RN3 to SQL Server  [Web link](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={fd0a2b2b-369d-47f4-af64-e3cb637a972f}&action=edit&wd=target%28From%20RN3%20to%20SQL%20Server.one%7Ce12603f6-7721-4d46-8859-6a3e39cffb50%2FIntroduction%7Cdda065eb-8020-4ebe-8bbc-bb6019f3fca3%2F%29&wdorigin=NavigationUrl) 


Additionally, the database is called [Floods_Import] under [WIGEON] SQL Server. 

 

More information about the database can be found on the following page: 
Database  [Visit Web](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28DWD%20Reportnet3.one%7C6d0878a4-aa18-477f-9cf4-a50dab6f67c8%2FDatabase%7Cbe7d4c42-a3b6-47d1-98ec-6ee5027c489b%2F%29&wdorigin=NavigationUrl) 

**Automation at FME**

The harvesting process has been automated in FME Server through an "Automation" called **RN3_Floods_Harvesting**, you can find it in the following link: [https://fme.discomap.eea.europa.eu/fmeserver/#/automations](https://fme.discomap.eea.europa.eu/fmeserver/#/automations)


This FME Automation runs the generic harvesting process through a schedule every day and if an error has occurred sends a notification to wfd.helpdesk@eionet.europa.eu. 

![FME Automation](img/FME_Export_Harvest.PNG) 

From Floods_import to Floods_production 
There is an automation to pass all the data harvested in Floods_Import to Floods_Production.  

 

FME: PostProcessing_Floods_Import_To_Floods_Production 

SVN: 

### QC


**Guidance to create testing files for ReportNet 3** 

This guidance contains best practices and it is independent of the file format used, whether Excel files, SQLite files or any other format. 

The testing files should be based on the templates to report and the definition of the QC. They should be able to test that valid data is considered as such and that invalid data is detected. 

**Best practices:**

Each QC must have two records in the testing files at least. One of them with valid data that should not raise and error and other with incorrect data that must raise an error. Some QC might need more records in order to test all possible situation. For example, QC that depend on the combination of several columns in a record. This is the most important phase of the definition of testing files: analysing all the possibilities that a QC requires to be tested. 

For table columns with cardinality “0..*”, there must be testing data without a value, with one value only and with multiple values. For table columns with cardinality “1..*”, there must be testing data with one value only and with multiple values. This is especially important for table columns with those cardinalities involved in QC, because multiple values (for example, “one; two; three”) must be selected individually in SQL commands using the SQL function “unnest”, to get individual records with “one”, “two”, three”. 

The record with valid data must have a column that contains the code of the QC and “_OK” in order to know that that record should pass the QC. For example: if there is a QC with code “V001” to test a WISE Identifier that must start with the country code and it must match a regular expression, the content of that column can be: “ES1_V001_OK”. 

The record with invalid data must have a column that contains the code of the QC and “_ERROR” in order to know that that record should pass the QC. For example: if there is a QC with code “V001” to test a WISE Identifier that must start with the country code and it must match a regular expression, the content of that column can be: “ES1__V001_ERROR”. 

In the previous cases, the column to be checked by the QC was the column that contained the QC code. That cannot be possible if the column to be checked by the QC does not allow text or must contain a value from a codelist. In that case, other column must contain the QC code that the record is testing. 

The importance of having the QC codes in the test files is twofold: 

1. After the validation of the test files in ReportNet 3, the records show the valid and invalid data with their corresponding QC code. 

2. In case a QC is modified, we might need to edit the test files and having the QC codes in them allows us to find the records to edit quite easily. 

    The testing files should allow us to identify these situations, that we have to check after importing and validating the test files in ReportNet 3: 
    - True positives: valid data for a QC that is validated as valid. 
    - False negatives: valid data for a QC that is validated as invalid. 
    - True negatives: invalid data for a QC that is validated as invalid. 
    - False positives: invalid data for a QC that is validated as valid. 

 
#### QC Spatial

Complete list: [Floods_Spatial_QC-RiskZone_HazardZone_UoM](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Floods_Spatial_QC-RiskZone_HazardZone_UoM.xlsx)


```{table} Spatial QCs
:width: 100%

| Spatial QCs | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Developers\mmarcos\FLOODS_SVN\ReportNet3\QC\Spatial\/Floods_Spatial_QC-RiskZone_HazardZone_UoM.xlsx` |
| SVN | [Spatial QC](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Floods_Spatial_QC-RiskZone_HazardZone_UoM.xlsx) |
| Taskman | [264323](https://taskman.eionet.europa.eu/issues/264323) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented):


```{table} QCs exported from RN3
:width: 100%
| QC export from RN3 | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\CompetentAuthoritiesAndUnitsOfManagement\QC\dataset-67542-QCS-2024-03-19%2007.13.33.csv` |
| SVN | [SpatialQCs](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/CompetentAuthoritiesAndUnitsOfManagement/QC/dataset-67542-QCS-2024-03-19%2007.13.33.csv) |

```

For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


**LINK QCs**

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC**. Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered. 


#### QC Descriptive


```{table} Spatial QCs
:width: 100%

| Spatial QCs | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\QC - Floods RN3 – Descriptive.xlsx` |
| SVN | [SpatialQC](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/QC - Floods RN3 – Descriptive.xlsx) |
| Taskman | [265098](https://taskman.eionet.europa.eu/issues/265098) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented):


```{table} QCs exported from RN3
:width: 100%
| QC export from RN3 | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\CompetentAuthoritiesAndUnitsOfManagement\QC` |
| SVN | [SpatialQCs](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/CompetentAuthoritiesAndUnitsOfManagement/QC) |

```

For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


Also note we follow predefined number range to get them ordered by schema: 

**CA-UOM: 0001-0199** <br>
APSFR: 0200-0399  <br>
PFRA: 0400-0599  <br>
FRMP: 0600-0799  <br>
FHRM: 0800-0999  <br>
Document: 1000  <br>

  

LINK QCs 

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC.** Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered. 

### Codelist

- Make sure that the codelist have clear names. No need to use abreviations. Use UpperCamelCase for codelist tables/views. 
- Make sure that the codelist value have a clear notation. No need to use abreviations. Use lowerCamelCasefor codelist values. Try to avoid cryptic codes. 
- Always add a label (you'll likely need it later for data products). Use the definition to provide the thematic reporting guidance. 
- Don't duplicate codelists. 

All the codelist should have the following structure: 


CREATE TABLE [codelist].[TheNameOfTheCodelistInUpperCamelCase] <br>( <br>
[notation] [nvarchar] 100 NOT NULL,-- the code itself, using lowerCamelCase (if a standard code doesn't yet exist) <br>
[label] [nvarchar] 400 NULL,-- a more descriptive and human-readable label (that will likely appear in dashboards, etc.) <br>
[definition] [nvarchar]4000 NULL,-- a thematically informative definition to be provided by ENV/BHR <br>
[URI] [nvarchar] 500 NULL,-- a unique URI (for example, generic codes like 'other' have URI = http://dd.eionet.europa.eu/vocabulary/common/NilReasonType/other <br>
[remarks] [nvarchar] 4000 NULL,-- a remarks field that by default contains the datetime when the value was last set <br>
CONSTRAINT [PK_TheNameOfTheCodelistInUpperCamelCase] PRIMARY KEY CLUSTERED ([notation] ASC) WITH (PAD_INDEX = OFF,STATISTICS_NORECOMPUTE = OFF,IGNORE_DUP_KEY = OFF,ALLOW_ROW_LOCKS = ON,ALLOW_PAGE_LOCKS = ON,OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY] <br>)

 
If the values exist in the table [WISE].[mapping].[LOV] create a view: 

CREATE VIEW [codelist].[LanguageCode] AS 
SELECT [notation] 
      ,[label] 
      ,[definition] 
      ,[URI] 
      ,convert([nvarchar] 4000, getdate(), 25) as [remarks]  
FROM [WISE].[mapping].[LOV] 
  where tableName like 'iso639-2' 

**Descriptive Codelist definition**

```{table}
:width: 100%

| | |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Descriptive\Codelist` |
| SVN | [DescriptiveCodelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Descriptive/Codelist/) |
| Taskman | [264432](https://taskman.eionet.europa.eu/issues/264432) |
```

**Spatial Codelist definition**  
 
```{table}
:width: 100%

| | |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Spatial\Floods\Spatial_QuickReferenceCard.xlsx` |
| SVN | [FloodsSpatial_QuickReferenceCard](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Spatial/FloodsSpatial_QuickReferenceCard.xlsx) |
| Taskman | [264753](https://taskman.eionet.europa.eu/issues/264753) |
```

All the values in the spatial codelist for Floods:  

#### Codelist Descriptive 

**Codelist UoM Descriptive: only the values that are valid for UoM**

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Descriptive\Codelist` |
| SVN | [SpatialCodelist.xlsx](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Descriptive/Codelist/) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
```
The codelists were generated based on spatial wfd codelist and adapting the necessary elements.  
Not completly defined yet  

#### Codelist Spatial 

Codelist UoM Spatial : only the values that are valid for UoM 

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Developers\mmarcos\FLOODS_SVN\ReportNet3\Documents\Spatial\Codelist` |
| SVN | [SpatialCodelist.xlsx](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Spatial/FloodsSpatial_QuickReferenceCard.xlsx) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
```
The codelists were generated based on spatial wfd codelist and adapting the necessary elements.  
Not completly defined yet  


Reportnet 3 back-up: 
```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\CompetentAuthoritiesAndUnitsOfManagement\Codelist` |
| SVN | [SpatialCodelist.xlsx](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/Spatial/UoM/Codelist) |
```
### Testing files

#### Creation Descriptive Testing files 
To generate the SQLite database to test the Qc you need to generate an Enterprise Architect project and define all the tables and all the columns with the type as TEXT.  

If it is easier you can use an already create template as the base and modify it.  
When the tables are ready you need to click on Develop/Generate 

![FME Automation](img/CreationDescriptive.PNG) 

When the SQL is generate you need to modify it to remove all the clauses COLLATE NOCASE. You can use control+H in notepad++ and replace it with nothing. 

![FME Automation](img/FloodRiskTable.PNG) 


Then you need to add at the end of each table the STRICT mode: 


![FME Automation](img/FloodRiskStrict.PNG) 

Finally you need to run the prepared SQL in SQLite program, using a new database or modifying an existing one.  

 

Finally, this script will be use in the EXPORT of the schemas, to generate the template to be fullfiled with the reporters data. It needs to be stored in [https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data](https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data)

#### Creating geopackage 

1. How to Create a GeoPackage File for Templates and Testing in QGIS 

2. To create a GeoPackage file to be used as a template or for testing purposes, follow these steps: 

3. Open QGIS. It must be QGIS, as ArcGIS does not support the GeoPackage format. 

4. In the Browser panel, usually on the right side, right-click on GeoPackage and select Create Database.

![FME Automation](img/Geopackage.PNG) 

5. Choose a name and location for your GeoPackage file and click Save. 

6. After creating the database, right-click on it and select New Layer. 

7. Set the EPSG code, usually starting with 4326, and choose the geometry type. 

8. Enter a name for the layer. 

9. Define each field, specifying its type and length. The field length should match the limits allowed in the report. 

10. Most fields are set to text, except for those that contain integer numbers.
![FME Automation](img/GeopackageLayer.PNG) 
11. Do not manually create a geometry column. It is created automatically when you select the geometry type. 

    Once the GeoPackage template is created in EPSG:4326, you also need to generate the other two EPSG versions required for the EEA project: 3035 and 4258. 
To do this in QGIS: 
- a. Select the layer you want to reproject. 
- b. Use the Reproject Layer tool. 
- c. Set the Target CRS to either EPSG:3035 or EPSG:4258. 
- d. Choose the option Save as GeoPackage and save the reprojected layer accordingly. 
- e. Repeat the process for each required CRS. 

![FME Automation](img/CRS.PNG) 

#### Descriptive testing files 

*Different testing files were generated one to test errors and others with correct data to validate executions.*  

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\CA_UOM ` |
| SVN | [CA_UOM](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/CA_UOM) |
| Taskman | [Issue 265097](https://taskman.eionet.europa.eu/issues/265097) |
```
**UoM**

To test UoM descriptive dataset several sqlite files were generated: 

- A) Errors 

    - **Floods_CA_UOM.db3:** this file will force every QC to be executed for the reporting dataset. 

    - **Floods_CA_UOM_Documents.db3:** for testing the Documents dataset. 

    - **Floods_CA_UOM_Documents_reporting_no:** Documents dataset when no late reporting. 

    - **Floods_CA_UOM_Documents_reporting_yes:** Documents dataset when late reporting. 

 

- B) Correct executions 

    - **Floods_CA_UOM_wfds_wfdsNoNo.db3:** Validates tables CompetentAuthority and UnitOfManagement are filled. 

    - **Floods_CA_UOM_wfds_wfdsNoYes.db3:** Validates table UnitOfManagement is empty and CompetentAuthority is filled. 

    - **Floods_CA_UOM_wfds_wfdsYesNo.db3:** Validates table CompetentAuthority is empty and UnitOfManagement is filled. 

    - **Floods_CA_UOM_wfds_wfdsYesYes.db3:** Validates tables CompetentAuthority and UnitOfManagement are empty. 

 

Note: Some Link QCs might be raised since they require many other values from other tables to be included. I.e.: QCs that requires all euFloodsUnitOfManagementCode from Spatial dataset (thematicIdIdentifier) to be included.

#### Spatial testing files 

Two diferent testing files are generated one that make the error appear and the other with correct data.  

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Spatial\Test Files` |
| SVN | [Testing files](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/SPATIALUoM_test_file_DescriptivePart_Correct_incorrect.gpkg) |
| Taskman | [Issue 265215](https://taskman.eionet.europa.eu/issues/265215) |
```


**UoM**

To test UoM spatial dataset several geopackages were generated: 

- **SPATIALUoM_test_file_DescriptivePart_incorrect_v1.gpkg** file used to tets taht all the descriptive Qc regarding UoM spatial are being launch correctly when the error occurs.  

- **SPATIALUoM_test_file_DescriptivePart_correct_v1.gpkg** file used to test that the correct values do not produce any false blocker.  

- **SPATIALUoM_test_file_geometry_invalidsrid_v1.gpkg** file used to test if QC that control invalid srid works correctly.  

- **SPATIALUoM_test_file_ReferenceQC_v1.gpkg**

- **SPATIALUoM_test_file_geometry_invalidgeometry_v1.gpkg** file to validate the Spatial QC 

- **SPATIALUoM_test_file_COUNTRY_PL_correct_v1 Country test** 

### Database

**Introduction**  

All tables are referred to the exporting process from RN3 to SQL Server. 

**SQL SERVER**
Server name: WIGEON. 
Database: ????. 

**Tables**
???? 

## Areas of Potential Flood Risk & Preliminary Flood Risk Assessment 

Master Dataset Risk Zone Dataflow [https://reportnet.europa.eu/dataflow/1186](https://reportnet.europa.eu/dataflow/1186)

 

Testing Dataflow VIEWER: [https://reportnet.europa.eu/dataflow/1198](https://reportnet.europa.eu/dataflow/1198)

Testing dataflow ALL QC to be done:  [https://reportnet.europa.eu/dataflow/1213](https://reportnet.europa.eu/dataflow/1213)

Testing dataflow for reporting countries: [https://reportnet.europa.eu/dataflow/1262](https://reportnet.europa.eu/dataflow/1262)

 

 

Spatial comments: Since we first need to develop a dataset to report the data only for the viewer, there are two dataset in the dataflow RiskZoner Viewer & RiskZone.  

 

 

Spatial dataset RiskZone VIEWER: [https://reportnet.europa.eu/dataflow/1186/datasetSchema/68573](https://reportnet.europa.eu/dataflow/1186/datasetSchema/68573) 

Spatial dataset RiskZone_ [https://reportnet.europa.eu/dataflow/1186/datasetSchema/69069](https://reportnet.europa.eu/dataflow/1186/datasetSchema/69069)

### FME
#### Export – Documents dataset 

**FME name**
Export_Descriptive_Documents.fmw 


**Descriptive Summary** 

Generates a db3 SQLITE file with all the data included in the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of the mentioned dataset. It's shared for APSFR, PFRA, FHRM and FRMP. 

**Areas of impact in the dataflow**

If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: [https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data ](https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data)  

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw` |
| SVN | [Export_Descriptive_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw ) |
| FME Server | [RN3_BWD_WISE_Spatial_Import_CSV_Spatial_Reference_data](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Export_Descriptive_Documents.fmw) |
| FME Server database template  | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FTemplate_Database_Documents.sql) |
| Taskman | [271065](https://taskman.eionet.europa.eu/issues/271065) |
```


```{table} Access Management  
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- RN3 dataset database data.

**Output data**

- SQLite db3 file containing each different table existing in RN3. 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName | The name that the exported file will have.  | `For instance: test_2024` |
| SQLITE_TEMPLATE_CREATION_SCRIPT  | FME flow path where to get the database template from.   | $(FME_SHAREDRESOURCE_DATA)/Floods/Template_Database_Documents.sql |
```

#### Import – Descriptive data [PFRA] 

**FME name** 

Import_PFRA.fmw 

**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "DESCRIPTIVE REPORTING PFRA" dataset", located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow. 
The FME is called from the "External integrations" of the mentioned dataset. 

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_PFRA\Import_PFRA.fmw` |
| SVN | [Import_PFRA](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_PFRA/Import_PFRA.fmw) |
| FME Server | [FME](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_PFRA.fmw) |
| Taskman | [267897](https://taskman.eionet.europa.eu/issues/267897) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**

- SQLite database (.db3 files). 

**Output data**

Zip file containing different csv files for each different table we will fill in RN3. 

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [1052](https://reportnet.europa.eu/dataflow/1052 ) | 1052 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | 65926  in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | Fixed value | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `65926/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| InputFileName | Path where the SQLite input file (db3) is stored.   | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Floods_Documents.db3 ` |
```

#### Import – Documents dataset 

**FME name**

Import_Documents.fmw 


**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow.  

This FME is called from the "External integrations" of the mentioned dataset. It's shared for APSFR, PFRA, FHRM and FRMP. 


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Import_Documents.fmw` |
| SVN | [Import_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_DOCUMENTS/Import_Documents.fmw) |
| FME Server | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Import_Documents.fmw) |
| Taskman | [267897](https://taskman.eionet.europa.eu/issues/267897) |
```


```{table} Access Management  
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- SQLite database (.db3 files). 

**Output data**

- Zip file containing different csv files for each different table we will fill in RN3.  


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | id for the dataflow we can find within the url, e.g.:[1052](https://reportnet.europa.eu/dataflow/1052) | In the case of the example:1052 |
| DatasetId | id for the dataset we can find within the url, e.g.: [65926](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | In the case of the example: 65926|
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `65926/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputFileName | Path where the SQLite input file (db3) is stored.   | `\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Floods_Documents.db3` |
```


#### Import – Descriptive data [APSFR] 

**FME name**
Import_APSFR_descriptive_data.fmw 


**Areas of impact in the dataflow**
Imports the data from a db3 SQLITE file to the RN3 "DESCRIPTIVE REPORTING APSFR", located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow. 
The FME is called from the "External integrations" of the mentioned dataset. 

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_APSFR\Import_APSFR_descriptive_data.fmw` |
| SVN | [Import_APSFR](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_APSFR/Import_APSFR_descriptive_data.fmw) |
| FME Server | [FME](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_APSFR_descriptive_data.fmw) |
| Taskman | [267344](https://taskman.eionet.europa.eu/issues/267344) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**

- SQLite database (.db3 files). 

**Output data**
Zip file containing different csv files for each different table we will fill in RN3. 

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [1052](https://reportnet.europa.eu/dataflow/1052 ) | 1052 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | 65926  in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | Fixed value | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `65926/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| InputFileName | Path where the SQLite input file (db3) is stored.   | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Floods_Documents.db3 ` |
```
#### Import - Spatial data [HazardZone] 

**FME name:** Import_HazardZone_Spatial_data 

**Descriptive Summary**
This FME imports spatial data reported by the Member States to RN3. The FME currently supports Geopackages,  format.  

**Areas of impact in the dataflow**
The FME is called from the “External integrations” of the “Spatial data” dataset. 

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Spatial\IMPORT\IMPORT_HazardZone\Import_HazardZone_Spatial_data.fmw` |
| SVN | [Import_Hazard zone](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Spatial/IMPORT/IMPORT_HazardZone/Import_HazardZone_Spatial_data.fmw) |
| FME Server | [FME](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_HazardZone_Spatial_data.fmw) |
| Taskman | [269373](https://taskman.eionet.europa.eu/issues/269373) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**
Geopackage. 

**Output data**

The dataset of “Spatial data” will be filled in with the data reported in the uploaded files. 

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [https://sandbox.reportnet.europa.eu/dataflow/9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | The url where the input file (geopackage, shapefile or GML) is. If it is a shapefile, the input file must be a zip file. If it is a GML, the inputfile must be a GML or a zip file. If it is a geopackage, it must be the geopackage (uncompressed). | `\\Serval\s\Common workspace\Water\DataFlows\BWD_ReportNet3\FME\ExportFiles\testIru.gpkg` |
``` 

#### Import - Spatial data [RiskZone] 

**FME name:** Import_RiskZone_Spatial_data 

**Descriptive Summary**
This FME imports spatial data reported by the Member States to RN3. The FME currently supports Geopackages,  format.  

**Areas of impact in the dataflow**
The FME is called from the “External integrations” of the “Spatial data” dataset. 


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Spatial\IMPORT\IMPORT_RiskZone\Import_RiskZone_Spatial_data.fmw` |
| SVN | [Import_Risk zone](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Spatial/IMPORT/IMPORT_RiskZone/Import_RiskZone_Spatial_data.fmw ) |
| FME Server | [FME](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_RiskZone_Spatial_data.fmw ) |
| Taskman | [267061](https://taskman.eionet.europa.eu/issues/267061) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**
Geopackage. 

**Output data**
The dataset of “Spatial data” will be filled in with the data reported in the uploaded files. 
```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | The url where the input file (geopackage, shapefile or GML) is. If it is a shapefile, the input file must be a zip file. If it is a GML, the inputfile must be a GML or a zip file. If it is a geopackage, it must be the geopackage (uncompressed). | `\\Serval\s\Common workspace\Water\DataFlows\BWD_ReportNet3\FME\ExportFiles\testIru.gpkg` |
``` 

#### Prefill - Spatial reference data 


**FME name:** 

**Descriptive Summary**

**Areas of impact in the dataflow**

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Database\Spatial\Reference Data\APSFR\APSFR_Reference.sql` |
| SVN | [Iprefill_spatialdata](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Spatial/Reference%20Data/APSFR/APSFR_Reference.sql) |
| Taskman | [262825](https://taskman.eionet.europa.eu/issues/262825) |
```
**Input data**

**Output data**


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
``` 

#### Export - Spatial data [RiskZone] 

**FME name**
Export_RiskZone.fwe 

**Descriptive Summary**
Generates a geopackage with all the data included in the RiskZone dataset and you can download to your local computer.  

**Areas of impact in the dataflow** 

```{table} Related sources 
:width: 100%

| Type | Path |
|---|---|
| CWS | `ReportNet3\FME\Spatial\EXPORT\EXPORT_RiskZone` |
| SVN | [Export_spatialdata](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Spatial/EXPORT/EXPORT_RiskZone/Export_RiskZone.fmw ) |
| Taskman | [267061](https://taskman.eionet.europa.eu/issues/267061) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**

**Output data**

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| Exportfile | The name that the exported file will have.  | For instance: test_2024  |
| format | The file type we want to export.  | `'shp' or 'gpkg'` |
```
#### Export - Spatial data [HazardZone] 
**FME name :** Export_HazardZone.fmw

**Descriptive Summary**

Generates a geopackage with all the data included in the RiskZone dataset and you can download to your local computer.  

**Areas of impact in the dataflow** 

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `ReportNet3\FME\Spatial\EXPORT\EXPORT_HazardZone` |
| SVN | [Export_HazardZonedata](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Spatial/EXPORT/EXPORT_HazardZone/Export_HazardZone.fmw) |
| Taskman | [267061](https://taskman.eionet.europa.eu/issues/267061) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**

**Output data**

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| Exportfile | The name that the exported file will have.  | For instance: test_2024  |
| format | The file type we want to export.  | `'shp' or 'gpkg'` |
```

#### Export – Descriptive data [APSFR] 
**FME name** : Export_APSFR_Descriptive.fmw 

**Descriptive Summary**
Generates a db3 SQLITE file with all the data included in the RN3 "DESCRIPTIVE REPORTING APSFR" dataset, located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of mentioned dataset.  

**Areas of impact in the dataflow**
If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data  

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive/EXPORT_APSFR/Export_APSFR_Descriptive.fmw` |
| SVN | [Export_Descriptive_APSFRDocuments](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_APSFR/Export_APSFR_Descriptive.fmw) |
| FME Server | [Export_APSFR_Descriptive](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_APSFR_Descriptive.fmw) |
| FME Server database template  | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FAPSFR_Template_Database.sql) |
| Taskman | [271065](https://taskman.eionet.europa.eu/issues/271065) |
```


```{table} Access Management  
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- RN3 dataset database data. 

**Output data**

SQLite db3 file containing each different table existing in RN3.  


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName | The name that the exported file will have.  | `For instance: test_2024` |
| `SQLITE_TEMPLATE_CREATION_SCRIPT` | FME flow path where to get the database template from.   | `$(FME_SHAREDRESOURCE_DATA)/Floods/APSFR_Template_Database.sql` |
```

#### Export – Descriptive data [PFRA] 
**FME name:** Export_PFRA_Descriptive.fmw 

**Descriptive Summary**
Generates a db3 SQLITE file with all the data included in the RN3 "DESCRIPTIVE REPORTING PFRA" dataset, located in the "Floods Directive - Preliminary Flood Risk Assessment and Areas of Potential Significant Flood Risk" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of mentioned dataset. 

**Areas of impact in the dataflow**

If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data  


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive/EXPORT_PFRA/Export_PFRA_Descriptive.fmw` |
| SVN | [Export_Descriptive_PFRADocuments](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_PFRA/Export_PFRA_Descriptive.fmw) |
| FME Server | [Export_PFRA_Descriptive](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_PFRA_Descriptive.fmw) |
| FME Server database template  | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FPFRA_Template_Database.sql) |
| Taskman | [271065](https://taskman.eionet.europa.eu/issues/271065) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- RN3 dataset database data. 

**Output data**

SQLite db3 file containing each different table existing in RN3.  


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName | The name that the exported file will have.  | `For instance: test_2024` |
| `SQLITE_TEMPLATE_CREATION_SCRIPT` | FME flow path where to get the database template from.   | `$(FME_SHAREDRESOURCE_DATA)/Floods/PFRA_Template_Database.sql` |
```

#### Export – Harvesting process to EEA's SQL Server 

The export of data from RN3 to SQL Server is done through a generic harvesting process which is documented in the following link: 
From RN3 to SQL Server  [Web link](https://eea1.sharepoint.com/:o:/r/teams/cws/_layouts/15/Doc.aspx?sourcedoc=%7Bfd0a2b2b-369d-47f4-af64-e3cb637a972f%7D&action=edit&wd=target(Secci%C3%B3n%20sin%20t%C3%ADtulo.one%7C9ea7e169-f3f6-48d0-9ae2-8b667944bc38%2F)&wdorigin=717&wdpreservelink=1) 


Additionally, the database is called [Floods_Import] under [WIGEON] SQL Server. 

 

More information about the database can be found on the following page: 
Database  [Visit Web](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28DWD%20Reportnet3.one%7C6d0878a4-aa18-477f-9cf4-a50dab6f67c8%2FDatabase%7Cbe7d4c42-a3b6-47d1-98ec-6ee5027c489b%2F%29&wdorigin=NavigationUrl) 

**Automation at FME**

The harvesting process has been automated in FME Server through an "Automation" called **RN3_Floods_Harvesting**, you can find it in the following link: [https://fme.discomap.eea.europa.eu/fmeserver/#/automations](https://fme.discomap.eea.europa.eu/fmeserver/#/automations)


This FME Automation runs the generic harvesting process through a schedule every day and if an error has occurred sends a notification to wfd.helpdesk@eionet.europa.eu. 

![FME Automation](img/FME_Export_Harvest.PNG) 

### QC

#### QC Descriptive



```{table} Spatial QCs
:width: 100%

| Spatial QCs | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\QC - Floods RN3 – Descriptive.xlsx` |
| SVN | [Spatial QC](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/QC - Floods RN3 – Descriptive.xlsx) |
| Taskman | [267821](https://taskman.eionet.europa.eu/issues/267821) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented):


```{table} QCs exported from RN3
:width: 100%
| QC export from RN3 | Path |
|---|---|
| CWS | `S:\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\PFRA_APSFR_RiskZone_HazardZone` |
| SVN | [HazardZoneSpatialQCs](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/PFRA_APSFR_RiskZone_HazardZone) |

```

For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


Also note we follow predefined number range to get them ordered by schema: 

CA-UOM: 0001-0199<br>
**APSFR: 0200-0399**<br>
**PFRA: 0400-0599**<br>
FRMP: 0600-0799<br>
FHRM: 0800-0999<br> 
Document: 1000<br>

If, and only if, the number of QCs per qc type exceeds 200 then we will provide the following codes: 
**APSFR: 1200-1399** 
**PFRA: 1400-1599** 
  

LINK QCs 

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC.** Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered. 
#### QC Spatial

We have an Excel file where we have defined all the spatial QCs: 
```{table} Spatial QCs
:width: 100%

| Spatial QCs | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Developers\mmarcos\FLOODS_SVN\ReportNet3\QC\Spatial\/Floods_Spatial_QC-RiskZone_HazardZone_UoM.xlsx` |
| SVN | [Spatial QC](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Floods_Spatial_QC-RiskZone_HazardZone_UoM.xlsx) |
| Taskman | [267062](https://taskman.eionet.europa.eu/issues/) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented):


```{table} QCs exported from RN3
:width: 100%
| QC export from RN3 | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\PFRA_APSFR_RiskZone_HazardZone\RiskZone Viewer\dataset-68573-QCS.csv (VIEWER)` |
| SVN | [SpatialQCs](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/PFRA_APSFR_RiskZone_HazardZone/RiskZone%20Viewer/dataset-68573-QCS.csv (VIEWER)) |

```

For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


**LINK QCs**

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC**. Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered.

### Codelist
#### Codelist Descriptive 


```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Descriptive\Codelist` |
| SVN | [Floods_Descriptive_ModelAndCodelists_Definition](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Descriptive/Codelist/Floods_Descriptive_ModelAndCodelists_Definition.xlsx) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
``` 
 RN3 Back-up: 

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\PFRA_APSFR_RiskZone_HazardZone\codelist` |
| SVN | [RiskZone/codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/Spatial/RiskZone/codelist ) |
``` 

### Testing files
#### Spatial testing files

The files below are for the Qc implemented for the viewer. A full testing file can be found in the second table below.  
- Testing files for RiskMap Viewer dataset, 
 

```{table} 
:width: 100%

| Testing files | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Spatial\Test Files` |
| SVN | [Spatial_RiskZone_test](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/Floods_Spatial_RiskZone_test%20-%204326.gpkg)<br>[Spatial_RiskZone_test-4326_checkgeometries](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/Floods_Spatial_RiskZone_test%20-%204326_checkgeometries.gpkg)<br>[Spatial_RiskZone_test-incorrectsrid](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/Floods_Spatial_RiskZone_test%20-%20incorrectsrid.gpkg)<br> [Spatial_RiskZone_test-4326_country](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/Floods_Spatial_RiskZone_test%20-%204326_country.gpkg)|
| Taskman | [Issue 267063](https://taskman.eionet.europa.eu/issues/267063) |
```
- Testing files for RiskMap FULL list QC dataset,   


```{table} 
:width: 100%

| Testing files | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Spatial\Test Files\Floods_Spatial_RiskZone_test%20-%204326_FULL.gpkg` |
| SVN | [Floods_test](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Spatial/Test%20Files/Floods_Spatial_RiskZone_test%20-%204326_FULL.gpkg) |
| Taskman | [Issue 268180](https://taskman.eionet.europa.eu/issues/268180) |
```
#### Descriptive Testing files 

```{table} 
:width: 100%

| Testing files | Path |
|---|---|
| CWS | APSFR: `\\SERVAL\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\APSFR`<br>PFRA: `S:\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\PFRA`<br>APSFR-PFRA Documents dataset: `S:\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\APSFR-PFRA Documents` |
| SVN | [APSFR:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/APSFR/Floods_APSFR_Template.db3)<br>[PFRA:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/PFRA/Floods_PFRA.db3 )<br>[APSFR-PFRA Documents dataset:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/APSFR-PFRA%20Documents/Floods_APSFR_PFRA.db3)|
| Taskman | [APSFR](https://taskman.eionet.europa.eu/issues/267850)<br>[PFRA: ](https://taskman.eionet.europa.eu/issues/267899) |
```
### Database
#### RiskZone Reference table 
The script for generating the reference table of APSFR is in: 

```{table} 
:width: 100%

| Testing files | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Data\Reference Data\APSFR_reference_table\APSFR_Reference.sql` |
| SVN | [APSFR_Reference:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods Directive 2018/ReportNet3/Database/Spatial/Reference Data/APSFR/APSFR_Reference.sql)|
| Taskman | [Issue 262825](https://taskman.eionet.europa.eu/issues/262825) |
| Database: Floods2018  | reference.APSFR |
```

**Initial Considerations**

For the creation of the reference table, we have taken into account the analysis done for the APSFR in https://taskman.eionet.europa.eu/issues/258152:  
(More details are given in the view itself.) 

General issues: 

- There are some duplicated localId (There is a xquery that controls this but the FME wasn’t called from converters for some time and wrong things were accepted).This problem is happening for BG and IT (SI reported duplicated localIds but in the last envelope they corrected it.). 
- There are many thematicIds that don't match the regex. 
- If an element has been reported in spatial but not in descriptive or viceversa, the statusCode will be 'submitted' for that element. 

Country specific issues: 

- LU had reported twice the descriptive data and the old one need to be excluded since they reported at national level and then corrected in UnitOfManagement level. 
    https://cdr.eionet.europa.eu/lu/eu/floods2019/pfra_2019/descriptive/national/envxtscha 
- SI reported incorrect at UnitOfManagement level and then re-reported in national level corrected https://cdr.eionet.europa.eu/si/eu/floods2019/pfra_2019/spatial/sirbd2/envxtgziq/ 
    https://cdr.eionet.europa.eu/si/eu/floods2019/pfra_2019/spatial/sirbd1/envxtgzbg/ are also excluded. 

- ES030 comes from 2010 because the coordinate system they reported is wrong and the data from 2018 is imposible to display. 33 records. 
- FRD data comes from 2010 because the coordinate system they reported is wrong and the data from 2018 is imposible to display. 30 records. 
- LT doesn’t report in 2018. All the data comes from 2010. 129 records. 

Issues with Filenames in CDR 

Countries are reporting files named GML_PFRAPE… based on GML_APSFR.xsd, so we are inserting in APSFR table because the file is APSFR. It can lead to a misunderstanding. 
For instance, if you sum all the elements that PT sent only in files called APSFRwhatever, you can see that there are 142 APSFR. 

- APSFR_Lines_RH3.gml 6 
- APSFR_Points_RH3.gml 1 
- APSFR_Polygon_RH3.gml 3 
- APSFR_Lines_RH4A_Corrigido.gml 4 
- APSFR_Polygon_RH4A_Corrigido.gml 4 
- APSFR_Points_RH4A_Corrigido.gml 1 
- APSFR_Lines_RH5A_Corrigido.gml 8 
- APSFR_Points_RH5A_Corrigido.gml 3 
- APSFR_Polygon_RH5A_Corrigido.gml 4 
- APSFR_Polygon_RH1.gml 2 
- APSFR_Lines_RH1.gml 5 
- APSFR_Polygon_RH6.gml 3 
- APSFR_Polygon_RH2.gml 1 
- APSFR_Lines_RH2.gml 5 
- APSFR_Polygon_RH9.gml 15 
- APSFR_Polygon_RH8.gml 5 
- APSFR_Lines_RH8.gml 4 
- APSFR_Points_RH8.gml 3 
- APSFR_Points_RH7_Corrigido.gml 1 
- APSFR_Polygon.gml 35 
- APSFR_Line.gml 29 
- 142
        

However, if you go to the database, you will see that there are 156 because there are files named PFRAPE and are using the APSFR schema:

![FME Automation](img/APSFRSchema.PNG) 

We have removed all the elements reported in a file named PFRA even if the file has APSFR.xsd schema. 
 
**General description of Reference Table creation script**

Description of what we have done in the script with the data: 

<br>
**IT:**
- We retrieve descriptive data related to IT. 
     - For those reported in descriptive but not in spatial, we add the value 'submitted' to the statusCode field and '2018descriptive' to the metadata field. 
- We obtain their spatial data. 
    - For all those with repeated localId and thematicId combinations, we have aggregated geometry. 
    - Before aggregating the geometry, we need to perform a makeValid because UnionAggregate function won't work otherwise. 
    - If the element is a point type, we create a buffer. 
    - If the element is a line type, we create a buffer. 
    - If the element is a polygon type, we keep the geometry as it is. 
    - Thus, all elements with duplicate IDs will have polygon-type geometry because it has been aggregated. 
  - We add elements with the aggregated geometry to a temporary table. 
  - We retrieve elements without duplicate localId and thematicId and add them to the temporary table containing Italy's data. 
  - We check elements that do not match the data reported in descriptive and set statusCode ='submitted' and metadata ='2018spatial'. This way, we know which elements do not match and where they were reported, either in spatial or descriptive part.
   
<br>
**BG:**
- I retrieve their spatial data. 
    - Before aggregating  the geometry, we perform a makeValid because UnionAggregate function won't work otherwise. 
    - If the element is a point type, we create a buffer. 
    - If the element is a line type, we create a buffer. 
    - If the element is a polygon type, we keep the geometry as it is. 
- We retrieve elements without duplicate localId and add them to the temporary table containing Belgium's data. 
- I check that the data reported in descriptive matches spatial and vice versa. All match. 127 elements. 
**Floods2018:**
- I retrieve the spatial data of the rest of the countries with some exceptions: 
    - I remove ES30 because the geometry is incorrect, and we will take it from Floods 2010. 
    - I remove FRD because the geometry is incorrect, and we take it from Floods 2010. 
    - I remove IT and BG because the elements have been treated separately due to aggregating their geometry for repeated IDs. 
    - I remove from the query those elements from PFRA files with APSFR schema (6 files). 

The GMLs that were reported with APSFR schema but reported in PFRA files are the followings and have been excluded from the query: 

[https://cdr.eionet.europa.eu/pl/eu/floods2019/pfra_2019/spatial/pl7000/envx6pv7q/PFRAFutureEvents_Polygon_PL7000_20190618.gml](https://cdr.eionet.europa.eu/pl/eu/floods2019/pfra_2019/spatial/pl7000/envx6pv7q/PFRAFutureEvents_Polygon_PL7000_20190618.gml)<br>
[https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/ptrh8/envxjki7g/PFRAPastEvents_Point_RH8.gml](https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/ptrh8/envxjki7g/PFRAPastEvents_Point_RH8.gml)<br>
[https://cdr.eionet.europa.eu/es/eu/floods2019/pfra_2019/spatial/es014/envxo0k7q/GML_PFRAFutureEvents_Line_ES014_20190527.gml](https://cdr.eionet.europa.eu/es/eu/floods2019/pfra_2019/spatial/es014/envxo0k7q/GML_PFRAFutureEvents_Line_ES014_20190527.gml)<br>
[https://cdr.eionet.europa.eu/hr/eu/floods2019/pfra_2019/spatial/hrc/envxsxww/GML_PFRA_PastEvents_HR_HRC_Polygon_2019-07-23.gml](https://cdr.eionet.europa.eu/hr/eu/floods2019/pfra_2019/spatial/hrc/envxsxww/GML_PFRA_PastEvents_HR_HRC_Polygon_2019-07-23.gml)<br>
[https://cdr.eionet.europa.eu/es/eu/floods2019/pfra_2019/spatial/es014/envxo0k7q/GML_PFRAPastEvents_Line_ES014_20190527.gml](https://cdr.eionet.europa.eu/es/eu/floods2019/pfra_2019/spatial/es014/envxo0k7q/GML_PFRAPastEvents_Line_ES014_20190527.gml)<br>
[https://cdr.eionet.europa.eu/hr/eu/floods2019/pfra_2019/spatial/hrj/envxsxxcg/GML_PFRA_PastEvents_HR_HRJ_Polygon_2019-07-23.gml](https://cdr.eionet.europa.eu/hr/eu/floods2019/pfra_2019/spatial/hrj/envxsxxcg/GML_PFRA_PastEvents_HR_HRJ_Polygon_2019-07-23.gml)<br>

  - I check elements that do not match the data reported in descriptive and set statusCode ='submitted' and metadata ='2018spatial'. This way, we know which elements do not match and where they were reported, either in spatial or descriptive part. (1251 elements. But two of them are elements from FR that have been corrected to match because in the descriptive part, they use the character '´' and in spatial, they don't). 

  - I check that for elements reported in spatial but not in descriptive, there are no repeated IDs and all comply with the regex. Only PTRH10 element is repeated, so I have aggregated its geometry and in the field thematicIdIdentifier, I used the ID used in descriptive to refer to the element (PTRH10G26). 

  - I modify all thematicIdIdentifiers based on what was reported in the descriptive part. 
       - If the thematicId is equal to the apsfrCode, then I use the thematicId. 
       - If not, the thematicIdIdentifier is equal to the value of localId. 

  - Once done, I check if the new thematicId complies with the regex. 

       - If it does, I leave it as is. 
       - If not, I call a function that returns the corrected thematicIdIdentifier. 

 <br>    

**Floods 2010:**

- I retrieve spatial data, but only those that match descriptive. 
     - I exclude elements from FR that use the character '´' and also exclude IT and BG.  'FRG_TRI_BAIE_DE_L'AIGUILLON' & 'FRG_TRI_ST_NAZAIRE_PRESQU'ILE_DE_GUERANDE'  
- From those elements, I only keep those not reported in Floods2018. 
- I check that there are no repeated localIds: None found. 
- I check if they comply with the regex: 8 elements don't comply, so I corrected them. 
<br>


**DE:**

- I retrieve spatial data of DE based on the data obtained in the Floods2018 temporary table. 
- I perform makeValid before aggregating geometries. 
- I aggregate geometry for all those with repeated thematicIds. 
     - If the element is a point type, we create a buffer. 
     - If the element is a line type, we create a buffer. 
     - If the element is a polygon type, we keep the geometry as it is. 
- I add to the DE data temporary table, elements that do not have the identifier repeated and the aggregated ones. 
- I delete from the Floods2018  temporary table everything related to DE and add what I just calculated. 


**Elements reported in descriptive but not in spatial:**

- I retrieve elements not reported in spatial (224 elements). I exclude the two from FR that use the character '´'. 
- Some PT elements, I match manually based on localId, namespace, nameOfAPSFR... 
     - For these elements, for the field thematicIdIdentifier, I use the value of the identifier used in the descriptive part. 
- The elements not matching from AT are because in the last envelope we manually harvested, they were not sent. But in the previously reported and accepted envelope, they were there. Since we only kept the last accepted envelope, those elements have been lost. 
- The one not matching from ES is because they reported two identifiers in the same record separated by a space. Separately, these two elements exist in spatial, so I delete the record from the reference table where they use two ids in the descriptive part. 
- After deleting this, only 223 elements remain. 
- The element not matching from SE is suspected to be equivalent to one in spatial, but since we are not sure, we leave it as is. 
- Out of 223 elements, 32 do not comply with the regex. Corrections have been made. 


**General observations:**

- There are 3 PT spatial files that have not been included in APSFR because they follow the PFRA schema. 

    - [https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Lines_PTcont_Corrigido.gml](https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Lines_PTcont_Corrigido.gml)

    - [https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Points_PTcont_Corrigido.gml](https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Points_PTcont_Corrigido.gml)

    - [https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Polygon_PTcont_Corrigido.gml](https://cdr.eionet.europa.eu/pt/eu/floods2019/pfra_2019/spatial/national/envx_kgma/APSFR_Polygon_PTcont_Corrigido.gml)

- There were 3 EE records that complied with the regex but did not start with the countryCode. So I checked that all elements start with their countryCode. Only 3 records were affected from Estonia. 

    - EEAPSFR109 

    - EEAPSFR103 

    - EEAPSFR102 

- For the elements that don't have beginLifeSpanVersion, we have decided: 
      - If the data is from 2010, we put to all those elements 2010-01-01. 
      - If the data is from 2018, the one reported in descriptive but not in spatial, we put 2018-01-01. 
      - The rest of the elements have the previously reported beginLifeSpanVersion. 

After the creation of the table, I have added some fields that were missing and I rename metadata field by statusRemarks. 

#### RelatedZones reference table 

The reference table used in this dataflow for the related zones in spatial and also the euFloodsUnitOfManagementCode field in descriptive is built based on data reported to WFD2022 and Floods2018 


```{table} 
:width: 100%

| SQL files | Path |
|---|---|
| CWS | `\\Serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Database\Spatial\Reference Data\UOM` |
| SVN | [FloodsUOM_or_WFDRBD](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Spatial/Reference%20Data/UOM/reference.FloodsUOM_or_WFDRBD.sql)<br>[FloodsUOM_and_WFDRBD](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Spatial/Reference%20Data/UOM/reference.FloodsUOM_and_WFDRBD.sql)|
| Taskman | [Issue 265217](https://taskman.eionet.europa.eu/issues/265217) |
| Database: Floods_Production | [reference].[FloodsUoMReference] - Just gets the UOM data from 2018 Floods reporting
[reference].[FloodsUOM_or_WFDRBD] - Gets UOM info from Floods2018. For the rest of countries, gets the RBD from WFD2022
[reference].[FloodsUOM_and_WFDRBD] - Gets both UOM from Floods2018 and RBDs from WFD2022 |
```

#### Codelist Spatial 

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Spatial\Codelist` |
| SVN | [Codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Spatial/Codelist/FloodsSpatial_Codelist.xlsx) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
```
RN3 Back-up: 


 ```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval.eea.dmz1\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\PFRA_APSFR_RiskZone_HazardZone\codelist` |
| SVN | [Codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/Spatial/RiskZone/codelist) |
```
## Flood Hazard and Risk Maps 

**Master dataflow:** [https://reportnet.europa.eu/dataflow/1252](https://reportnet.europa.eu/dataflow/1252) 
**Reporting dataflow:** [https://reportnet.europa.eu/dataflow/1587](https://reportnet.europa.eu/dataflow/1587)

Access to the dataflow is granted only to countries whose UoM and APSFR & PFRA have been technically accepted. 


### FME
#### Export – Documents dataset 

**FME name**

Export_Descriptive_Documents.fmw 

**Descriptive Summary**

Generates a db3 SQLITE file with all the data included in the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Floods Hazard and Risk Maps" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of the mentioned dataflow. It's shared for APSFR, PFRA, FHRM and FRMP. 

**Areas of impact in the dataflow**

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw` |
| SVN | [Export_Descriptive_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw) |
| FME Server | [Export_APSFR_Descriptive](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Export_Descriptive_Documents.fmw) |
| FME Server database template  | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FTemplate_Database_Documents.sql) |
| Taskman | [271065](https://taskman.eionet.europa.eu/issues/271065) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- RN3 dataset database data. 

**Output data**

SQLite db3 file containing each different table existing in RN3.  


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName | The name that the exported file will have.  | `For instance: test_2024` |
| `SQLITE_TEMPLATE_CREATION_SCRIPT`  | FME flow path where to get the database template from.   | `$(FME_SHAREDRESOURCE_DATA)/Floods/Template_Database_Documents.sql` |
```
#### Import – Documents dataset 

**FME name**
Import_Documents.fmw 

**Areas of impact in the dataflow**
Imports the data from a db3 SQLITE file to the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Floods Hazard and Risk Maps" dataflow.  
This FME is called from the "External integrations" of the mentioned dataset. It's shared for APSFR, PFRA, FHRM and FRMP. 


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Import_Documents.fmw` |
| SVN | [Export_Descriptive_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_DOCUMENTS/Import_Documents.fmw) |
| FME Server | [Import documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Import_Documents.fmw) |
| Taskman | [267897](https://taskman.eionet.europa.eu/issues/267897) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- SQLite database (.db3 files). 

**Output data**

Zip file containing different csv files for each different table we will fill in RN3. 

```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | Path where the SQLite input file (db3) is stored. | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Floods_Documents.db3` |
```

#### Import – Descriptive data 
**FME name**

Import_FHRM.fmw 
**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "REPORTING Floods Hazard and Risk Maps" dataset, located in the "Floods Directive - Floods Hazard and Risk Maps" dataflow. 

The FME is called from the "External integrations" of the mentioned dataset. 


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_FHRM\Import_FHRM.fmw` |
| SVN | [Import FHRM](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_FHRM/Import_FHRM.fmw) |
| FME Server | [Import documents](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_FHRM.fmw) |
| Taskman | [271299](https://taskman.eionet.europa.eu/issues/271299) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- SQLite database (.db3 files). 

**Output data**

Zip file containing different csv files for each different table we will fill in RN3. 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | Path where the SQLite input file (db3) is stored. | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_FHRM\Floods_FHRM.db3` |
```


#### Export – Descriptive data 


**FME name**

Export_FHRM_Descriptive.fmw 


**Areas of impact in the dataflow**

Generates a db3 SQLITE file with all the data included in the "REPORTING Floods Hazard and Risk Maps" dataset, located in the "Floods Directive - Floods Hazard and Risk Maps" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of the mentioned dataset. 
If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data  



```{table} Related resources 
:width: 100%

| Type | Path |
|---|---|
| CWS | \\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\EXPORT_FHRM\Export_FHRM_Descriptive.fmw |
| SVN |
[Export_FHRM_descriptive_data](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_FHRM/Export_FHRM_Descriptive.fmw) |
| FME Server | Reporting dataset: [Export_CA_UOM_descriptive_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_FHRM_Descriptive.fmw)  |
| FME Server database template |  [FFHRM](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FFHRM_Template_Database.sql)  |
| Taskman | [issues/271302](https://taskman.eionet.europa.eu/issues/271302) |
```

```{table} Access Management  
:width: 100%

| Place | User | Permissions |
|---|---|---|
| | FME_Authors | Full access |
| | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```


**Input data**
RN3 dataset database data. 

 

**Output data**
SQLite db3 file containing each different table existing in RN3. 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| countryCode | If a country code is passed as a parameter, the FME will act as a prefill of protected areas for the specific country | ES |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName  | The name that the exported file will have. | For instance:test_2024  |
| `SQLITE_TEMPLATE_CREATION_SCRIPT`  | FME flow path where to get the database template from.  | `$(FME_SHAREDRESOURCE_DATA)/Floods/FHRM_Template_Database.sql` |

```

### QC


```{table} 
:width: 100%

| Spatial QCs  | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\QC - Floods RN3 – Descriptive.xlsx` |
| SVN | [Floods RN3 – Descriptive](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/QC - Floods RN3 – Descriptive.xlsx) |
| Taskman | [271300](https://taskman.eionet.europa.eu/issues/271300) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented): 


```{table} 
:width: 100%

| QC export from RN3  | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\FloodsHazardAndRiskMaps` |
| SVN | [Floods RN3 – Descriptive](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/FloodsHazardAndRiskMaps) |
```


For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


Also note we follow predefined number range to get them ordered by schema: 

CA-UOM: 0001-0199<br>
APSFR: 0200-0399<br>
PFRA: 0400-0599<br>
FRMP: 0600-0799<br>
**FHRM: 0800-0999**<br>
Document: 1000<br> 

If, and only if, the number of QCs per qc type exceeds 200 then we will provide the following codes: 

**FHRM: 1800-1999**

LINK QCs 

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC.** Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered. 

### Codelist

```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Descriptive\Codelist ` |
| SVN | [Codelist_definitions](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Descriptive/Codelist/Floods_Descriptive_ModelAndCodelists_Definition.xlsx ) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
```
RN3 Back-up: 


 ```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\FloodsHazardAndRiskMaps\CODELIST.zip` |
| SVN | [Codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/FloodsHazardAndRiskMaps/CODELIST.zip) |
```
### Testing files 


 ```{table} 
:width: 100%

| Testing files  | Path |
|---|---|
| CWS | Reporting dataset:`\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\FHRM\Floods_FHRM.db3`<br>Documents dataset:`\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\FHRM\Floods_FHRM_Documents.db3` |
| SVN | [Descriptive dataset:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/FHRM/Floods_FHRM.db3)<br>[Documents dataset:](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/FHRM/Floods_FHRM_Documents.db3) |
| Taskman | [Issue 271301](https://taskman.eionet.europa.eu/issues/271301) |
```
### Database

**Introduction** 
All tables are referred to the exporting process from RN3 to SQL Server. 

**SQL SERVER**

Server name: WIGEON. 
Database: ????. 

**Tables** 

???? 

**Introduction**
SQL tables for code list: 

All SQL tables under [codelist] SQL Schema. 
Necessary SQL Table for generic harvesting process: 

[metadata].[HarvestingJobs] 

#### ProtectedArea Reference data 

The reference table used in this dataflow  for the protected areas is based on a view in the database. 

```{table} 
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Database\Descriptive\Reference Data` |
| SVN |[Export_FHRM_descriptive_data](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Descriptive/Reference%20Data/reference.v_ProtectedArea.sql) |
| Taskman | [issues/271333](https://taskman.eionet.europa.eu/issues/271333) |
| Database: Floods_Production  | [reference].[v_ProtectedArea] - Gets the list of latest WFD ProtectedAreas from WISE_Spatial database  |
```

## Flood Risks Management Plans 

**Development dataflow:** https://reportnet.europa.eu/dataflow/1243  
**Testing dataflow for reporting countries:** https://reportnet.europa.eu/dataflow/1261 
**Reporting dataflow:** https://reportnet.europa.eu/dataflow/1909  

### FME
Each FME involved will have a subpage with the description.

#### Export – Documents dataset 

**FME name**
Export_Descriptive_Documents.fmw 

**Descriptive Summary**

Generates a db3 SQLITE file with all the data included in the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Floods Risk Management Plans" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of the mentioned dataset. It's shared for APSFR, PFRA, FHRM and FRMP. 

**Areas of impact in the dataflow**


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw` |
| SVN | [Export_Descriptive_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_DOCUMENTS/Export_Descriptive_Documents.fmw) |
| FME Server | [RN3_BWD_WISE_Spatial_Import_CSV_Spatial_Reference_data](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Export_Descriptive_Documents.fmw) |
| FME Server database template  | [Database documents](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FTemplate_Database_Documents.sql) |
| Taskman | [271065](https://taskman.eionet.europa.eu/issues/271065) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**

- RN3 dataset database data.  

**Output data**

SQLite db3 file containing each different table existing in RN3. 




```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | 9413 in the case of the example |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | 22930 in the case of the example |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| exportFileName | The name that the exported file will have.  | `For instance: test_2024` |
| SQLITE_TEMPLATE_CREATION_SCRIPT  | FME flow path where to get the database template from.   | $(FME_SHAREDRESOURCE_DATA)/Floods/Template_Database_Documents.sql |
```
#### Import – Documents dataset 

**FME name**
Import_Documents.fmw 

**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "DOCUMENTS" dataset, located in the "Floods Directive - Floods Risk Management Plans" dataflow.  
This FME is called from the "External integrations" of the "Documents" dataset. It's shared for APSFR, PFRA, FHRM and FRMP. 

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Import_Documents.fmw` |
| SVN | [Export_Descriptive_Documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_DOCUMENTS/Import_Documents.fmw) |
| FME Server | [RN3_BWD_WISE_Spatial_Import_CSV_Spatial_Reference_data](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Import_Documents.fmw) |
| Taskman | [267897](https://taskman.eionet.europa.eu/issues/267897) |
```


```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```
**Input data**
SQLite database (.db3 files). 

**Output data**
Zip file containing different csv files for each different table we will fill in RN3.


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [9413](https://sandbox.reportnet.europa.eu/dataflow/9413) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://sandbox.reportnet.europa.eu/dataflow/9413/datasetSchema/22930?tab=6593e7c260d48300011d9492&view=design) | [1052](https://reportnet.europa.eu/dataflow/1052) |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | Path where the SQLite input file (db3) is stored. | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_DOCUMENTS\Floods_Documents.db3` |
```
#### Import – Descriptive data 

**FME name** 
Import_FRMP 

**Areas of impact in the dataflow**

Imports the data from a db3 SQLITE file to the RN3 "REPORTING Floods Hazard and Risk Maps" dataset, located in the "Floods Directive - Floods Risk Management Plans" dataflow. 
The FME is called from the "External integrations" of the mentioned dataset.

```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_FRMP\Import_FRMP\Import_FRMP.fmw` |
| SVN | [Import_FRMP](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/IMPORT_FRMP/Import_FRMP.fmw) |
| FME Server | [Import_FRMP](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_FRMP.fmw) |
| Taskman | [270204](https://taskman.eionet.europa.eu/issues/270204) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**
SQLite database (.db3 files). 

**Output data** 
Zip file containing different csv files for each different table we will fill in RN3. 



```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId | We need to insert the id of the dataflow that we can find on the url. For instance [1234](https://sandbox.reportnet.europa.eu/dataflow/1243) | [1243] |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [Sandbox](https://reportnet.europa.eu/dataflow/1243/datasetSchema/71135) | In the case of the example:71135  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| providerId | Fixed value | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| inputfile | Path where the SQLite input file (db3) is stored. | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\IMPORT_FRMP\Floods_FRMP.db3` |
```
```{table} Web connections
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| Connection Name  | Name to identify the connection  | FME Server ReportNet3  |
| Server URL   | Server where we're connecting to   | https://fme.discomap.eea.europa.eu   |
| Authentication   | Authentication type   | Basic |
| User Name  | Credential   | Example: mosquera |
| Password  | User's password for this server    | [password] |
| Verify SSL Certificates | Checked for verifying certificate  | Unchecked |
```

#### Export – Descriptive data 
**FME name**
Export_FRMP_Descriptive.fmw 

**Areas of impact in the dataflow**

Generates a db3 SQLITE file with all the data included in the RN3 "REPORTING Floods Risk Management Plans" dataset, located in the "Floods Directive - Floods Risk Management Plans" dataflow, that you can download to your local computer. 
This FME is called from the "External integrations" of the mentioned dataset.

If the data model is changed and the SQL template needs to be modified or recreate, the SQL needs to be changed in SVN and FME SERVER: https://fme.discomap.eea.europa.eu/fmeserver/resources/browse?path=FME_SHAREDRESOURCE_DATA%2FFloods&name=Data  


```{table} Related sources
:width: 100%

| Type | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\FME\Descriptive\EXPORT_FRMP\Export_FRMP_Descriptive.fmw` |
| SVN | [Export_FRMP_Descriptive](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/FME/Descriptive/EXPORT_FRMP/Export_FRMP_Descriptive.fmw) |
| FME Server | [Export_FRMP_Descriptive](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Export_FRMP_Descriptive.fmw) |
| FME Server | [FFRMP_Template_Database](https://fme.discomap.eea.europa.eu/fmeserver/resources/view?file=FME_SHAREDRESOURCE_DATA%2FFloods%2FFRMP_Template_Database.sql) |
| Taskman | [271067](https://taskman.eionet.europa.eu/issues/271067) |
```

```{table} Access Management 
:width: 100%

| Place | User | Permissions |
|---|---|---|
|  | FME_Authors | Full access |
|  | FME_Administrators | Full access |
|  | Reportnet3 | Full access |
```

**Input data**
RN3 dataset database data. 

**Output data** 
Zip file containing different csv files for each different table we will fill in RN3. 


```{table} Parameters
:width: 100%

| Name | Description | Possible values |
|---|---|---|
| dataflowId |id for the dataflow we can find within the url, e.g.: [1052](https://reportnet.europa.eu/dataflow/1052) | [1052]In the case of the example: |
| DatasetId | We need to insert the id of the dataset that we can find on the url. For instance [65926](https://reportnet.europa.eu/dataflow/1052/datasetSchema/65926) | In the case of the example:65926  |
| baseUrl | The url of the api of reportnet3. It is different if we work in production or sandbox. | Production: [api](https://api.reportnet.europa.eu) <br/> Sandbox: [sandbox-api](https://sandbox-api.reportnet.europa.eu/) |
| countryCode | If a country code is passed as a parameter, the FME will act as a prefill of protected areas for the specific country | ES |
| providerId | | `design` |
| folder | It must be composed by datasetID + / + providerid | In the case of the previous example: `22930/design` |
| apiKey | It must be composed by `ApiKey` + apikey number. The apikey number can be obtained from reportnet3 in the dataflow. ![API key location](img/Api.PNG) | `ApiKey cdc6e04d-565c-4c88-b21b-939008d8b8cb` |
| InputFileName  | Path where the SQLite input file (db3) is stored. | For instance:test_2024  |
| SQLITE_TEMPLATE_CREATION_SCRIPT  | FME flow path where to get the database template from.  | $(FME_SHAREDRESOURCE_DATA)/Floods/FRMP_Template_Database.sql |

```

#### Export – Harvesting process 

The export of data from RN3 to SQL Server is done through a generic harvesting process which is documented in the following link: 
[From RN3 to SQL Server]
(https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={fd0a2b2b-369d-47f4-af64-e3cb637a972f}&action=edit&wd=target%28From%20RN3%20to%20SQL%20Server.one%7Ce12603f6-7721-4d46-8859-6a3e39cffb50%2FIntroduction%7Cdda065eb-8020-4ebe-8bbc-bb6019f3fca3%2F%29&wdorigin=NavigationUrl)

Additionally, the database is called [BWD_Import] under [WIGEON] SQL Server. 
More information about the database can be found on the following page: 
[Database]
(https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28DWD%20Reportnet3.one%7C6d0878a4-aa18-477f-9cf4-a50dab6f67c8%2FDatabase%7Cbe7d4c42-a3b6-47d1-98ec-6ee5027c489b%2F%29&wdorigin=NavigationUrl)

**Automation at FME**

The harvesting process has been automated in FME Server through an "Automation" called RN3_BWD_Harvesting, you can find it in the following link:
https://fme.discomap.eea.europa.eu/fmeserver/#/automations  

This FME Automation runs the generic harvesting process through a schedule every day and if an error has occurred sends a notification to wfd.helpdesk@eionet.europa.eu. 

![FME Automation](img/FME_Export_Harvest.PNG)

### QC

```{table}
:width: 100%

| Spatial QCs | Path |
|---|---|
| CWS | `\\Serval\s\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\QC - Floods RN3 – Descriptive.xlsx` |
| SVN | [Spatial QC](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/QC - Floods RN3 – Descriptive.xlsx) |
| Taskman | [270205](https://taskman.eionet.europa.eu/issues/270205) |
```

The Excel file with the QCs exported from RN3 (The ones already implemented):


```{table} QCs exported from RN3
:width: 100%
| QC export from RN3 | Path |
|---|---|
| CWS | `S:\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\FloodRiskManagementPlans` |
| SVN | [HazardZoneSpatialQCs](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/FloodRiskManagementPlans) |

```

For the nomenclature of the QC codes, we have use the one described here:

[QC code nomenclature](https://eea1.sharepoint.com/teams/cws/_layouts/15/Doc.aspx?sourcedoc={a045c367-ebe9-40d7-8b70-d158ae78821a}&action=edit&wd=target%28QC%20code%20nomenclature.one%7C908816d3-0363-486b-bffe-a66783407b1a%2F%29&wdorigin=717&wdpreservelink=1)
*link missing here*


Also note we follow predefined number range to get them ordered by schema: 

CA-UOM: 0001-0199<br>
APSFR: 0200-0399  <br>
PFRA: 0400-0599  <br>
**FRMP: 0600-0799**<br>
FHRM: 0800-0999  <br>
Document: 1000 <br> 
If, and only if, the number of QCs per qc type exceeds 200 then we will provide the following codes: 

FRMP: 1600-1799
  

LINK QCs 

In many instances, a field is considered correct only if its value belongs to a predefined list of values. This list of values is stored in a codelist; however, not all values added to the codelist are necessarily accepted for the field in question. For example, the thematicIdIdentifierScheme may take on values such as 'euProtectedAreaCode' and 'eionetProtectedAreaCode,' but the 'IdentifierScheme' codelist offers a broader range of options as other fields also read from the same codelist. For instance, the relatedZoneIdentifier may have values like 'eionetGroundWaterBodyCode,' 'euGroundWaterBodyCode,' 'eionetSurfaceWaterBodyCode,' and 'eionetSurfaceWaterBodyCode'. All these values are stored in the same codelist. 

Therefore, **if a field is restricted to specific values from a codelist, it will have a specific QC.** Additionally, the field will be designated as a link in the design section, but automatic QC will remain disabled. This approach allows reporters to manually input values in RN3, providing a dropdown menu with codelist values for a more intuitive user experience. If an incorrect codelist value is entered, a BLOCKER will be triggered. 

### Codelist


```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Documents\Descriptive\Codelist` |
| SVN | [Codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Documents/Descriptive/Codelist/Floods_Descriptive_ModelAndCodelists_Definition.xlsx) |
| Taskman | [Issue 264432](https://taskman.eionet.europa.eu/issues/264432) |
```
RN3 Back-up: 


 ```{table} 
:width: 100%

| Codelist | Path |
|---|---|
| CWS | `\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Dataflow Backup\FloodRiskManagementPlans\CODELIST.zip` |
| SVN | [Codelist](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Dataflow%20Backup/FloodRiskManagementPlans/CODELIST.zip) |
```
### Testing files




```{table} 
:width: 100%

| Testing files | Path |
|---|---|
| CWS | Reporting dataset:`\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\FRMP\Floods_FRMP.db3`<br>Documents dataset:`\\serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\QC\Descriptive\Test Files\FRMP\Floods_FRMP_Documents.db3`  |
| SVN | Reporting dataset:[Floods_FRMP](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/FRMP/Floods_FRMP.db3)<br>Documents dataset: [FRMP documents](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/QC/Descriptive/Test%20Files/FRMP/Floods_FRMP_Documents.db3)  |
| FME Server | Reporting dataset: [Import_CA_UOM_descriptive_data](https://fme.discomap.eea.europa.eu/fmeserver/#/workspaces/run/Floods%20RN3/Import_CA_UOM_descriptive_data.fmw)<br>Documents dataset:
[Import_CA_UOM_descriptive_data_Documents](https://fme.discomap.eea.europa.eu/fmeserver/workspaces/run/Floods%20RN3/Import_CA_UOM_descriptive_data_Documents.fmw)  |
| Taskman | [issues/270206](https://taskman.eionet.europa.eu/issues/270206) |
```

### Database
#### WFD Measure Codes Reference data 

The reference table used in this dataflow for the list of WFD Measure codes used as reference for the wfdMeasure field 
```{table}
:width: 100%

| SQL files | Path |
|---|---|
| CWS | `\\Serval\S\Common workspace\Water\DataFlows\Floods Directive\Floods Directive 2018\ReportNet3\Database\Descriptive\Reference Data` |
| SVN | [WFDMeasuresCode](https://svn.eionet.europa.eu/repositories/Reportnet/Dataflows/FloodsDirective/Floods%20Directive%202018/ReportNet3/Database/Descriptive/Reference%20Data/reference.v_WFDMeasureCodes.sql) |
| Taskman | [271332](https://taskman.eionet.europa.eu/issues/271332) |
| Database: Floods_Production | [reference].[v_WFDMeasureCodes] - Gets the list of latest WFD Measure codes (2016 or 2022) from WISE_SOW database |
```
## Nery's scrapbook 

**Article 3 - Units of Management and Competent Authorities** 
- By default, MS use the WFD units of management and competent authorities (Article 3.1) 
- Only if they do differently (Article 3.2) must they report the UOM and CA. 
- So, the modelling option is 100% correct. 
**Chapter II - Preliminary Flood Risk Assessment**

Article 4 seems to be where the past floods come from…  but what is the difference between 4.2.b and 4.2.c? I see no difference.

*Article 4.2 […]The assessment shall include at least the following: […]*

*(b) a description of the floods which have occurred in the past and which had significant adverse impacts on human health, the environment, cultural heritage and economic activity and for which the likelihood of similar future events is still relevant, including their flood extent and conveyance routes and an assessment of the adverse impacts they have entailed;*  

*(c) a description of the significant floods which have occurred in the past, where significant adverse consequences of similar future events might be envisaged;* 

*and, depending on the specific needs of Member States, it shall include:*

*(d) an assessment of the potential adverse consequences of future floods for human health, the environment, cultural heritage and economic activity*

Article 5 seem to be where the Areas of Potential Significant Flood Risk come from. 
But there's no description of the content. One would assume 4.2.d would be a part of it. 

*Article 5 1. On the basis of a preliminary flood risk assessment as referred to in Article 4, Member States shall, for each river basin district, or unit of management referred to in Article 3(2)(b), or portion of an international river basin district lying within their territory, identify those areas for which they conclude that potential significant flood risks exist or might be considered likely to occur.*

**Very important: The PFRA and APSFR can be completely bypassed if:**
CHAPTER VII TRANSITIONAL MEASURES Article 13 

*1. Member States may decide not to undertake the preliminary flood risk assessment referred to in Article 4 for those river basins, sub-basins or coastal areas where they have either: (a) already undertaken a risk assessment to conclude, before 22 December 2010, that a potential significant flood risk exists or might be considered likely to occur leading to the identification of the area among those referred to in Article 5(1) or (b) decided, before 22 December 2010, to prepare flood hazard maps and flood risk maps and to establish flood risk management plans in accordance with the relevant provisions of this Directive. 2. Member States may decide to make use of flood hazard maps and flood risk maps finalised before 22 December 2010, if such maps provide a level of information equivalent to the requirements of Article 6. 3. Member States may decide to make use of flood risk management plans finalised before 22 December 2010, provided the content of these plans is equivalent to the requirements set out in Article 7. 4. Paragraphs 1, 2 and 3 shall apply without prejudice to Article 14.* 

**Chapter III - FLOOD HAZARD MAPS AND FLOOD RISK MAPS**

*Article 6*

*1. Member States shall, at the level of the river basin district, or unit of management referred to in Article 3(2)(b), prepare flood hazard maps and flood risk maps, at the most appropriate scale for the areas identified under Article 5(1).* 

*3. Flood hazard maps*
(a) floods with a low probability, or extreme event scenarios;  
(b) floods with a medium probability (likely return period ≥ 100 years);  
(c) floods with a high probability, where appropriate.*

*4. For each scenario referred to in paragraph 3 the following elements shall be shown:*  
(a) the flood extent;  
(b) water depths or water level, as appropriate;  
(c) where appropriate, the flow velocity or the relevant water flow. 

*5. Flood risk maps shall show the potential adverse consequences associated with flood scenarios referred to in paragraph 3 and expressed in terms of the following: * 

(a) the indicative number of inhabitants potentially affected;  
(b) type of economic activity of the area potentially affected;  
(c) installations as referred to in Annex I to Council Directive 96/61/EC of 24 September 1996 concerning integrated pollution prevention and control which might cause accidental pollution in case of flooding and potentially affected protected areas identified in Annex IV(1)(i), (iii) and (v) to Directive 2000/60/EC;  
(d) other information which the Member State considers useful such as the indication of areas where floods with a high content of transported sediments and debris floods can occur and information on other significant sources of pollution.  

So, the way I read it, and looking for minimum requirements. 
    - One "hazard map" and one "risk map" per UOM. 
    - Times three scenarios. 
    - For each scenario and UOM, description of adverse consequences for inhabitants, economic activity, SEVESO installations, and  protected areas. 
    - For coastal areas, and flooding from groundwater sources - only extreme events 

**Now looking at the existing models… **
Past events & Future events  

https://cdr.eionet.europa.eu/help/Floods/Floods_2018/UML/PFRA_FutureEvents.png 
https://cdr.eionet.europa.eu/help/Floods/Floods_2018/UML/PreliminaryFloodsRiskAssessmentsPastEvents.png 

It follow the HazardArea class in the NZ model. 
Therefore it should only allow GM_Surface… 
I see no reason to have different models. 
The validity period should be enough to distinguish past and future. 
Or are they using kikelihoodOfOcurrence for future events? And magnitudeOrIntensity for past events? 

**Areas of potential significant flood risk**
https://cdr.eionet.europa.eu/help/Floods/Floods_2018/UML/GML_APSFR.png 

It follow the RiskZone class in the NZ model. 
Therefore it should only allow GM_Surface… 
![FME Automation](img/GML.PNG) 

SELECT [apsfrCode] 
      ,[crossBorderAPSFRCode] --- this will create a syncronisation issue 
      ,[crossBorderRelationship] 
      ,[nameOfAPSFR]  --- move to spatial? 
      ,[apsfrDataID] 
      ,[apsfrID] 
      ,[pk] 
  -- ### always null
      --,[hazardAreaCode] 
      --,[hazardAreaDescription] 
      --,[lat] 
      --,[lon] 
  FROM [Floods2018].[dbo].[APSFR_APSFRData] 

 

SELECT  DISTINCT  
  --- ONLY 49 RECORDS, BNATIVE LANGUAGES 
       [otherCharacteristicsDescription] 
      ,[otherMechanismDescription] 
      ,[otherSourceDescription] 
  /*** ALWAYS NULL  
      ,[characteristicsUncertainDescription] 
      ,[sourceUncertainDescription] 
  ,[characteristicsUncertain] 
      ,[mechanismUncertainDescription] 
  ***/ 
  FROM [Floods2018].[dbo].[APSFR_TypeOfFloods] 

Why was this ever modelled like this?! 
And  

![FME Automation](img/Typeoffloods.PNG) 