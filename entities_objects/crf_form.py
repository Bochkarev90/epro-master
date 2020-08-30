from api.api_supporting_requests import APISupportingRequests
from entities_objects.base_entity import _BaseEntity


class CRFForm(_BaseEntity):

    def __init__(self, f_type, f_title, f_code, f_order, v_title, v_guid=None):
        super().__init__()
        self._title = f_title
        self._code = f_code
        self._type = f_type
        self._order = f_order
        self._visit_title = v_title
        self._visit_guid = v_guid or APISupportingRequests().visit_guid_by_title(v_title)
        self._guid = ''

        self._data_for_api = {
            'projectGuid': f"{self._headers['ProjectGuid']}",
            'crfVersionGuid': f"{self._headers['CrfVersionGuidCode']}",
            'title': f"{self._title}",
            'formCode': f"{self._code}",
            'formTypeGuid': f"{APISupportingRequests().form_type_guid_by_value(self._type)}",
            'studyEventForms': [{"guidCode": f"{self._visit_guid}", "isMirror": "False"}],
            'sequence': f"{self._order}",
            'studyEventGuid': f"{self._visit_guid}",
            'isRepeating': "False" if self._type.lower() != 'epro' else "True",
            'languageGuid': f"{self._headers['LanguageGuidCode']}"
        }

    @property
    def _uri(self):
        return 'dmx-crf-core-api/form'

    @property
    def _pre_steps(self):
        return f"""
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
        And I put {self._title} in Form Name field
        And I put {self._code} in Form Code field
        And I put {self._order} in Order field
        And I choose {self._type} option in Form Type field
        And I choose {self._visit_title} option in Visit field
        """

    @property
    def _post_steps(self):
        return """
        And I click on SAVE button
        Then Add New Form popup disappears
        """

    def is_repeated(self, value):
        if bool(value):
            self._steps_for_web += 'And I mark is repeated checkbox'
        else:
            self._steps_for_web += 'And I unmark is repeated checkbox'
        self._data_for_api['isRepeating'] = str(value)
        return self
