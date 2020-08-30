from behave import *
from selene.core.exceptions import TimeoutException

from helpers.helpers import random_char
from page_elements.epro.field import Field
from page_elements.matrixcloud.field import FieldByLabel

use_step_matcher('re')


# TODO Should it be here?
@step("I put this access code in access code field")
def step_impl(context):
    if context.environment == 'web':
        raise Exception("Not applicable for web")
    Field()['access_code'].send_keys(context.access_code)


@step("I read about (?P<label>\D+) field")
def step_impl(context, label):
    print(FieldByLabel(label))


@step(r"I put (?P<keys>.*) in (?P<label>\D+) field")
def step_impl(context, keys, label):
    if context.environment == 'web':
        FieldByLabel(label).clear().type(keys)
    elif context.environment == 'android':
        if keys.lower() == 'random':
            keys = random_char(9)
            print(f'Generated random string: "{keys}"')
        Field()[label].type(keys)


@step("I choose (?P<option>.*) option in (?P<label>\D+) field")
def step_impl(context, option, label):
    FieldByLabel(label).expand().choose_option(option)


@step("I delete (?P<option>.*) option from (?P<label>\D+) field")
def step_impl(context, option, label):
    if context.environment == 'android':
        raise Exception("Not implemented on ePRO")
    FieldByLabel(label).delete_option(option)


@step(r"I see (?:that )?(?P<label>\D+) field(?: is enabled| is active)?")
def step_impl(context, label):
    if context.environment == 'web':
        field = FieldByLabel(label)
        assert not field.is_disabled, str(field)
    elif context.environment == 'android':
        try:
            assert Field()[label].is_displayed()
        except TimeoutException:
            raise Exception(f"\nExpected: {label} field is on the page\n"
                            f"Actual: There is no {label} field")


@step(r"I see that (?P<label>\D+) field is disabled")
def step_impl(context, label):
    if context.environment == 'web':
        field = FieldByLabel(label)
        assert field.is_disabled, str(field)
    elif context.environment == 'android':
        raise Exception("Not implemented on ePRO")


@step("I see that (?P<label>\D+) field is blank")
def step_impl(context, label):
    if context.environment == 'web':
        field = FieldByLabel(label)
        assert field.is_blank, str(field)
    elif context.environment == 'android':
        raise Exception("Not implemented on ePRO")


@then(r"I see that (?P<label>\D+) field has exact (?P<text>.*) text")
def step_impl(context, label, text):
    if context.environment == 'web':
        raise Exception("Not implemented on web")
    elif context.environment == 'android':
        assert Field()[label].has_text(text)


@then("I see (?P<text>.*) (?:text|option) in (?P<label>\D+) field")
def step_impl(context, text, label):
    if context.environment == 'web':
        field = FieldByLabel(label)
        assert text in FieldByLabel(label), f"There is no {text} text/option in {label} field.\n" \
                                            f"{field}"
    elif context.environment == 'android':
        raise Exception("Not implemented on ePRO")


@then("I don't see (?P<text>.*) (?:text|option) in (?P<label>\D+) field")
def step_impl(context, text, label):
    if context.environment == 'web':
        field = FieldByLabel(label)
        assert text not in field, f"There is {text} text/option in {label} field.\n" \
                                  f"{field}"
    elif context.environment == 'android':
        raise Exception("Not implemented on ePRO")
