import time
from typing import Dict

from selene.api import *
from selenium.webdriver.common.keys import Keys

from helpers.helpers import take_element_screenshot


class TimeFields:

    def __init__(self):
        self._date_time_input_css_selector = 'span.ui-calendar > dmx-ui-input > div > input'

    def __getitem__(self, item):
        return [_TimeField(element)
                for element in ss(self._date_time_input_css_selector).filtered_by(be.visible)][item]


class _TimeField:

    def __init__(self, element):
        self._element = element

    def __call__(self):
        return self._element

    @property
    def input_field_element(self):
        return self._element

    # TODO
    def is_disabled(self) -> bool:
        raise Exception("Not implemented")

    # TODO
    def is_enabled(self) -> bool:
        raise Exception("Not implemented")

    def click(self):
        self._element.click()

    def type(self, value):
        self._element.clear().type(value.strip() + Keys.TAB)

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self._element)
        return self
