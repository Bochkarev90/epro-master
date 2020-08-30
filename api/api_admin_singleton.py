import requests
from config import API_ADMIN_LOGIN, API_ADMIN_PASSWORD, HOST


class _AuthorizationError(Exception):
    def __init__(self, text):
        self.txt = text


class _APIAdminMeta(type):

    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class APIAdmin(metaclass=_APIAdminMeta):

    __login = API_ADMIN_LOGIN
    __password = API_ADMIN_PASSWORD
    __host = HOST

    def __init__(self):
        self._token = self._get_token()
        self._headers = self._get_headers()

    @property
    def token(self):
        return self._token

    @property
    def headers(self):
        return self._headers

    def _get_token(self):
        url = self.__host + 'identity/api/token/connect/?forceLogin=true'
        data = {
            'username': self.__login,
            'password': self.__password
        }
        response = requests.post(url=url, json=data, verify=False)
        if response.status_code != 200:
            raise _AuthorizationError('Не удалось авторизоваться')
        response = response.json()
        return 'Bearer ' + response['access_token']

    def _get_headers(self):
        url = self.__host + 'identity/api/SessionInfo'
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url=url, headers=headers, verify=False).json()
        headers['ProjectGuid'] = response[0]['ProjectGuidCode']
        headers['SpaceGuid'] = response[0]['SpaceGuidCode']
        headers['CrfVersionGuidCode'] = response[0]['CrfVersionGuidCode']
        headers['CrfGuidCode'] = response[0]['CrfGuidCode']
        headers['LanguageGuidCode'] = response[0]['LanguageGuidCode']
        return headers

    def refresh_token_and_headers(self):
        self._token = self._get_token()
        self._headers = self._get_headers()


if __name__ == '__main__':
    pass
