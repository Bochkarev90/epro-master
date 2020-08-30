from behave import *

from page_objects.edc import EDC

use_step_matcher('re')


@step("I see (?P<form_title>.*) form in (?P<form_status>new|saved|approved|verified|locked) status")
def step_impl(context, form_title, form_status):
    form = EDC().edc_form
    expected = f'Form with {form_title} title'
    actual = f'Form has {form.title_text} title'
    assert form_title in form.title_text, f'Expected: {expected}\nActual: {actual}'
    expected = f'Form with {form_title} title has {form_status} status'
    actual = f'Form has {form.status} status'
    assert form.status == form_status, f'Expected: {expected}\nActual: {actual}'
