from behave import *

from helpers.helpers import take_element_screenshot
from page_objects.edc import EDC


use_step_matcher('re')


@step("I test")
def step_impl(context):
    EDC().edc_form.save_button.take_screenshot('asda')
    # print('Save button is visible: ', EDC().edc_form.save_button.is_displayed())
    # print('Save button is active: ', EDC().edc_form.save_button.is_enabled())
    # print('Save button is disabled: ', EDC().edc_form.save_button.is_disabled())
    # print('Cancel button is visible: ', EDC().edc_form.cancel_button.is_displayed())
    # print('Cancel button is active: ', EDC().edc_form.cancel_button.is_enabled())
    # print('Cancel button is disabled: ', EDC().edc_form.cancel_button.is_disabled())
    # print('Approve button is visible: ', EDC().edc_form.approve_button.is_displayed())
    # print('Approve button is active: ', EDC().edc_form.approve_button.is_enabled())
    # print('Approve button is disabled: ', EDC().edc_form.approve_button.is_disabled())
