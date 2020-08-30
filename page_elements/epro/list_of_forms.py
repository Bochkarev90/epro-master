from selene.core.exceptions import TimeoutException

from page_elements.epro.baseelement import BaseEproElement
from selene.api import *


class ListOfForms(BaseEproElement):

    def __init__(self):
        self._forms_locators_xpath = './/android.view.ViewGroup/android.widget.FrameLayout//android.view.ViewGroup'
        super().__init__(s(by.id('com.dmmatrix.epro.test:id/eventsRecyclerView')))
        self.element.wait_until(be.visible)

    @property
    def forms(self):
        self.element.s(by.xpath(self._forms_locators_xpath)).wait_until(be.visible)
        return (_Form(form) for form in self.element.ss(by.xpath(self._forms_locators_xpath)).filtered_by(be.visible))

    @property
    def forms_titles(self):
        return [form.title for form in self.forms]

    def form_by_title(self, form_title):
        for form in self.forms:
            if form.title == form_title:
                return form
        exception = f"No form with {form_title} title"
        raise Exception(exception)


class _Form(BaseEproElement):

    def __init__(self, element):
        super().__init__(element)
        self._title_locator = 'com.dmmatrix.epro.test:id/title'
        self._time_locator = 'com.dmmatrix.epro.test:id/time'
        self._status_locator = 'com.dmmatrix.epro.test:id/eventStatus'

    @property
    def title(self):
        return self.element.s(by.id(self._title_locator)).get(query.text)

    @property
    def time(self):
        return self.element.s(by.id(self._time_locator)).get(query.text)

    @property
    def status(self):
        try:
            return self.element.s(by.id(self._status_locator)).get(query.text)
        except TimeoutException:
            return ''
