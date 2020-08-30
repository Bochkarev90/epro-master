from api.api_supporting_requests import APISupportingRequests
from entities_objects.base_entity import _BaseEntity


class CRFItem(_BaseEntity):

    def __init__(self, i_title, i_code, i_order, f_code, s_code, s_guid=None):
        super().__init__()
        self._title = i_title
        self._code = i_code
        self._order = i_order
        self._form_code = f_code
        self._section_code = s_code
        self._section_guid = s_guid or APISupportingRequests().section_guid_by_form_and_section_codes(f_code=f_code,
                                                                                                      s_code=s_code)
        self._guid = ''

        self._data_for_api = {
            'title': f"{self._title}",
            'itemCode': f"{self._code}",
            'sequence': f"{self._order}",
            'crfVersionGuid': f"{self._headers['CrfVersionGuidCode']}",
            'sectionGuid': f"{self._section_guid}",
            'itemTypeGuid': "9dcb51de-e109-48e9-b61a-ac3d841e124f",
            'dataTypeGuid': "e9952d97-fae5-46c0-a66b-ed3205036c8f",
            'controlTypeGuid': "9cf0e53c-1653-4c50-beff-1aa380b9eed3"
        }

    @property
    def _uri(self):
        return 'dmx-crf-core-api/item'

    @property
    def _pre_steps(self):
        return f"""
        When I click on CRF DESIGNING button
        And I click on SYNC button
        And I expand record with params in forms table
            | column header     | td value               |
            | Form Code         | {self._form_code}      |
        And I expand record with params in sections table
            | column header     | td value               |
            | Section Code      | {self._section_code}   |
        And I click on ADD NEW ITEM button
        And I put {self._title} in Title field
        And I put {self._code} in Code field
        And I put {self._order} in Order field
        """

    @property
    def _post_steps(self):
        return """
        And I click on SAVE button
        Then Add New Item popup disappears
        """

    def field_type(self, value):
        self._steps_for_web += f'And I choose {value} option in Field Type field\n'
        self._data_for_api['itemTypeGuid'] = APISupportingRequests().item_type_guid_by_value(value)
        return self

    def data_type(self, value):
        self._steps_for_web += f'And I choose {value} option in Data Type field\n'
        self._data_for_api['dataTypeGuid'] = APISupportingRequests().data_type_guid_by_value(value)
        return self

    def control_type(self, value):
        self._steps_for_web += f'And I choose {value} option in Control Type field\n'
        self._data_for_api['controlTypeGuid'] = APISupportingRequests().control_type_guid_by_value(value)
        return self
