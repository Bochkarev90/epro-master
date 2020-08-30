from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class WaitingElement(object):

    def __init__(self, driver, element_id):
        self._driver = driver
        self._locator = element_id

    def _finder(self):
        return self._driver.find_element_by_id(self._locator)

    def __getattr__(self, item):
        WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, self._locator)))
        return getattr(self._finder(), item)

    def tap(self):
        WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, self._locator)))
        actions = TouchAction(self._driver)
        actions.tap(self._finder())
        actions.perform()

    def has_text(self, text):
        try:
            WebDriverWait(self._driver, 5).until(EC.text_to_be_present_in_element((By.ID, self._locator), text))
            return self
        except TimeoutException:  # Todo Add all possible Exceptions
            return False


def s(driver, css_selector):
    return WaitingElement(driver, css_selector)


if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "deviceName": "Android Emulator",
        "app": "C:/Users/mbochkarev/Desktop/ePRO_1.0.8_build_4_test-signed.apk",
        "udid": "emulator-5554",
        "appPackage": "com.dmmatrix.epro.test",
        "appWaitActivity": "com.dmmatrix.epro.presentation.view.activity.AuthorizationActivity",
        "isHeadless": True
    }
    context_driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    s(context_driver, "com.dmmatrix.epro.test:id/etAccessCode").send_keys("asdkljhqlwj")
    s(context_driver, "com.dmmatrix.epro.test:id/etPassword").send_keys("somepwd")
    print(s(context_driver, "com.dmmatrix.epro.test:id/btnLogin").is_visible())
