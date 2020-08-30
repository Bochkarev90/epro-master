from appium.webdriver.common.touch_action import TouchAction
from selene.api import *

from helpers.helpers import take_element_screenshot


class BaseEproElement:

    def __init__(self, element):
        self._element = element

    @property
    def element(self):
        return self._element

    @property
    def text(self):
        return self.element.get(query.text)

    def has_text(self, text):
        self.element.should(have.exact_text(text))
        return self

    def click(self):
        self.element.click()
        return self

    def tap(self):
        self.element.wait_until(be.visible)
        actions = TouchAction(browser.driver)
        actions.tap(self.element())
        actions.perform()
        return self

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.element)
        return self

    def is_displayed(self):
        self.element.should(be.visible)
        return self
