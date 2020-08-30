from behave import *

from page_elements.epro.webview import WebView

use_step_matcher('re')


@step("I put (?P<answer>.*) answer")
def step_impl(context, answer):
    WebView().put_answer(answer)


@step("I choose (?P<answer>.*) answer")
def step_impl(context, answer):
    WebView().choose_answer(answer)


@step("I go to the next page")
def step_impl(context):
    WebView().go_next()


@step("I go to the previous page")
def step_impl(context):
    WebView().go_previous()


@step("I see (?P<question_text>.*) question")
def step_impl(context, question_text):
    expected = question_text
    actual = WebView().get_question_text()
    assert expected == actual, \
        f"Expected: '{expected}' question\n " \
        f"Actual: '{actual}' question"
