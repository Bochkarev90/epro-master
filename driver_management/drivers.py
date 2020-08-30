from webdriver_manager.chrome import ChromeDriverManager

from config import HOST
from driver_management.driver import WebDriver, AndroidDriver
from threading import Thread


class _DriversMeta(type):

    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Drivers(metaclass=_DriversMeta):

    _webdriver_thread = None
    _web = None
    _android_driver_thread = None
    _android = None

    @property
    def webdriver(self):
        if not self._web:
            self.start_web()
        self._webdriver_thread.join()
        return self._web.driver

    @property
    def android_driver(self):
        if not self._android:
            self.start_android()
        self._android_driver_thread.join()
        return self._android.driver

    def start_web(self):
        web = WebDriver()
        self._webdriver_thread = Thread(target=web.start)
        self._webdriver_thread.start()
        self._web = web
        return self

    def start_android(self):
        android = AndroidDriver()
        self._android_driver_thread = Thread(target=android.start)
        self._android_driver_thread.start()
        self._android = android
        return self

    def clean_web(self):
        if self._web:
            self._web.driver.execute_script('window.localStorage.clear();')
            self._web.driver.execute_script('window.sessionStorage.clear();')
            self._web.driver.delete_all_cookies()
            self._web.driver.get(HOST)
        return self

    def quit_web(self):
        self._web.driver.close()
        return self

    def quit_android(self):
        if self._android:
            self._android.driver.quit()
            self._android = None
        return self
