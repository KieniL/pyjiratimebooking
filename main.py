import jira_py, urllib.request, urllib.error, numpy

import pandas as pd


#define the Paths to the JIRAInstance and the TimebookingMapping
filePathMapping = "Mappingtable.xlsx"

filePathTimeBooking = "Timebooking.xlsx"


#Read the JIRAInstance data into variable
credentials = pd.read_excel(filePathMapping)
#Read the Timebooking data into variable
timebooking = pd.read_excel(filePathTimeBooking)


for indexCred, credRow in credentials.iterrows():
    try:
        #Try to open the URL to check if it is reachable
        url_requested = urllib.request.urlopen(credRow['JIRAURL'])
        if 200 == url_requested.code:
            for indexTime, timeRow in timebooking.iterrows():
                #Add Worklog to JIRA Issue
                if credRow['JIRAURL'] == timeRow['JIRAURL']:
                    #if not numpy.isnan(timeRow['Comment']) and len(str(timeRow['Comment'])) > 0:
                    if pd.notnull(timeRow['Comment']):
                        timelog = jira_py.logWork(timeRow['JIRAURL'],  credRow['JIRAUser'], credRow['JIRAPW'], timeRow['JIRAIssue'], timeRow['Date'], timeRow['Time'], timeRow['Comment'])
                    else:
                        timelog = jira_py.logWork(timeRow['JIRAURL'],  credRow['JIRAUser'], credRow['JIRAPW'], timeRow['JIRAIssue'], timeRow['Date'], timeRow['Time'], None)
                    if timelog:
                        print("Time logged on " + timeRow['JIRAIssue'])
                    
    #Except if the URL could not be read
    except urllib.error.URLError as e: print('URL ' + credRow['JIRAURL'] + ' could not be read')
    #Except a ValueError and prints it
    except ValueError as e: print(e)
          
