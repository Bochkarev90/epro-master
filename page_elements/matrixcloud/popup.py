from selene.api import ss, be, have, query


class Popup:

    def __init__(self, title=''):
        popups = ss(f'//span[contains(@class, "popup-title")]').filtered_by(be.visible)
        self._locator = popups.element_by(have.exact_text(title)) if title else popups.element(-1)

    def __call__(self):
        return self._locator

    # @property
    # def top_popup(self):
    #     return ss(f'//span[contains(@class, "popup-title")]').element(-1)

    # @property
    # def popup_by_title(self):
    #     return s(f'//span[contains(@class, "popup-title") and text()="{self._title}"]')

    @property
    def text(self):
        return self._locator.get(query.text)

    def disappears(self):
        return self._locator.should(be.not_.visible)

    def close(self):
        self._locator.s('./following-sibling::span[contains(@class, "popup-close")]').click()
