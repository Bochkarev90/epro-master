from behave.formatter.base import Formatter

from myjira.customjira import CustomJira
from mytestrail.testrailsettings import STATUS_IDS
from mytestrail.customtestrail import CustomTestRail


class FormattedFeature:

    def __init__(self, feature, section_id):
        self._feature = feature
        self._section_id = section_id

    @property
    def title(self):
        return self._feature.name

    @property
    def description(self):
        return f'Feature: {self.title} \n' + '\n'.join(self._feature.description)

    @property
    def background(self):
        background_title = f'\n\nBackground: {self._feature.background.name}\n'
        background_steps = '\n\t'.join([step.keyword + ' ' + step.name for step in self._feature.background.steps])
        return background_title + background_steps if self._feature.background else ''

    @property
    def duration(self):
        return self._feature.duration

    @property
    def status(self):
        return self._feature.status

    @property
    def scenarios(self):
        return [FormattedScenario(scenario) for scenario in self._feature.scenarios]

    @property
    def section_id(self):
        return self._section_id


class FormattedScenario:

    def __init__(self, scenario):
        self._scenario = scenario

    @property
    def title(self):
        return self._scenario.name

    @property
    def duration(self):
        duration = str(round(self._scenario.duration)) + 's'
        return duration

    @property
    def status(self):
        status = str(self._scenario.status)[7:].title()
        return STATUS_IDS[status]

    @property
    def tags(self):
        return self._scenario.tags

    @property
    def precondition_steps(self):
        return '\n'.join([FormattedStep(step).title for step in self._scenario.steps if step.step_type is 'given'])

    @property
    def steps(self):
        return [FormattedStep(step) for step in self._scenario.steps if step.step_type is not 'given']


class FormattedStep:

    def __init__(self, step):
        self._step = step

    @property
    def title(self):
        title = self._step.keyword + ' ' + self._step.name
        if self._step.table:
            title += FormattedTable(self._step.table).table
        return title

    @property
    def duration(self):
        duration = str(round(self._step.duration, 2))
        return duration

    @property
    def status(self):
        status = str(self._step.status)[7:].title()
        return status

    @property
    def expected(self):
        return ''

    @property
    def content(self):
        return {'content': self.title, 'expected': self.expected}

    @property
    def error_message(self):
        return self._step.error_message if self._step.error_message else ''

    @property
    def result(self):
        return {
            'content': self.title,
            'expected': self.expected,
            'actual': self.status + ': ' + self.duration + '\n' + self.error_message,
            'status_id': STATUS_IDS[self.status]
        }


class FormattedTable:

    def __init__(self, table):
        self._table = table

    @property
    def headings(self):
        return '\n|||:' + '|'.join(self._table.headings) + '\n||'

    @property
    def cells(self):
        return '\n|| '.join(['|'.join(row.cells) for row in self._table])

    @property
    def table(self):
        return self.headings + self.cells


class CustomTestRailFormatter(Formatter):

    name = 'CustomReporter'
    description = 'TestRail dump of test run'

    def __init__(self, stream_opener, config):
        super(CustomTestRailFormatter, self).__init__(stream_opener, config)
        self._features = []
        self._file_path = ''
        self._testrail = CustomTestRail()
        self._testrail_section_id = None
        self._current_feature = None
        self._cases_ids = []
        self._failed_scenarios = []

    def _check_existing_features_in_testrail_and_create_not_existing(self, uri):
        # 'features/CRF Designer/ePRO Forms/Creation.feature' -> ['CRF Designer', 'ePRO Forms', 'Creation.feature']
        self._file_path = uri.split('/')[1:]
        # ['CRF Designer', 'ePRO Forms', 'Creation.feature'] -> ['CRF Designer', 'ePRO Forms', 'Creation']
        self._file_path[-1] = self._file_path[-1][:self._file_path[-1].find('.feature')]

        parent_folder_id = None
        for folder in self._file_path:
            sections_ids = self._testrail.get_sections_ids_by_title(folder, parent_folder_id)
            if len(sections_ids) == 0:
                parent_folder_id = self._testrail.add_section(title=folder, parent_section_id=parent_folder_id)
            elif len(sections_ids) > 1:
                raise Exception("There are several folders with same path. Check folders/features names")
            else:  # len(sections_ids) == 1
                parent_folder_id = sections_ids[0]
        testrail_section_id = parent_folder_id
        return testrail_section_id

    def _update_feature_title_and_description_in_testrail(self, formatted_feature):
        self._testrail.update_section(section_id=formatted_feature.section_id,
                                      title=formatted_feature.title,
                                      description=formatted_feature.description)

    def _update_scenarios_in_testrail(self, formatted_feature):
        for scenario in formatted_feature.scenarios:
            case_id = self._testrail.get_cases_ids_by_title(case_title=scenario.title,
                                                            section_id=self._testrail_section_id)
            if len(case_id) == 0:
                self._cases_ids.append(self._testrail.add_case(case_title=scenario.title,
                                                               section_id=self._testrail_section_id,
                                                               steps=[step.content for step in scenario.steps],
                                                               background=scenario.precondition_steps))
            elif len(case_id) > 1:
                raise Exception("There are several cases with given title. Please check")
            else:  # len(cases_ids) == 1
                self._testrail.update_case(case_id=case_id[0],
                                           steps=[step.content for step in scenario.steps],
                                           background=scenario.precondition_steps)
                self._cases_ids.append(case_id[0])

    def uri(self, uri):
        self._testrail_section_id = self._check_existing_features_in_testrail_and_create_not_existing(uri)

    def feature(self, feature):
        self._current_feature = feature
        formatted_feature_before_start = FormattedFeature(self._current_feature, self._testrail_section_id)
        self._update_feature_title_and_description_in_testrail(formatted_feature_before_start)
        self._update_scenarios_in_testrail(formatted_feature_before_start)

    def scenario(self, scenario):
        print(scenario.name + ' is in process')

    def eof(self):
        formatted_feature_after_start = FormattedFeature(self._current_feature, self._testrail_section_id)
        self._features.append(formatted_feature_after_start)

    def close(self):
        # Jira
        # jira_ticket_summary = 'Automation Результаты тестового прогона'
        # jira_ticket_description = f'Идет процесс выгрузки результатов'
        # jira_task = CustomJira().create_issue(summary=jira_ticket_summary,
        #                                       description=jira_ticket_description)

        # TestRail
        run_id = self._testrail.add_run(self._cases_ids)
        for feature in self._features:
            for scenario in feature.scenarios:
                case_id = self._testrail.get_cases_ids_by_title(scenario.title, feature.section_id)[0]
                status = scenario.status
                defects = None
                if status == 5:  # failed
                    self._failed_scenarios.append(scenario.title)
                    # defects = jira_task.key
                steps_results = [step.result for step in scenario.steps]
                result_id = self._testrail.add_result_for_case(run_id=run_id,
                                                               case_id=case_id,
                                                               status=status,
                                                               duration=scenario.duration,
                                                               steps_results=steps_results,
                                                               defects=defects)

        # Jira again
        # jira_task.update(description=f'Всего запущено тестов: {len(self._cases_ids)}\n'
        #                              f'Из них не пройдено: {len(self._failed_scenarios)}. '
        #                              f'Упавшие тесты прикреплены')
