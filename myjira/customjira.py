from jira import JIRA

from config import JIRA_LOGIN, JIRA_PASSWORD


class CustomJira:

    jira_options = {'server': 'https://jira.dm.dm-matrix.com/'}
    _jira = JIRA(options=jira_options, basic_auth=(JIRA_LOGIN, JIRA_PASSWORD))
    task_id = '10003'
    bug_id = '10004'
    sub_task_id = '10000'
    sub_bug_id = '10900'

    def _all_jira_info(self):
        for project in self._jira.createmeta()['projects']:
            print(project)

    def create_issue(self, summary, description):
        data = {
            "fields":
                {
                    "project":
                        {
                            "key": 'CDMS'
                        },
                    "summary": summary,
                    "description": description,
                    "issuetype":
                        {
                            "id": self.task_id
                        },
                }
        }
        new_issue = self._jira.create_issue(**data)
        return new_issue
