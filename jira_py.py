import jira
from jira import JIRA, exceptions as jiraex

#Authentication Method
def authenticate(username, password):
    basic_auth=(username, password)
    return basic_auth

#Create a JIRA Object which can be used later on
def createJIRAObject(jiraURL, username, password):
    jira = JIRA(server=jiraURL, basic_auth=authenticate(username, password))
    return jira


#Create JIRA Object and log the input timespent on the input issue
def logWork(jiraURL, username, password, issue, date, timespent):
        
    jira = createJIRAObject(jiraURL, username, password)

    try:     
        worklog = jira.add_worklog(issue = issue,timeSpent = timespent, started = date)

        return worklog
    except jiraex.JIRAError as e: print("Time logging not possible on " + issue)

    

    
