from behave import *
from selene.api import browser

from config import MATRIX_CLOUD_PASSWORD, EMAIL_DOMAIN

use_step_matcher('re')


@given(r"I logged in as (?P<role>[A-Za-z]+)")
@when(r"I log in as (?P<role>[A-Za-z]+)")
def step_impl(context, role):
    login = role + EMAIL_DOMAIN
    password = MATRIX_CLOUD_PASSWORD
    context.execute_steps(f"""
        Given I put {login} in Email field
        And I put {password} in Password field
        And I click on Login button
        And I close system alert
    """)


@step("I logout")
def step_impl(context):
    if context.environment == 'web':
        context.execute_steps("""
            Given I open user info menu
            And I click on Logout option
        """)
        browser.driver.execute_script('window.localStorage.clear();')
        browser.driver.execute_script('window.sessionStorage.clear();')
    elif context.environment == 'android':
        context.execute_steps("""
            Then I tap on Person button
            And I click on Logout button
            And I click on OK button
        """)


@step("I go to CRF structure")
def step_impl(context):
    context.execute_steps("""
        Given I expand main menu
        And I expand CRF designer menu
        And I open CRF submenu
        And I click on button with Go to visit structure title
    """)
