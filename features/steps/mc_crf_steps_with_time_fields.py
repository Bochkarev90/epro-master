from behave import *

from page_elements.matrixcloud.button import ButtonByText
from page_elements.matrixcloud.timefield import TimeFields


@step("I add {time} time")
def step_impl(context, time):
    ButtonByText('ADD').click()
    TimeFields()[-1].type(time)


@step("I add several times: {times}")
def step_impl(context, times):
    for time in (times.split(',')):
        ButtonByText('ADD').click()
        context.execute_steps("Given I wait for angular")
        TimeFields()[-1].type(time.strip())
