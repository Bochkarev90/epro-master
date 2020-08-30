from behave import *
from selene.api import s, by
from selene.core.exceptions import TimeoutException

from page_elements.epro.alert import Alert, PermissionAlert
from page_elements.epro.button import AndroidButtons
from page_elements.matrixcloud.button import ButtonByText
from page_elements.matrixcloud.popup import Popup
from page_elements.matrixcloud.message import Message

use_step_matcher('re')


@then("I see error message with (?P<text>.*) text(?P<close> and close it)?")
def i_see_error_message_with_text(context, text, close):
    expected = text
    actual = Message().text if context.environment == 'web' else Alert().text
    assert expected == actual, f"Expected: Error message with {expected} text\n" \
                               f"Actual: Error message with {actual} text"

    if close:
        ButtonByText('CLOSE').click() if context.environment == 'web' else AndroidButtons()['OK'].tap()


@step("I see permission alert with (?P<text>.*) text")
def i_see_error_message_with_text(context, text):
    if context.environment == 'web':
        raise Exception("Not applicable for web")
    expected = text
    actual = PermissionAlert().text
    assert expected == actual, f"Expected: Permission alert with {expected} text\n" \
                               f"Actual: Permission alert with {actual} text"


# region POPUP STEPS
@then("(?:I see that )?(?P<popup_title>\D+) popup disappears")
def step_impl(context, popup_title):
    if context.environment == 'android':
        raise Exception("Not applicable for android")
    Popup(popup_title).disappears()


@then("I see (?P<popup_title>\D+) popup")
def step_impl(context, popup_title):
    if context.environment == 'android':
        raise Exception("Not applicable for android")
    expected = popup_title
    actual = Popup().text
    assert expected == actual, f"Expected: Popup has {expected} text\n" \
                               f"Actual: Popup has {actual} text"


@step("I close (?:this|top) popup")
def step_impl(context):
    if context.environment == 'android':
        raise Exception("Not applicable for android")
    Popup().close()


@step("I close (?P<popup_title>\D+) popup")
def step_impl(context, popup_title):
    if context.environment == 'android':
        raise Exception("Not applicable for android")
    Popup(popup_title).close()


@given("I close system alert")
def step_impl(context):
    if context.environment == 'android':
        raise Exception("Not applicable for android")
    try:
        s(by.xpath('//span[contains(text(), "Yes")]')).click()
    except TimeoutException:
        pass
# endregion
