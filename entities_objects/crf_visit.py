from api.api_supporting_requests import APISupportingRequests
from entities_objects.base_entity import _BaseEntity


class CRFVisit(_BaseEntity):

    def __init__(self, v_title, v_code, v_type):
        super().__init__()
        self._title = v_title
        self._code = v_code
        self._type = v_type

        self._data_for_api = {
            'projectGuid': f"{self._headers['ProjectGuid']}",
            'crfVersionGuid': f"{self._headers['CrfVersionGuidCode']}",
            'title': f"{v_title}",
            'studyEventCode': f"{v_code}",
            'studyEventTypeGuid': f"{APISupportingRequests().visit_type_guid_by_value(v_type)}",
        }

    @property
    def _uri(self):
        return 'dmx-crf-core-api/studyevent'

    @property
    def _pre_steps(self):
        return f"""
        When I click on VISIT STRUCTURE button
        And I click on ADD VISIT button
        And I put {self._title} in Visit Name field
        And I put {self._code} in Visit Code field
        And I choose {self._type} option in Visit Type field
        """

    @property
    def _post_steps(self):
        return f"""            
        And I click on SAVE button
        Then Add Visit popup disappears
        """

    def order(self, value):
        self._steps_for_web += f'And I put {str(value)} in Order field'
        self._data_for_api['sequence'] = str(value)
        return self


if __name__ == '__main__':
    CRFVisit('1', '1', 'Common').create_by_api()
