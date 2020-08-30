import os

from appium.webdriver.appium_service import AppiumService


def start_emulator():
    os.system("emulator -avd Pixel_2_API_28 &")


def kill_drivers():
    os.system('taskkill.exe /IM "chromedriver.exe" /F')


def start_appium(with_executable_path=False):
    AppiumService().start()
    if with_executable_path:
        os.system("appium --chromedriver-executable D:\pythonProjects\wow\chromedriver.exe &")
    else:
        os.system("appium &")
    AppiumService().stop()


if __name__ == '__main__':
    kill_drivers()
    start_emulator()
    # start_appium(with_executable_path=True)
