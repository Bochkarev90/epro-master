from selene.api import *

from helpers.helpers import take_element_screenshot


class SubjectMatrix:
    
    def __init__(self):
        self._element_css_selector = 'div.edc-matrix'
        self._headers_css_selector = 'div.edc-matrix-headers > div.sub-item > span.sub-item-visit-title'
        self._subjects_row_css_selector = 'dmx-edc-subject-matrix-line > div.sub-line-holder'
        self._subjects_css_selector = 'span.subject-key-title'

    def __getitem__(self, subject_title):
        subject_index = self.subjects.index(subject_title)
        subject_element = ss(self._subjects_row_css_selector).filtered_by(be.visible)[subject_index]
        return _SubjectRow(subject_element, self.visits)

    @property
    def element(self):
        return s(self._element_css_selector)

    @property
    def subjects(self):
        return [subject.text for subject in ss(self._subjects_css_selector).filtered_by(be.visible)]
    
    @property
    def visits(self):
        return [header.text for header in self.element.ss(self._headers_css_selector).filtered_by(be.visible)]

    @property
    def first_subject(self):
        subject_element = ss(self._subjects_row_css_selector).filtered_by(be.visible)[0]
        return _SubjectRow(subject_element, self.visits)

    @property
    def last_subject(self):
        subject_element = ss(self._subjects_row_css_selector).filtered_by(be.visible)[-1]
        return _SubjectRow(subject_element, self.visits)

    def subject_by_title(self, subject_title):
        subject_index = self.subjects.index(subject_title)
        subject_element = ss(self._subjects_row_css_selector).filtered_by(be.visible)[subject_index]
        return _SubjectRow(subject_element, self.visits)

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.element)
        return self


class _SubjectRow:

    def __init__(self, subject_row_element, visits):
        self._row_element = subject_row_element
        self._visits = visits

        self._access_code_icon_css_selector = 'span.subj-line-functional-icon'
        self._cell_css_selector = 'div.sub-item'

    def __getitem__(self, visit_code):
        visit_index = self._visits.index(visit_code)
        return _Cell(self._row_element, visit_index)

    @property
    def subject_row_element(self):
        return self._row_element

    @property
    def access_code_icon(self):
        return self._row_element.s(self._access_code_icon_css_selector)

    @property
    def access_code_is_generated(self):
        self.access_code_icon.should(have.attribute('title', 'Access code has been generated')).\
            should(have.css_class('has-subject-code')).should(have.css_property('color', 'rgba(238, 175, 0, 1)'))
        return self

    @property
    def access_code_is_not_generated(self):
        self.access_code_icon.should(have.attribute('title', 'Generate access code')).\
            should(have.no.css_class('has-subject-code'))
        return self

    def access_code_icon_click(self):
        self.access_code_icon.click()
        return self

    def expand(self):
        if 'opened' not in self.subject_row_element.get(query.attribute('class')):
            self.subject_row_element.click()
        return self

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.subject_row_element)
        return self


class _Cell:

    def __init__(self, row_element, visit_index):
        self._row_element = row_element
        self._visit_index = visit_index

        self._crosshair_css_selector = 'div.sub-line > div.sub-item:not(.subj-title)'
        self._issue_diary_icon_css_selector = 'button.diary-icon'
        self._add_button_css_selector = 'div.sub-line-expander-holder div.forms-holder div.txt2center dmx-ui-button'
        self._form_column_css_selector = 'div.form-column'
        self._forms_css_selector = 'dmx-edc-subject-matrix-item > div.form-item'

    @property
    def crosshair(self):
        return self._row_element.ss(self._crosshair_css_selector).filtered_by(be.visible)[self._visit_index]

    @property
    def issue_diary_icon(self):
        return self.crosshair.s(self._issue_diary_icon_css_selector)

    @property
    def add_btn(self):
        self._row_element.s(self._add_button_css_selector).wait_until(be.visible)
        return self._row_element.ss(self._add_button_css_selector).filtered_by(be.visible)[self._visit_index]
    
    @property
    def _forms(self):
        self._row_element.s(self._form_column_css_selector).wait_until(be.visible)
        elements = self._row_element.ss(self._form_column_css_selector).filtered_by(be.visible)[self._visit_index].\
            ss(self._forms_css_selector).filtered_by(be.visible)
        return [_Form(form_element) for form_element in elements]

    @property
    def forms_titles(self):
        return [form.title for form in self._forms]

    def form_with_title_exists(self, form_title):
        for form in self._forms:
            if form.title == form_title:
                return True
        return False

    def form_by_title(self, form_title):
        for form in self._forms:
            if form.title == form_title:
                return form
        exception = f"No form with title {form_title}"
        raise Exception(exception)

    def issue_diary_icon_click(self):
        self.issue_diary_icon.click()

    def click(self):
        self.crosshair.click()
        return self

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.crosshair)
        return self


class _Form:

    def __init__(self, form_element):
        self._element = form_element

        self._title_css_selector = 'div.matrix-item-header > span.form-title'

    @property
    def element(self):
        return self._element

    @property
    def title(self):
        return self._element.s(self._title_css_selector).text

    def open(self):
        self._element.click()

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.element)
        return self
