
#   AZURE DEVOPS NOTES

DaveB FEB-2022

## 1. Schema Comparison


Not necessary - just for checks


## 2. "Publish Profile" file creation


- necessary to avoid objects in the Target database
  being dropped by the release

Victor's instructions;
https://wahealthdept.sharepoint.com/:w:/r/sites/DISDatawarehouseProject/_layouts/15/Doc.aspx?sourcedoc=%7B9BCD40DA-2091-4533-BDB0-AB2295693F28%7D&file=SSDT%20-%20Publish%20Database%20Settings.docx&action=default&mobileredirect=true


General Info Online (use Victor's notes first);
https://microsoft-bitools.blogspot.com/2020/04/databases-in-devops-publishing-profile.html
https://www.mssqltips.com/sqlservertip/5456/using-advanced-publish-settings-for-visual-studio-database-project/


- create the Publish Profile
- create the Publish Profile file in the VS Solution
  - Remove from gitignore (right click on *.publish.xml file and )
- add the Publish Profile to version control
  - add
  - commit
  - sync



## 3. Visual Studio Prepea