from behave import *

from page_elements.matrixcloud.checkbox import Checkbox

use_step_matcher('re')


@step(r"I click on (?P<label>\D+) checkbox")
def step_impl(context, label):
    Checkbox(label).click()


@step(r"I (?P<action>mark|unmark) (?P<label>\D+) checkbox")
def step_impl(context, action, label):
    checkbox = Checkbox(label)
    if action == 'mark':
        checkbox.mark()
    elif action == 'unmark':
        checkbox.unmark()


@step(r"I see (?:that )?(?P<label>\D+) checkbox(?: exists)?")
def step_impl(context, label):
    assert Checkbox(label).is_displayed, \
        f'\nExpected: {label} checkbox exists\n' \
        f'Actual: No {label} checkbox in DOM'


@step(r"(?:I see that )?(?P<label>\D+) checkbox (?:is active|is enabled)")
def step_impl(context, label):
    assert not Checkbox(label).is_disabled, \
        f'\nExpected: {label} checkbox is enabled\n' \
        f'Actual: {label} checkbox is disabled'


@step(r"(?:I see that )?(?P<label>\D+) checkbox (?:is inactive|is disabled)")
def step_impl(context, label):
    assert Checkbox(label).is_disabled, \
        f'\nExpected: {label} checkbox is disabled\n' \
        f'Actual: {label} checkbox is enabled'


@step("(?:I see that )?(?P<label>\D+) checkbox is marked")
def step_impl(context, label):
    assert not Checkbox(label).is_blank, \
        f'\nExpected: {label} checkbox is marked\n' \
        f'Actual: {label} checkbox is unmarked'


@step(r"(?:I see that )?(?P<label>\D+) checkbox is unmarked")
def step_impl(context, label):
    assert Checkbox(label).is_blank, \
        f'\nExpected: {label} checkbox is unmarked\n' \
        f'Actual: {label} checkbox is marked'


@step(r"I take a screenshot of (?P<label>\D+) checkbox")
def step_impl(context, label):
    context.screen_num += 1
    img_title = f'{str(context.screen_num)}_{context.scenario.name}_{label}_checkbox'
    Checkbox(label).take_screenshot(img_title=img_title)
