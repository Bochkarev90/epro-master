from abc import abstractmethod

from selene.api import *

from helpers.helpers import wait_for_angular, S
from page_elements.matrixcloud.lists import PopoverList, DataAutotestList


class _BaseField(S):

    def __init__(self, label):
        self.label = label
        self._label = label if label.endswith(':') else label + ':'
        self._label_element = ss(by.text(self._label)).element(-1)
        self._input_element = self.input_element
        super().__init__(self._input_element)

    def __contains__(self, item: str):
        return item in self.text

    @property
    def description(self) -> str:
        return f"\n{self.__class__.__name__.upper()} FIELD ELEMENT FOUND BY LABEL" \
               f"\nSearch label: {self.label}" \
               f"\nReal label: {self._label_element.get(query.text)}"

    @property
    @abstractmethod
    def input_element(self) -> Element:
        raise Exception('Need to implement this method')


class Input(_BaseField):

    def __init__(self, label):
        super().__init__(label)

    @property
    def input_element(self):
        return self._label_element.s(by.xpath('./following-sibling::input'))

    @property
    def description(self) -> str:
        return f"\nINPUT ELEMENT FOUND BY LABEL" \
               f"\nSearch label: {self.label}" \
               f"\nReal label: {self._label_element.get(query.text)}\n"


class Selector(_BaseField):

    def __init__(self, label):
        super().__init__(label)
        self._disabled_element = self._label_element.s(by.xpath(
            './parent::div[contains(@class, "ui-selector-holder")]'))
        self._icon_up_or_down_element = self._input_element.s('span.ui-selector-icon')

    @property
    def input_element(self):
        return self._label_element.s(by.xpath(
            './following-sibling::div[contains(@class, "ui-selector")]'))

    @property
    def is_disabled(self) -> bool:
        return self._disabled_element.matching(have.css_class('ui-selector-disabled'))

    @property
    def is_blank(self) -> bool:
        return not bool(self.text)
    
    @property
    def _is_expanded(self) -> bool:
        return self._icon_up_or_down_element.matching(have.css_class('pi-angle-up'))

    def expand(self) -> PopoverList:
        if not self._is_expanded:
            self._input_element.click()
            wait_for_angular()
        return PopoverList()


class Pseudo(_BaseField):

    def __init__(self, label):
        super().__init__(label)
        self._disabled_element = self._label_element.s(by.xpath('./parent::div'))
        self._data_autotest_id_element = self.input_element.s('span.pseudo-input-value')
        self._icon_up_or_down_element = self._input_element.s('span.icon')

    @property
    def input_element(self):
        return self._label_element.s(by.xpath('./following::div[contains(@class, "pseudo-input")]'))

    @property
    def is_disabled(self) -> bool:
        return self._disabled_element.matching(have.css_class('dmx-ui-dropdown-disabled'))

    @property
    def is_blank(self) -> bool:
        return not bool(self.text)

    @property
    def _data_autotest_id(self):
        return self._data_autotest_id_element.get(query.attribute('data-autotest-dropdownlist'))

    @property
    def _is_expanded(self) -> bool:
        return self._icon_up_or_down_element.matching(have.css_class('icon-up'))

    def expand(self) -> DataAutotestList:
        if not self._is_expanded:
            self._input_element.click()
            wait_for_angular()
        return DataAutotestList(self._data_autotest_id)


class MultiSelect(_BaseField):

    def __init__(self, label):
        super().__init__(label)
        self._disabled_element = self._label_element.s(by.xpath('./parent::div'))
        self._chosen_options_elements = self.input_element.ss('ul > li.multiselect-item').filtered_by(be.visible)

    def __contains__(self, item):
        return item in self._chosen_options

    @property
    def description(self) -> str:
        return super().description + f"\nChosen options: {', '.join(list(self._chosen_options.keys()))}"

    @property
    def input_element(self):
        return self._label_element.s(by.xpath('./following-sibling::div[contains(@class, "multiselect-holder")]'))

    @property
    def is_disabled(self) -> bool:
        return self._disabled_element.matching(have.css_class('dmx-ui-dropdown-disabled'))

    @property
    def is_blank(self) -> bool:
        return bool(self._chosen_options_elements)

    @property
    def _data_autotest_id(self):
        return self.input_element.get(query.attribute('data-autotest-dropdownlist'))

    @property
    def _chosen_options(self) -> dict:
        return {option.get(query.text): option for option in self._chosen_options_elements}

    @property
    def _is_expanded(self):
        return DataAutotestList(self._data_autotest_id).is_visible

    def delete_option(self, option_title):
        self._chosen_options[option_title].s(by.xpath('./span[contains(@class, "icon-x")]')).click()
        return self

    def expand(self) -> DataAutotestList:
        if not self._is_expanded:
            self._input_element.click()
            wait_for_angular()
        return DataAutotestList(self._data_autotest_id)


class FieldByLabel:

    def __init__(self, label):
        self.label = label
        self._label = label if label.endswith(':') else label + ':'
        self._label_element = ss(by.text(self._label)).filtered_by(be.visible).element(-1)
        self._label_classes = self._label_element.get(query.attribute('class'))
        self._classes_of_next_element = self._label_element.s(by.xpath(
            './/following-sibling::*')).get(query.attribute('class'))

    def __getattr__(self, item):
        return getattr(self._element, item)

    def __contains__(self, item):
        return item in self._element

    def __str__(self):
        return self._element.__str__()

    @property
    def _element(self):
        if 'ui-inputtext-label' in self._label_classes:
            return Input(self.label)
        elif 'dmx-ui-dropdown-label' in self._label_classes:
            if 'pseudo-input' in self._classes_of_next_element:
                return Pseudo(self.label)
            elif 'multiselect-holder' in self._classes_of_next_element:
                return MultiSelect(self.label)
        elif 'ui-selector-label' in self._label_classes:
            return Selector(self.label)
        elif 'line-label' in self._label_classes:
            return Pseudo(self.label)
        elif 'label-like' in self._label_classes:
            return Pseudo(self.label)
        else:
            exception = f'Hm smth new... {self._classes_of_next_element}, {self._label_element.get(query.text)}'
            raise Exception(exception)
