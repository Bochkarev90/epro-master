from selene.api import s, query

from helpers.helpers import take_element_screenshot


class SpecialFields:

    @property
    def access_code_field(self):
        return _AccessCodeField()


class _AccessCodeField:

    def __init__(self):
        self._css_selector = 'div.access-code-popup-container > div.main-info h2'

    @property
    def element(self):
        return s(self._css_selector)

    @property
    def access_code(self):
        return self.element.get(query.text)

    def click(self):
        self.element.click()
        return self

    def take_screenshot(self, img_title):
        return take_element_screenshot(img_title=img_title, element=self.element)
