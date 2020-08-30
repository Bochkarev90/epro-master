from behave import *
from selene.api import *

from page_elements.matrixcloud.lists import List
from page_elements.matrixcloud.specialfields import SpecialFields
from page_objects.subject_matrix import SubjectMatrix
from page_elements.matrixcloud.table import Table

use_step_matcher('re')


@step("I run (?P<environment>Sandbox|Test|Training|Production) environment")
def step_impl(context, environment):
    Table()['environments'].row_by_params(**{'Environment': environment}).run_btn().click()


@step("I expand (?P<subject>this|first|last) subject")
def step_impl(context, subject):
    if subject == 'this':
        context.subject.expand()
    elif subject == 'first':
        context.subject = SubjectMatrix().first_subject.expand()
    elif subject == 'last':
        context.subject = SubjectMatrix().last_subject.expand()


@step("I (?P<action>find|expand) subject with (?P<subject_title>.*) title")
def step_impl(context, action, subject_title):
    context.subject = SubjectMatrix().subject_by_title(subject_title)
    if action == 'expand':
        context.subject.expand()


@step("I click on generate access code icon for (?P<subject>this|first|last) subject")
def step_impl(context, subject):
    if subject == 'this':
        context.subject.access_code_icon.click()
    elif subject == 'first':
        context.subject = SubjectMatrix().first_subject.access_code_icon.click()
    elif subject == 'last':
        context.subject = SubjectMatrix().last_subject.access_code_icon.click()


@step("I click on generate access code icon for (?P<subject_title>.*) subject")
def step_impl(context, subject_title):
    context.subject = SubjectMatrix().subject_by_title(subject_title).access_code_icon.click()


@step("I click on ADD button for (?P<subject>this|first|last) subject in (<visit_title>) visit")
def step_impl(context, subject, visit_title):
    if subject == 'this':
        context.subject.expand()[visit_title].add_btn.click()
    elif subject == 'first':
        SubjectMatrix().first_subject.expand()[visit_title].add_btn.click()
    elif subject == 'last':
        SubjectMatrix().last_subject.expand()[visit_title].add_btn.click()


@step("I see access code")
def step_impl(context):
    access_code_field = SpecialFields().access_code_field
    access_code_field.element.should(have.css_class('access-code-title'))
    assert len(access_code_field.access_code) == 9
    context.access_code_field = access_code_field
    context.access_code = access_code_field.access_code


@step("I copy access code")
def step_impl(context):
    SpecialFields().access_code_field.click()


@step("I see that access code icon is (?P<icon_color>yellow|grey) for (?P<subject>this|first|last) subject")
def step_impl(context, icon_color, subject):
    if subject == 'first':
        context.subject = SubjectMatrix().first_subject
    elif subject == 'last':
        context.subject = SubjectMatrix().last_subject
    if icon_color == 'yellow':
        assert context.subject.access_code_is_generated
    elif icon_color == 'grey':
        assert context.subject.access_code_is_not_generated


@step("I see that access code icon is (?P<icon_color>yellow|grey) for (?P<subject_title>.*) subject")
def step_impl(context, icon_color, subject_title):
    context.subject = SubjectMatrix().subject_by_title(subject_title)
    if icon_color == 'yellow':
        assert context.subject.access_code_is_generated
    elif icon_color == 'grey':
        assert context.subject.access_code_is_not_generated


@given("I add new subject with access code")
def step_impl(context):
    context.execute_steps("""
        Given I start the browser
        And I logged in as investigator
        And I expand main menu
        And I expand EDC menu
        And I open Environment submenu
        And I add subject
        And I click on generate access code icon for last subject
        And I click on generate button
    """)


@step("I get access code of last subject")
def step_impl(context):
    context.execute_steps("""
        Given I start the browser
        And I logged in as investigator
        And I expand main menu
        And I expand EDC menu
        And I open Environment submenu
        And I click on generate access code icon for last subject
    """)


@step("I click on issue diary icon for (?P<subject>this|first|last) subject in (?P<visit_code>.*) visit")
def step_impl(context, subject, visit_code):
    if subject == 'this':
        return context.subject[visit_code].issue_diary_icon_click()
    if subject == 'first':
        context.subject = SubjectMatrix().first_subject[visit_code].issue_diary_icon_click()
    if subject == 'last':
        context.subject = SubjectMatrix().last_subject[visit_code].issue_diary_icon_click()


@step("I click on issue diary icon for (?P<subject_title>.*) subject in (?P<visit_code>.*) visit")
def step_impl(context, subject_title, visit_code):
    context.subject = SubjectMatrix().subject_by_title(subject_title)[visit_code].issue_diary_icon_click()


@step("I see that this subject has filled (?P<form_code>.*) form in (?P<visit_code>.*) visit")
def step_impl(context, form_code, visit_code):
    assert context.subject[visit_code].form_with_title_exists(form_code), \
        f"Expected: subject has filled {form_code} form\nActual: no filled {form_code} form"
    context.form = context.subject[visit_code].form_by_title(form_code)


@step("I click on this form")
def step_impl(context):
    context.form.open()


@step("I select (?P<form_title>.*) form")
def step_impl(context, form_title):
    List().option_with_text_click(form_title)


@step("I take a screenshot of (?P<subject>this|first|last) subject")
def step_impl(context, subject):
    if subject == 'first':
        context.subject = SubjectMatrix().first_subject
    elif subject == 'last':
        context.subject = SubjectMatrix().last_subject
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f' - {subject} subject'
    context.subject.take_screenshot(img_title)


@step("I take a screenshot of (?P<subject_title>.*) subject")
def step_impl(context, subject_title):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f' - {subject_title} subject'
    context.subject = SubjectMatrix().subject_by_title(subject_title).take_screenshot(img_title)
