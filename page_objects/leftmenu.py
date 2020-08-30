from selene.api import *


class LeftMenu:

    def __init__(self):
        self._locator = s('ul.main-menu')
        self._menu_locator = 'li.menu-list'

    def __str__(self):
        return ', '.join([menu.text for menu in self.menus])

    def __call__(self):
        return self._locator

    def __getitem__(self, item):
        for menu in self.menus:
            if menu.text == item:
                return menu
        exception = f"No visible menu with {item} title. These menus are visible {str(self)}"
        raise Exception(exception)

    def __contains__(self, item):
        return item in [menu.text for menu in self.menus]

    @property
    def toggle_button(self):
        return s('button.toggler > em.toggler-icon')

    @property
    def menus(self):
        return (MainMenu(element) for element in ss(self._menu_locator).filtered_by(be.visible))

    @property
    def is_expanded(self):
        return True if 'icon-chevrons-left' in self.toggle_button.get(query.attribute('class')) else False

    def expand(self):
        if not self.is_expanded:
            self.toggle_button.click()
        return self

    def collapse(self):
        if self.is_expanded:
            self.toggle_button.click()
        return self

    def menu_by_title(self, menu_title):
        return self[menu_title]


class MainMenu:

    def __init__(self, element):
        self._locator = element
        self._expand_icon_element = self._locator.s('span.icon-arrow')
        self._span_with_text_element = self._locator.s('a > span.item-name')

    def __call__(self):
        return self._locator

    @property
    def text(self):
        return self._span_with_text_element.get(query.text)

    @property
    def is_expanded(self):
        return True if 'icon-up' in self._expand_icon_element.get(query.attribute('class')) else False

    def expand(self):
        if not self.is_expanded:
            self._expand_icon_element.click()
        return self

    def collapse(self):
        if self.is_expanded:
            self._expand_icon_element.click()
        return self

    def click(self):
        self._locator.click()
        return self
