import time

from config import TESTRAIL_LOGIN, TESTRAIL_PASSWORD
from mytestrail.testrail import *


class CustomTestRail:
    client = APIClient('https://datamatrix.testrail.io/')
    client.user = TESTRAIL_LOGIN
    client.password = TESTRAIL_PASSWORD
    project_id = 7  # ePRO project https://datamatrix.testrail.io/index.php?/projects/overview/7
    suite_id = 243  # ePRO suite https://datamatrix.testrail.io/index.php?/suites/view/243

    def __init__(self):
        self._sections = []

    def get_sections_ids_by_title(self, section_title, parent_section_id=None):
        if not self._sections:
            self._sections = self.client.send_get(f'get_sections/{self.project_id}&suite_id={self.suite_id}')
        section_ids = []
        for section in self._sections:
            if section['name'].lower() == section_title.lower() and section['parent_id'] == parent_section_id:
                section_ids.append(section['id'])
        return section_ids

    def add_section(self, title, parent_section_id: int = None, description: str = None):
        data = {'name': title, 'suite_id': self.suite_id}
        if parent_section_id:
            data['parent_id'] = parent_section_id
        if description:
            data['description'] = description
        new_section_id = self.client.send_post(uri=f'add_section/{self.project_id}', data=data)['id']
        # Refresh sections list after new section adding
        self._sections = self.client.send_get(f'get_sections/{self.project_id}&suite_id={self.suite_id}')
        return new_section_id

    def update_section(self, section_id, title: str = None, description: str = None):
        data = {}
        if title:
            data['name'] = title
        if description:
            data['description'] = description
        self.client.send_post(uri=f'update_section/{section_id}', data=data)

    def get_cases_ids_by_title(self, case_title, section_id):
        cases_ids = []
        cases = self.client.send_get(f'get_cases/{self.project_id}&suite_id={self.suite_id}&section_id={section_id}')
        for case in cases:
            if case['title'].lower() == case_title.lower():
                cases_ids.append(case['id'])
        return cases_ids

    def add_case(self, case_title, section_id, automation_type='3', release_status='2', priority='2', steps=None,
                 background: str = None):
        data = {
            'title': case_title,
            'custom_automation_type': automation_type,
            'custom_release_status': release_status,
            'custom_preconds': background,
            'priority_id': priority,
            "custom_steps_separated": steps
        }
        new_case_id = self.client.send_post(uri=f'add_case/{section_id}', data=data)['id']
        # This is for adding case_id to custom field CASE_ID in TestRail
        self.update_case(new_case_id)
        return new_case_id

    def update_case(self, case_id, automation_type='3', steps=None, background: str = None):
        data = {
            'custom_automation_type': automation_type,
            'custom_caseid': 'C' + str(case_id)
        }
        if steps:
            data['custom_steps_separated'] = steps
        if background:
            data['custom_preconds'] = background
        return self.client.send_post(uri=f'update_case/{case_id}', data=data)

    def _get_cases_ids_by_py_bdd_automation_type(self):
        return [case['id'] for case in self.client.send_get('get_cases/7&suite_id=243')
                if case['custom_automation_type'] == 3]

    def add_run(self, case_ids):
        data = {
            'suite_id': self.suite_id,
            'include_all': False,
            'case_ids': case_ids,
            'name': time.asctime()
        }
        return self.client.send_post(uri=f'add_run/{self.project_id}',
                                     data=data)['id']

    def add_result_for_case(self, run_id, case_id, status, duration, steps_results, defects=None):
        data = {
            'status_id': status,
            'elapsed': duration,
            'custom_step_results': steps_results
        }
        if defects:
            data['defects'] = defects
        result_id = self.client.send_post(uri=f'add_result_for_case/{run_id}/{case_id}', data=data)['id']
        return result_id

    def add_screenshot_to_result(self, result_id, screenshot_abs_path):
        attachment_id = self.client.send_post(uri=f'add_attachment_to_result/{result_id}',
                                              data=screenshot_abs_path)['attachment_id']
        return attachment_id


if __name__ == '__main__':
    CustomTestRail().add_result_for_case('489', '30901', '5', '15s', steps_results=None)
