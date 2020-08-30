import re
from functools import lru_cache

from selene.api import *
from selene.core.exceptions import TimeoutException

from page_elements.matrixcloud.button import ButtonByText, ButtonByTitle


class EDCForm:

    def __init__(self):
        self._header_locator = s('div.edc-form-header-container')
        self._title_locator = self._header_locator.s('h1.form-name')
        self._status_icon_locator = self._header_locator.s('i.status-icon')
        self._delete_btn_locator = self._header_locator.s('span.delete-form-btn-icon')
        self._save_btn_locator = self._header_locator.s('span.delete-form-btn-icon')
        self._approve_btn_locator = self._header_locator.s('span.delete-form-btn-icon')
        self._verify_btn_locator = self._header_locator.s('span.delete-form-btn-icon')
        self._lock_btn_locator = self._header_locator.s('span.delete-form-btn-icon')

    def __str__(self):
        presentation = f"{self.status.title()} form with {self.title} title"
        if self.repeat_key:
            presentation += f" #{self.repeat_key}"
        return presentation
        
    @property
    @lru_cache()
    def title_text(self) -> tuple:
        """
        Smoke Form Title #1 -> Smoke Form Title, 1
        Smoke Form Title -> Smoke Form Title
        """
        title_text = self._title_locator.get(query.text)
        title, *repeat_key = tuple(re.split(r" #(\d+)", title_text, maxsplit=1))
        repeat_key = repeat_key[0] if repeat_key else None
        return title, repeat_key

    @property
    def title(self) -> str:
        return self.title_text[0]

    @property
    def repeat_key(self) -> str:
        return self.title_text[-1]

    @property
    def status(self):
        status_icon_classes = self._status_icon_locator.get(query.attribute('class'))
        if 'locked-form' in status_icon_classes:
            return 'locked'
        elif 'icon-verify' in status_icon_classes:
            return 'verified'
        elif 'icon-edit' in status_icon_classes:
            return 'saved'
        elif 'approve-form' in status_icon_classes:
            return 'approved'
        elif 'create-form' in status_icon_classes:
            return 'new'
        exception = f"'What am I doing here?! No expected class in '{status_icon_classes}'"
        raise Exception(exception)

    @property
    def sections(self):
        return Sections()

    @property
    def save_button(self):
        return ButtonByText('Save')

    @property
    def cancel_button(self):
        return ButtonByText('Cancel')

    @property
    def approve_button(self):
        return ButtonByText('Approve')

    @property
    def delete_icon(self):
        return ButtonByTitle('Delete Form')


class Sections:

    def __init__(self):
        self._sections_locator = 'div.form-items-container'
        self._sections = (Section(section_element) for section_element in
                          ss(self._sections_locator).filtered_by(be.visible))

    def __getitem__(self, item):
        for section in self._sections:
            if section.title == item:
                return section
        exception = f'No section with {item} title'
        raise Exception(exception)

    def __repr__(self):
        return [section.title for section in self._sections]

    @property
    def first(self):
        return list(self._sections)[0]

    @property
    def last(self):
        return list(self._sections)[-1]


class Section:

    def __init__(self, element):
        self._element = element
        self._title_locator = 'ui-accordion-header-wrapper'

    @property
    def title(self):
        return self._element.s(self._title_locator).get(query.text)
