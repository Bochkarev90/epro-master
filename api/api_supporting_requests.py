import requests
import urllib3

from api.api_admin_singleton import APIAdmin
from config import HOST


urllib3.disable_warnings()


class APISupportingRequests:

    def __init__(self):
        self._token = APIAdmin().token
        self._headers = APIAdmin().headers

    def visit_type_guid_by_value(self, visit_type_title):
        url = HOST + 'dmx-syts-dictionary/api/DictionaryValues'
        params = {
            'dictionaryTypeName': 'StudyEventType'
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for visit_type in response:
            if visit_type['title'] == visit_type_title:
                return visit_type['guidCode']
        exception = f'No visit type {visit_type_title} found'
        raise Exception(exception)

    def form_type_guid_by_value(self, form_type_title):
        url = HOST + 'dmx-syts-dictionary/api/DictionaryValues'
        params = {
            'dictionaryTypeName': 'FormType'
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for form_type in response:
            if form_type['title'] == form_type_title:
                return form_type['guidCode']
        exception = f'No form type {form_type_title} found'
        raise Exception(exception)

    def visit_guid_by_title(self, v_title):
        url = HOST + 'crf/studyevent'
        params = {
            'crfVersionGuid': self._headers['CrfVersionGuidCode']
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()['value']
        for visit in response:
            if visit['title'] == v_title:
                return visit['guidCode']
        exception = f'No visit with title {v_title}'
        raise Exception(exception)

    def form_guid_by_code(self, f_code):
        url = HOST + 'dmx-crf-core-api/form'
        params = {
            'crfVersionGuid': self._headers['CrfVersionGuidCode']
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()['value']
        for form in response:
            if form['formCode'] == f_code:
                return form['guidCode']
        exception = f'No form with code {f_code}'
        raise Exception(exception)

    def form_uid_by_code(self, f_code):
        url = HOST + 'dmx-crf-core-api/form'
        params = {
            'crfVersionGuid': self._headers['CrfVersionGuidCode']
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()['value']
        for form in response:
            if form['formCode'] == f_code:
                return form['uidCode']
        exception = f'No form with code {f_code}'
        raise Exception(exception)

    def section_guid_by_form_and_section_codes(self, f_code, s_code):
        url = HOST + f'dmx-crf-core-api/form({self.form_guid_by_code(f_code)})'
        params = {
            'crfVersionGuid': self._headers['CrfVersionGuidCode']
        }
        sections = requests.get(url=url, params=params, headers=self._headers, verify=False).json()['data']['sections']
        for section in sections:
            if section['sectionCode'] == s_code:
                return section['guidCode']
        exception = f'No section with code {s_code} in form with code {f_code}'
        raise Exception(exception)

    def item_type_guid_by_value(self, item_type_title):
        item_type_title = item_type_title.replace(' ', '')
        url = HOST + 'dmx-syts-dictionary/api/DictionaryValues'
        params = {
            'dictionaryTypeName': 'ItemType'
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for item_type in response:
            if item_type['title'] == item_type_title:
                return item_type['guidCode']
        exception = f'No {item_type_title} item type found'
        raise Exception(exception)

    def data_type_guid_by_value(self, data_type_title):
        url = HOST + 'dmx-syts-dictionary/api/DictionaryValues'
        params = {
            'dictionaryTypeName': 'DataType'
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for data_type in response:
            if data_type['title'] == data_type_title.title():
                return data_type['guidCode']
        exception = f'No {data_type_title} data type found'
        raise Exception(exception)

    def control_type_guid_by_value(self, control_type_title):
        url = HOST + 'dmx-syts-dictionary/api/DictionaryValues'
        params = {
            'dictionaryTypeName': 'ControlType'
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for control_type in response:
            if control_type['title'] == control_type_title.title():
                return control_type['guidCode']
        exception = f'No {control_type_title} control type found'
        raise Exception(exception)

    def edc_and_edc_version_guids_by_edc_env_title(self, edc_env_title):
        url = HOST + 'dmx-edc-core-api/api/v1/edc'
        response = requests.get(url=url, headers=self._headers, verify=False).json()
        for edc_env in response['edc']:
            if edc_env['edcEnvironment'] == edc_env_title.title():
                return edc_env['edcGuid'], edc_env['edcVersionGuid']
        exception = f'No {edc_env_title} edc environment found'
        raise Exception(exception)

    def subject_guid_by_subject_code_and_edc_env_title(self, subject_code, edc_env_title):
        url = HOST + 'dmx-edc-core-api/api/v1/subject/matrix/Subjects'
        params = {
            'EdcGuid': self.edc_and_edc_version_guids_by_edc_env_title(edc_env_title)[0]
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for subject_guid, subject_data in response['subjects'].items():
            if subject_data['subjectKey'] == subject_code:
                return subject_guid
        exception = f'No subject with {subject_code} code found in {edc_env_title} environment'
        raise Exception(exception)

    def site_and_country_guids_by_site_code_and_edc_environment_title(self, site_code, edc_env_title):
        url = HOST + 'dmx-edc-core-api/api/v1/subject/matrix/structure'
        edc_guid, edc_version_guid = self.edc_and_edc_version_guids_by_edc_env_title(edc_env_title)
        params = {
            'EdcGuid': edc_guid,
            'EdcVersionGuid': edc_version_guid
        }
        response = requests.get(url=url, params=params, headers=self._headers, verify=False).json()
        for site_guid, site_data in response['sites'].items():
            if site_data['siteId'] == site_code:
                return site_guid, site_data['countryGuid']
        exception = f'No site with {site_code} code found in {edc_env_title} environment'
        raise Exception(exception)


if __name__ == '__main__':
    print(APISupportingRequests().visit_type_guid_by_value('Common'))
