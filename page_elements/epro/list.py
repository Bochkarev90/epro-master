from page_elements.epro.baseelement import BaseEproElement
from selene.api import *


class List(BaseEproElement):
    
    def __init__(self):
        self._list_options_locators_xpath = './/android.widget.TextView'
        super().__init__(s(by.id('com.dmmatrix.epro.test:id/list')))
        self.element.wait_until(be.visible)

    def __getitem__(self, item):
        return self.options[item]

    @property
    def options(self):
        return [BaseEproElement(element) for element in self.element.ss(by.xpath(self._list_options_locators_xpath))]

    def option_by_text(self, text):
        for option in self.options:
            if option.text.lower() == text.lower():
                return option
        exception = f"No option with {text} text"
        raise Exception(exception)
