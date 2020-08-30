from api.api_supporting_requests import APISupportingRequests
from entities_objects.base_entity import _BaseEntity


class CRFSchedule(_BaseEntity):

    def __init__(self, s_type, f_code, f_guid=None):
        super().__init__()
        self._type = s_type
        self._form_code = f_code
        self._form_guid = f_guid or APISupportingRequests().form_guid_by_code(f_code)
        self._guid = ''

        self._data_for_api = {
            "scheduleObject": {
                "spaceGuid": f"{self._headers['SpaceGuid']}",
                "projectGuid": f"{self._headers['ProjectGuid']}",
                "objectGuid": f"{self._headers['CrfGuidCode']}",
                "objectVersionGuid": f"{self._headers['CrfVersionGuidCode']}",
                "elementGuid": f"{self._form_guid}",
                "elementUid": f"{APISupportingRequests().form_uid_by_code(self._form_code)}",
                "elementType": "Form",
            },
            "schedule": {
                "scheduleType": f"{self._type}",
                "patternScheduleItems": []
            }
        }

    @property
    def _uri(self):
        return 'dmx-syts-schedule/api/v1/Schedule/create'

    @property
    def _pre_steps(self):
        return f"""          
        When I click on CRF DESIGNING button
        And I create schedule for record with params in forms table
            | column header     | td value              |
            | Form Code         | {self._form_code}     |
        And I choose {self._type} option in Schedule Type field
        """

    @property
    def _post_steps(self):
        return """
        And I click on CREATE button
        And I close Create Schedule popup
        """

    def repeat_type(self, value):
        """
        :param value should be in ['Day', 'Week', 'Month']
        """
        self._steps_for_web += f'And I choose One or several times per {value.lower()} option ' \
                               f'in Please, define a pattern for your schedule field\n'
        if value.lower() == 'day':
            self._data_for_api['schedule']['repeatType'] = "Everyday"
        elif value.lower() == 'week':
            self._data_for_api['schedule']['repeatType'] = "Weekly"
            raise Exception('Not implemented')
        elif value.lower() == 'month':
            self._data_for_api['schedule']['repeatType'] = "Monthly"
            raise Exception('Not implemented')
        else:
            exception = "Schedule repeat type should be in ['Day', 'Week', 'Month']"
            raise Exception(exception)
        return self

    def repeat_period(self, value):
        self._steps_for_web += f'And I put {value} in Repeat every field\n'
        self._data_for_api['schedule']['repeatPeriod'] = f"{value}"
        return self

    def valid_during(self, value):
        self._steps_for_web += f'And I put {value} in Valid during field\n'
        self._data_for_api['schedule']['validDuring'] = f"{value}"
        return self

    def times(self, times):
        self._steps_for_web += f'And I add several times: {times}\n'

        times = [{
            "actionTime": f"Thu Jan 01 1970 {time.strip()}",
            "isDeleted": "False"
        } for time in times.split(',')]
        self._data_for_api['schedule']['patternScheduleItems'] = times
        return self
