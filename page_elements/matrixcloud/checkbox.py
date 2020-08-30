from selene.api import *

from helpers.helpers import S


class Checkbox(S):

    def __init__(self, label: str):
        self._label = label
        self._label_element = s(by.text(label))
        self._checkbox_holder = self._label_element.s(by.xpath(
            './preceding-sibling::div/parent::div[@class="ui-checkbox-holder"]'))
        self._disabled_element = self._checkbox_holder.s('div.ui-chkbox-box')
        self._marked_element = self._disabled_element.s('span.ui-chkbox-icon')
        super().__init__(self._disabled_element)

    @property
    def description(self) -> str:
        return f"\nCHECKBOX ELEMENT FOUND BY LABEL\n" \
               f"Search label: {self._label}\n" \
               f"Real label: {self._label_element.get(query.text)}\n"

    @property
    def is_disabled(self) -> bool:
        return self._disabled_element.matching(have.css_class('ui-state-disabled'))

    @property
    def is_blank(self) -> bool:
        return self._marked_element.matching(have.no.css_class('icon-checkbox-active'))

    def mark(self):
        if self.is_blank:
            self.click()
        return self

    def unmark(self):
        if not self.is_blank:
            self.click()
        return self


if __name__ == '__main__':
    from selene.api import browser
    import time
    from page_elements.matrixcloud.field import FieldByLabel
    from page_elements.matrixcloud.button import ButtonByText, ButtonByTitle
    from page_objects.leftmenu import LeftMenu

    browser.open('https://dmxtest.dm-matrix.com/')
    browser.config.hold_browser_open = True
    browser.config.start_maximized = True
    browser.open_url('https://dmxtest.dm-matrix.com/client/login')
    FieldByLabel('Email').field.clear().type('crfdesigner@behave.test')
    FieldByLabel('Password').field.clear().type('Somepwd123')
    ButtonByText('Login').click()
    LeftMenu().menu_by_title('CRF designer').expand()
    LeftMenu().menu_by_title('CRF').click()
    ButtonByTitle('Go to visit structure').click()
    ButtonByText('CRF DESIGNING').click()
    ButtonByText('ADD FORM').click()
    print(Checkbox('is repeated'))
    print(Checkbox('is mandatory'))
    # assert Checkbox('is repeated').is_enabled()
    # assert Checkbox('is repeated').is_unmarked()
    # assert Checkbox('is mandatory').is_enabled()
    # assert Checkbox('is mandatory').is_unmarked()
    FieldByLabel('Form Type').field.choose_option('ePRO')
    print(Checkbox('is repeated'))
    print(Checkbox('is mandatory'))
    # assert Checkbox('is repeated').is_disabled()
    # assert Checkbox('is repeated').is_marked()
    # assert Checkbox('is mandatory').is_disabled()
    # assert Checkbox('is mandatory').is_unmarked()
    FieldByLabel('Form Type').field.choose_option('Common')
    print(Checkbox('is repeated'))
    print(Checkbox('is mandatory'))
    # assert Checkbox('is repeated').is_enabled()
    # assert Checkbox('is repeated').is_unmarked()
    # assert Checkbox('is mandatory').is_enabled()
    # assert Checkbox('is mandatory').is_unmarked()

    time.sleep(30)
