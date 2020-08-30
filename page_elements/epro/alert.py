from selene.api import *


class Alert:

    def __init__(self):
        self._locator = s(by.id('android:id/message'))

    def __call__(self):
        return self._locator

    @property
    def text(self):
        return self._locator.get(query.text)


class PermissionAlert:

    def __init__(self):
        self._locator = s(by.id('com.android.packageinstaller:id/permission_message'))

    def __call__(self):
        return self._locator

    @property
    def text(self):
        return self._locator.get(query.text)
