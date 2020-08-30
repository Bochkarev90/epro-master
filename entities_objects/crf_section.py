from api.api_supporting_requests import APISupportingRequests
from entities_objects.base_entity import _BaseEntity


class CRFSection(_BaseEntity):

    def __init__(self, s_title, s_code, s_order, f_code, f_guid=None):
        super().__init__()
        self._title = s_title
        self._code = s_code
        self._order = s_order
        self._form_code = f_code
        self._form_guid = f_guid or APISupportingRequests().form_guid_by_code(f_code)
        self._guid = ''

        self._data_for_api = {
            'sectionItems': [],
            'formSections': [{"guidCode": f"{self._form_guid}", "isMirror": "False"}],
            'crfVersionGuid': f"{self._headers['CrfVersionGuidCode']}",
            'title': f"{self._title}",
            'sectionCode': f"{self._code}",
            'sequence': f"{self._order}",
            'formGuid': f"{self._form_guid}"
        }

    @property
    def _uri(self):
        return 'dmx-crf-core-api/section'

    @property
    def _pre_steps(self):
        return f"""          
        When I click on CRF DESIGNING button
        And I filter forms table by Form Code column with {self._form_code} value
        And I expand record with params in forms table
            | column header     | td value               |
            | Form Code         | {self._form_code}      |
        And I click on ADD SECTION button
        And I put {self._title} in Section Name field
        And I put {self._code} in Section Code field
        And I put {self._order} in Order field
        """

    @property
    def _post_steps(self):
        return """
        And I click on SAVE button
        Then Add New Section popup disappears
        """

    @property
    def form_code(self):
        return self._form_code

    def is_repeated(self, value):
        if bool(value):
            self._steps_for_web += 'And I mark is repeated checkbox'
        else:
            self._steps_for_web += 'And I unmark is repeated checkbox'
        self._data_for_api['isRepeating'] = str(value)
        return self
