import os
import string
import random
import warnings
from typing import Collection

from appium.webdriver.common.touch_action import TouchAction
from selene import be, query
from selene.api import browser

import cv2
from selene.core.entity import Element


class S:

    def __init__(self, selene_element):
        self._locator = selene_element
        self._description = None

    def __call__(self) -> Element:
        return self._locator

    def __getattr__(self, item):
        return getattr(self(), item)

    def __str__(self):
        return self.description + self.condition

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def is_displayed(self) -> bool:
        return self.matching(be.existing)

    @property
    def is_visible(self) -> bool:
        return self.matching(be.visible)

    @property
    def is_disabled(self) -> bool:
        return self.matching(be.disabled)

    @property
    def is_blank(self) -> bool:
        return self.matching(be.blank)

    @property
    def text(self):
        return self.get(query.text)

    @property
    def condition(self):
        return f"\nClasses: {self.get(query.attribute('class'))}" \
               f"\nText: {self.text}" \
               f"\nExisting/In DOM/Present/!Absent: {self.is_displayed}" \
               f"\nVisible/!Hidden: {self.is_visible}" \
               f"\nDisabled/!Enabled/!Clickable: {self.is_disabled}" \
               f"\nBlank: {self.is_blank}\n"

    def tap(self):
        self().wait_until(be.visible)
        actions = TouchAction(browser.driver)
        actions.tap(self()())
        actions.perform()
        return self

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self())
        return self


def random_char(y):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(y))


def translate(title):
    return title.strip().lower().replace(' ', '_')


def take_element_screenshot(img_title, element):
    screenshot_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"..\\screenshots\\{img_title}.png"))
    browser.save_screenshot(screenshot_path)
    src_img = cv2.imread(screenshot_path)
    pt1 = (element.location['x'] - 10, element.location['y'] - 10)
    pt2 = (element.location['x'] + element.size['width'] + 7, element.location['y'] + element.size['height'] + 7)
    thickness = 6
    color = (0, 0, 255)
    output_image = cv2.rectangle(img=src_img, pt1=pt1, pt2=pt2, color=color, thickness=thickness)
    cv2.imwrite(screenshot_path, output_image)
    return screenshot_path


def warning_a_lot_of_labels_were_found(label_text: str, elements: Collection):
    warning_message = f'These labels with text {label_text} were found: {[element.text for element in elements]}.' \
                      f'Was chosen last one'
    warnings.warn(warning_message)


def wait_for_angular():
    angular_loaded = """
            callback = arguments[arguments.length - 1];
            try {
                var testabilities = window.getAllAngularTestabilities();
                var count = testabilities.length;
                var decrement = function() {
                count--;
                if (count === 0) {
                  callback('completed');
                    }
                };
                testabilities.forEach(function(testability) {
                    testability.whenStable(decrement);
                });
             } catch (err) {
                callback(err.message);
             }
            """
    browser.driver.set_script_timeout(30)
    browser.driver.execute_async_script(angular_loaded)


if __name__ == '__main__':
    print(translate('asd_asdfe '))
