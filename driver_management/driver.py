from selenium import webdriver
from appium import webdriver as appium_driver
from webdriver_manager.chrome import ChromeDriverManager

from config import HOST, ANDROID_VERSION


class AndroidDriver:

    def __init__(self):
        self._desired_caps = {
            "browserName": "",
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": "Android Emulator",
            # "udid": f"emulator",
            "app": f"C:/Users/mbochkarev/Desktop/ePRO_{ANDROID_VERSION}_test-signed.apk",
            "appPackage": "com.dmmatrix.epro.test",
            "appWaitActivity": "com.dmmatrix.epro.presentation.view.activity.AuthorizationActivity",
            "newCommandTimeout": 6000
        }
        self._driver = None

    @property
    def driver(self):
        return self._driver

    def start(self):
        self._driver = appium_driver.Remote("http://localhost:4723/wd/hub", self._desired_caps)


class WebDriver:

    def __init__(self):
        self._chrome_options = webdriver.ChromeOptions()
        self._driver = None
        # chrome_options.add_argument('--headless')

    @property
    def driver(self):
        return self._driver

    def start(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  options=self._chrome_options)
        driver.maximize_window()
        driver.get(HOST)
        self._driver = driver
