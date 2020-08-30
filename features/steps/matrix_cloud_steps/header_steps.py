from behave import *

from page_elements.matrixcloud.lists import PopoverList
from page_objects.header import Header

use_step_matcher('re')


@step("I go to dashboard")
def step_impl(context):
    Header().go_to_dashboard()


@step("I see that project title is (?P<project_title>.*)")
def step_impl(context, project_title):
    expected = project_title
    actual = Header().get_project_title()
    assert expected == actual, f"Expected: {expected} project title\nActual: {actual} project title"


@step("I open user info menu")
def step_impl(context):
    Header().open_user_info()


@step("I click on (?P<option>Change Password|Manuals|Helpdesk|Logout) option")
def step_impl(context, option):
    PopoverList().choose_option(option)
