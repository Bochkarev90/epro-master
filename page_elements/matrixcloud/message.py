from selene.api import *


class Message:

    def __init__(self):
        self._locator = s('div.system-block h2.header-title')

    def __call__(self):
        return self._locator

    @property
    def text(self):
        return self._locator.get(query.text)
