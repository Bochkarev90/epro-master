from behave import *
from selene.api import *

from page_elements.epro.field import Field
from page_elements.epro.list import List
from page_elements.epro.list_of_forms import ListOfForms
from page_elements.epro.page import Page

use_step_matcher('re')


@step('I am on (?P<page_title>\D+) page')
@step('I see (?P<page_title>\D+) page')
def step_impl(context, page_title):
    assert Page().page_has_title(page_title)
    context.page = Page().page_title


@step("I choose (?P<question>.*) question in questions list")
def step_impl(context, question):
    List().option_by_text(question).tap()


@step("I put (?P<pin_code>\d{1,4}) (?P<repeat>repeat )?pin code")
def step_impl(context, pin_code, repeat):
    Field()['repeat pin code'].tap() if repeat else Field()['pin code'].tap()
    for symbol in list(pin_code):
        symbol = int(symbol)
        symbol += 7
        browser.driver.press_keycode(symbol)


@step("I see (?P<form_title>.*) form")
def step_impl(context, form_title):
    assert form_title in ListOfForms().forms_titles, f"No form with {form_title} title"
    context.form = ListOfForms().form_by_title(form_title)


@step("I open this form")
def step_impl(context):
    context.form.tap()


@step("I open (?P<form_title>.*) form")
def step_impl(context, form_title):
    ListOfForms().form_by_title(form_title).tap()


@step("I see that (?P<form_title>.*) form has (?P<status>no|Active|Pending|Sent) status")
def step_impl(context, form_title, status):
    expected = status
    actual = ListOfForms().form_by_title(form_title).status
    assert expected == actual, f"Expected: {expected} status of {form_title} form\nActual: {actual} status"
    context.form = ListOfForms().form_by_title(form_title)


@step("I put (?P<password>.*) password")
def step_impl(context, password):
    Field()['confirm password'].send_keys(password)
