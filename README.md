# pyjiratimebooking

A python application which reads the jira credentials from a mappingtable.xlsx.

Then it goes overall timebookings in timebooking.xlsx and book it on the defined Issue at the defined date with the defined time if the instance matches.


You need to install pandas (pip install pandas), xlrd (pip install xlrd) and jira (pip install jira)


Steps
Install Python and Install GIT
Modify the PathtoPythonDirectory in Run_Script.bat and in Install.bat
Run Install.bat to get all necessary python libraries
Create Shortcut for Run_Script.bat to run it from Desktop
Modify Mappingtable.xlsx to add the JIRAInstance, JIRAUser and Password where you want to Add Worklog

Modify Timebooking.xlsx

End: Click on Run_Script.bat