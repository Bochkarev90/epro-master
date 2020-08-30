from behave import *

use_step_matcher('re')


@step("I add subject")
def step_impl(context):
    context.execute_steps("""
       When I click on ADD SUBJECT button
       When I click on ADD button
    """)

#
# @step("I click on ADD button for {subject_title} subject in {visit_title} visit")
# def step_impl(context, subject_title, visit_title):
#     SubjectMatrix().subject_by_title(subject_title).expand()[visit_title].add_btn.click()
