import re
from functools import lru_cache

from selene.api import *


class FormsTree:

    def __init__(self):
        self._locator = s('ul.visits-list')
        self._visits = [_Visit(element) for element in self._locator.ss(by.xpath('./li')).filtered_by(be.visible)]

    def __str__(self):
        return '\n'.join([visit.title for visit in self._visits])

    def __call__(self):
        return self._locator

    def __getitem__(self, item):
        for visit in self._visits:
            if visit.title == item:
                return visit
        exception = f'No visit with {item} title'
        raise Exception(exception)

    @property
    def first_visit(self):
        return list(self._visits)[0]

    @property
    def last_visit(self):
        return list(self._visits)[-1]

    def visit_by_title(self, visit_title):
        return self[visit_title]


class _Visit:

    def __init__(self, element):
        self._locator = element
        self._title_locator = self._locator.s('span.visit-name')
        self._forms_ul_locator = self._locator.s('ul.forms-list')
        self._forms_li_locator = self._forms_ul_locator.ss(by.xpath('./li')).filtered_by(be.visible)
        self._forms = (_TreeForm(element) for element in self._forms_li_locator)

    def __str__(self):
        return self.title

    def __call__(self):
        return self._locator

    def __getitem__(self, item):
        for form in self._forms:
            if form.title == item:
                return form
        exception = f'No form with {item} title'
        raise Exception(exception)

    @property
    def title(self) -> str:
        return self._title_locator.get(query.attribute('title'))

    @property
    def is_expanded(self) -> bool:
        return 'forms-list-opened' in self._forms_ul_locator.get(query.attribute('class'))

    @property
    def first_form(self):
        return list(self._forms)[0]

    @property
    def last_form(self):
        return list(self._forms)[-1]

    def form_by_title(self, form_title):
        return self[form_title]

    def click(self):
        self._locator.click()
        return self

    def expand(self):
        if self.is_expanded:
            self._locator.click()

    def collapse(self):
        if not self.is_expanded:
            self._locator.click()


class _TreeForm:

    def __init__(self, element):
        self._locator = element
        self._title_locator = self._locator.s('div.form-title-block')
        self._status_icon_locator = self._locator.s('i.status-icon')

    def __str__(self):
        presentation = f"{self.status.title()} form with '{self.title}' title"
        if self.repeat_key:
            presentation += f" with '{self.repeat_key}' repeat key"
        return presentation

    def __call__(self):
        return self._locator

    @property
    @lru_cache()
    def _text(self) -> tuple:
        """
        (1) Smoke Form Title -> Smoke Form Title, 1
        Smoke Form Title -> Smoke Form Title
        """
        text = self._title_locator.get(query.text)
        title, *repeat_key = tuple(reversed(re.split(r"\((\d+)\) ", text, maxsplit=1)))
        repeat_key = repeat_key[0] if repeat_key else None
        return title, repeat_key

    @property
    def repeat_key(self) -> str:
        return self._text[1]

    @property
    def title(self) -> str:
        return self._text[0]

    @property
    def status(self) -> str:
        status_icon_title = self._status_icon_locator.get(query.attribute('title'))
        if status_icon_title == 'Add Mandatory Form':
            return 'new'
        elif status_icon_title == 'Edit Form':
            return 'saved'
        elif status_icon_title == 'Approved Form':
            return 'approved'
        elif status_icon_title == 'Verified Form':
            return 'verified'
        elif status_icon_title == 'Locked Form':
            return 'locked'
        exception = f"What am I doing here?! '{status_icon_title}' is unexpected"
        raise Exception(exception)

    @property
    def is_active(self) -> bool:
        return 'form-active' in self._locator.get(query.attribute('class'))

    def open(self):
        self._locator.click()
        return self
