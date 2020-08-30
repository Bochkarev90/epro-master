import requests

from api.api_admin_singleton import APIAdmin
from config import HOST


class CRFAPIRequests:

    def __init__(self):
        self._token = APIAdmin().token
        self._headers = APIAdmin().headers

    def to_review(self):
        url = HOST + 'structure/workflow/review'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "91c2ef6f-a948-42fc-aec1-b82b2f5e0a4c",
            "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def first_approve(self):
        url = HOST + 'structure/workflow/approve'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "33398b56-17a4-4094-97a2-018f095ad4fb",
            "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def to_test(self):
        url = HOST + 'structure/workflow/test'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "33398b56-17a4-4094-97a2-018f095ad4fb",
            "crfStateGuid": "18103ca4-363a-4211-bc65-90c3db0af7d5"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def second_approve(self):
        url = HOST + 'structure/workflow/approve'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "3fe1ca1f-78bd-4b5e-903c-f91b6af60fde",
            "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def first_reject(self):
        url = HOST + 'structure/workflow/reject'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "33398b56-17a4-4094-97a2-018f095ad4fb",
            "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def second_reject(self):
        url = HOST + 'structure/workflow/reject'
        data = {
            "crfGuid": f"{self._headers['CrfGuidCode']}",
            "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
            "crfStatusGuid": "3fe1ca1f-78bd-4b5e-903c-f91b6af60fde",
            "crfStateGuid": "18103ca4-363a-4211-bc65-90c3db0af7d5"
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def deploy_to_sandbox(self):
        url = HOST + 'structure/workflow/deploy'
        data = {
            "deployRequest": {
                "edcEnvironmentGuid": "409420d0-7f6f-4626-bf5e-c9b5116c6e56",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "autoUpdateSubjects": "true"
            },
            "workflowRequest": {
                "crfGuid": f"{self._headers['CrfGuidCode']}",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "crfStatusGuid": "91c2ef6f-a948-42fc-aec1-b82b2f5e0a4c",
                "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
            }
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def deploy_to_test(self, edc_title):
        url = HOST + 'structure/workflow/deploy'
        data = {
            "deployRequest": {
                "edcEnvironmentGuid": "66d4b691-0bc0-461c-9262-1e26c62d3fb2",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "edcName": f"{edc_title}",
                "autoUpdateSubjects": "true"
            },
            "workflowRequest": {
                "crfGuid": f"{self._headers['CrfGuidCode']}",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "crfStatusGuid": "33398b56-17a4-4094-97a2-018f095ad4fb",
                "crfStateGuid": "25918b1c-3108-4706-8630-349c51f332b0"
            }
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def deploy_to_training(self, edc_title):
        url = HOST + 'structure/workflow/deploy'
        data = {
            "deployRequest": {
                "edcEnvironmentGuid": "af08f050-bdf8-4658-b355-f536faad0b64",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "edcName": f"{edc_title}",
                "autoUpdateSubjects": "true"
            },
            "workflowRequest": {
                "crfGuid": f"{self._headers['CrfGuidCode']}",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "crfStatusGuid": "3fe1ca1f-78bd-4b5e-903c-f91b6af60fde",
                "crfStateGuid": "18103ca4-363a-4211-bc65-90c3db0af7d5"
            }
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def deploy_to_production(self, edc_title):
        url = HOST + 'structure/workflow/deploy'
        data = {
            "deployRequest": {
                "edcEnvironmentGuid": "885d313a-e7a1-4ed4-8f3e-9ae674ff4698",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "edcName": f"{edc_title}",
                "autoUpdateSubjects": "true"
            },
            "workflowRequest": {
                "crfGuid": f"{self._headers['CrfGuidCode']}",
                "crfVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "crfStatusGuid": "3fe1ca1f-78bd-4b5e-903c-f91b6af60fde",
                "crfStateGuid": "18103ca4-363a-4211-bc65-90c3db0af7d5"
            }
        }
        response = requests.post(url=url, data=str(data), headers=self._headers, verify=False)
        if response.status_code != 200:
            exception = str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        return self

    def create_new_version(self):
        raise Exception("Not implemented. Need to understand how to save CRF Version guid")
