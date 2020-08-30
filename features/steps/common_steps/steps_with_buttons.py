import warnings

from behave import *
from selene import be, have, query

from page_elements.matrixcloud.button import ButtonByText, ButtonByTitle
from page_elements.epro.button import AndroidButtons

use_step_matcher('re')


@step(r"I (?:click|tap) on (?P<button_text>\D+) button")
def step_impl(context, button_text):
    if context.environment == 'web':
        ButtonByText(button_text).click()
    elif context.environment == 'android':
        AndroidButtons()[button_text].tap()

@step("I click on button with (?P<button_title>\D+) title")
def step_impl(context, button_title):
    if context.environment == 'web':
        ButtonByTitle(button_title).click()
    elif context.environment == 'android':
        raise Exception("Not applicable for android. Use 'click/tap on {button_text} button' step")


@step("I see (?:that )?(?P<button_text>\D+) button(?: exists)?")
def step_impl(context, button_text):
    button_element = ButtonByText(button_text) if context.environment == 'web' else AndroidButtons()[button_text]
    assert button_element.is_displayed, \
        f"\nExpected: {button_text} button exists" \
        f"\nActual: No {button_text} button\n"


@step("I see that (?P<button_text>\D+) button (?:is enabled|is active)")
def step_impl(context, button_text):
    button_element = ButtonByText(button_text) if context.environment == 'web' else AndroidButtons()[button_text]
    assert not button_element.is_disabled, \
        f"\nExpected: {button_text} button is enabled" \
        f"\nActual: No {button_text} button is disabled\n"


@step("I see that (?P<button_text>\D+) button (?:is disabled|is inactive)")
def step_impl(context, button_text):
    if context.environment == 'android':
        warnings.warn("Not sure if it works on android")  # Todo check on android
    button_element = ButtonByText(button_text) if context.environment == 'web' else AndroidButtons()[button_text]
    assert button_element.is_disabled, \
        f'\nExpected: {button_text} button is disabled' \
        f'\nActual: {button_text} button is enabled\n'


@step("I see that button with (?P<button_title>\D+) title (?:is enabled|is active)")
def step_impl(context, button_title):
    assert not ButtonByTitle(button_title).is_disabled, \
        f'\nExpected: Button with title {button_title} is enabled\n' \
        f'Actual: Button with title {button_title} is disabled'
    if context.environment == 'android':
        raise Exception("Not applicable for android. Use 'see {button_text} button' step")


@step("I see that button with (?P<button_title>\D+) title (?:is disabled|is inactive)")
def step_impl(context, button_title):
    assert ButtonByText(button_title).is_disabled, \
        f'\nExpected: Button with title {button_title} is disabled\n' \
        f'Actual: Button with title {button_title} is enabled'
    if context.environment == 'android':
        raise Exception("Not applicable for android. Use 'see {button_text} button' step")


@step("I see that (?P<button_title>\D+) button has (?P<text>.*) text")
def step_impl(context, button_title, text):
    if context.environment == 'web':
        raise Exception("Not implemented on web")
    elif context.environment == 'android':
        button_element = AndroidButtons()[button_title]
        assert button_element.matching(have.exact_text(text)), \
            f'\nExpected: Button with title {button_title} has {text} text\n' \
            f'Actual: Button with title {button_title} has {button_element.text} text'


@step("I take a screenshot of (?P<button_text>\D+) button")
def step_impl(context, button_text):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f' {button_text} button'
    button_element = ButtonByText(button_text) if context.environment == 'web' else AndroidButtons()[button_text]
    button_element.take_screenshot(img_title=img_title)


@step("I take a screenshot of button with (?P<button_title>\D+) title")
def step_impl(context, button_title):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f' {button_title} button'
    ButtonByText(button_title).take_screenshot(img_title=img_title)
    if context.environment == 'android':
        raise Exception("Not applicable for android. Use 'I take a screenshot of {button_text} button' step")
