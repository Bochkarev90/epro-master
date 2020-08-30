from selene.api import *

from page_objects.edc_form import EDCForm
from page_objects.edc_forms_tree import FormsTree


class EDC:

    def __init__(self):
        self._subject_title_element = s('h1.subject-title')

    @property
    def current_subject_title(self):
        subject_title = self._subject_title_element.get(query.text)
        subject_title_numbers = slice(subject_title.find(': ') + 2)
        return subject_title[subject_title_numbers]

    @property
    def forms_tree(self):
        return FormsTree()

    @property
    def edc_form(self):
        return EDCForm()
