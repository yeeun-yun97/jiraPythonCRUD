from jira import JIRA
import os

#your jira url
JIRA_URL_PREFIX=''
JIRA_URL=f'https://{JIRA_URL_PREFIX}.atlassian.net'

#your jira issue prefix
JIRA_PREFIX=''

#your jira username and api token
USER_EMAIL=''
API_TOKEN=''

#connect jira
jira=JIRA(server=JIRA_URL,basic_auth=(USER_EMAIL,API_TOKEN))



'''jira issue CRUD Functions'''
def createIssue(summary,description,issueType):
	return jira.create_issue(
		project=JIRA_PREFIX, 
		summary=summary,
		description=description, 
		issuetype={'name': issueType})

def readIssue(number):
	return jira.issue(f'{JIRA_PREFIX}-{number}')

def updateIssueDescription(issue,description):
	issue.update(notify=False, description=description)
def updateIssueAssign(issue,assignee):
	jira.assign_issue(issue,assignee)

def deleteIssue(issue):
	issue.delete()



'''print proj info'''
os.system('cat info.txt')

'''create example'''
issue0= createIssue('testSummary','this is description','Story')
issue1= createIssue('testSummary','this is description','Story')
os.system(f'echo created two issues {issue0}, {issue1}')

'''read example'''
number=1
issue2= readIssue(number)
os.system(f'echo read issue {issue2}')

'''update example'''
editDescription='editted description'
updateIssueDescription(issue2,editDescription)
updateIssueAssign(issue2,USER_EMAIL)
os.system(f'echo update issue {issue2} description to {editDescription} and assign to {USER_EMAIL}')

'''delete example'''
deleteIssue(issue1)
os.system(f'echo deleted issue {issue1}')


