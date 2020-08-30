from behave import *
from selene.api import *

from driver_management.drivers import Drivers
from page_elements.epro.page import Page

use_step_matcher('re')


@given("(?P<driver>Web|Browser|App|Android) is (?:started|loaded)")
@given("I (?:start|load) (?:the )?(?P<driver>web|browser|app|android)")
@step("I (?:switch|return) to (?:the )?(?P<driver>web|browser|app|android)")
def step_impl(context, driver):
    if driver.lower() in ['web', 'browser']:
        context.environment = 'web'
        browser.config.driver = Drivers().webdriver
    elif driver.lower() in ['app', 'android']:
        context.environment = 'android'
        browser.config.driver = Drivers().android_driver


@step("I switch to (?P<webview_or_native>webview|native)")
def step_impl(context, webview_or_native):
    if context.environment == 'web':
        raise Exception("Not applicable for web")
    Page().wait_for_page_loaded()
    contexts = browser.driver.contexts
    if webview_or_native == 'webview':
        browser.driver.switch_to.context(contexts[-1])
    elif webview_or_native == 'native':
        browser.driver.switch_to.context(contexts[0])


@step("I take a screenshot")
def step_impl(context):
    context.screen_num += 1
    filename = 'screenshots/' + str(context.screen_num) + '_' + context.scenario.name + '.png'
    browser.save_screenshot(file=filename)


@step("I hide keyboard")
def step_impl(context):
    browser.driver.hide_keyboard()
