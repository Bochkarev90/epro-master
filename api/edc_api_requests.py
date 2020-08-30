from api.api_admin_singleton import APIAdmin


class EDCAPIRequests:

    def __init__(self):
        self._token = APIAdmin().token
        self._headers = APIAdmin().headers

    def add_subject(self, edc_environment_title, clinic_code):
        pass
