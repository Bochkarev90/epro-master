from selene.api import *

from helpers.helpers import S


class ButtonByText(S):

    def __init__(self, button_text):
        self.button_text = button_text
        _selene_element = ss(by.xpath(f'//span[translate'
                                      f'(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")'
                                      f'="{self.button_text.lower()}"]/'
                                      f'parent::button')).filtered_by(be.visible).element(-1)
        super().__init__(_selene_element)

    @property
    def description(self) -> str:
        return f"\nBUTTON ELEMENT FOUND BY TEXT" \
               f"\nSearch text: {self.button_text}" \
               f"\nReal text: {self.get(query.text)}"


class ButtonByTitle(S):

    def __init__(self, button_title):
        self.button_title = button_title
        _selene_element = ss(f'dmx-ui-button[title="{self.button_title}"] > button').filtered_by(be.visible).element(-1)
        super().__init__(_selene_element)

    @property
    def description(self) -> str:
        return f"\nBUTTON ELEMENT FOUND BY TITLE" \
               f"\nSearch title: {self.button_title}" \
               f"\nReal title: {self.get(query.attribute('title'))}"
