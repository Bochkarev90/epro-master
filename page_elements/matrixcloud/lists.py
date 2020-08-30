from selene.api import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from helpers.helpers import S


class _BaseList(S):

    def __init__(self, ul_element: Element):
        self._ul_element = ul_element
        self._options_elements = self._ul_element.ss('li > a, span').filtered_by(be.visible)
        super().__init__(self._ul_element)

    def __contains__(self, item):
        return item in self._options

    @property
    def text(self):
        return ''

    @property
    def _options(self):
        return {option.get(query.text): option for option in self._options_elements}

    def choose_option(self, option_text):
        self._ul_element.s(by.text(option_text)).click()
        return self


class PopoverList(_BaseList):

    def __init__(self):
        self._ul_element = ss('div.sat-popover-container ul').filtered_by(be.visible).element(-1)
        super().__init__(self._ul_element)

    @property
    def description(self) -> str:
        return f"\nTOP POPOVER UL ELEMENT" \
               f"\nOptions: {', '.join(list(self._options.keys()))}"

    def close(self):
        ActionChains(browser.driver).send_keys(Keys.ESCAPE).perform()
        return self


class DataAutotestList(_BaseList):

    def __init__(self, data_autotest_id: str):
        self._ul_element = s(f'div[data-autotest-id="{data_autotest_id}"] > div > ul.option-items')
        super().__init__(self._ul_element)

    @property
    def description(self) -> str:
        return f"\nDATA AUTOTEST LIST ELEMENT" \
               f"\nOptions: {', '.join(list(self._options.keys()))}"

    def close(self):
        self().click()
        return self


class List:

    def __init__(self):
        self._ul_locator_css_selector = 'ul.subject-form-list'
        self._li_locator_css_selector = 'li.subject-form-item'

    @property
    def list_element(self):
        return ss(self._ul_locator_css_selector).element_by(be.visible)

    @property
    def list_options_elements(self):
        return self.list_element.ss(self._li_locator_css_selector).filtered_by(be.visible)

    def option_with_text_click(self, option_text):
        self.list_options_elements.element_by(have.exact_text(option_text)).click()
        return self
