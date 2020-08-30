from abc import abstractmethod

import requests

from api.api_admin_singleton import APIAdmin
from config import HOST


class _BaseEntity:

    def __init__(self):
        self._headers = APIAdmin().headers
        self._steps_for_web = ''
        self._data_for_api = {}
        self._guid = ''
        self._title = ''
        self._code = ''

    @property
    @abstractmethod
    def _uri(self):
        return

    @property
    @abstractmethod
    def _pre_steps(self):
        return

    @property
    @abstractmethod
    def _post_steps(self):
        return

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

    def create_by_api(self):
        url = HOST + self._uri
        response = requests.post(url=url, headers=self._headers, data=str(self._data_for_api), verify=False)
        if response.status_code != 200:
            exception = '\nStatus code: ' + str(response.status_code) + '\n' + response.text
            raise Exception(exception)
        try:
            self._guid = response.json()['data']
        except KeyError:
            self._guid = response.json()['scheduleGuid']

    @property
    def steps(self):
        return self._pre_steps + self._steps_for_web + self._post_steps

    @property
    def title(self):
        return self._title

    @property
    def code(self):
        return self._code
