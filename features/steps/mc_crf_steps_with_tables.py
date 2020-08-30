from behave import *
from selene.api import *
from selene.core.exceptions import TimeoutException

from page_elements.matrixcloud.button import ButtonByText
from page_elements.matrixcloud.table import Table


@step("I filter {table_title} table by {column_header} column with {filter_value} value")
def step_impl(context, table_title, column_header, filter_value):
    header_row = Table()[table_title].header_row
    header_row.header_by_text(column_header).filter_icon.click()
    header_row.filter_input_field_by_header_text(column_header).type(filter_value)


@step("I sort {table_title} table by {column_header}")
def step_impl(context, table_title, column_header):
    Table()[table_title].header_row.header_by_text(column_header).sort_icon.click()


@step("I find record in {table_title} table with params")
@step("I see record in {table_title} table with params")
def step_impl(context, table_title):
    data = dict(context.table)
    context.record = Table()[table_title].row_by_params(**data)


@step("I see {number_of_records} records in {table_title} table with params")
def step_impl(context, number_of_records, table_title):
    data = dict(context.table)
    expected_number_of_records = int(number_of_records)
    actual_number_of_records = Table()[table_title].count_rows_by_params(**data)
    assert expected_number_of_records == actual_number_of_records, \
        f'Expected: {expected_number_of_records} record(s) with given params' \
        f'\nActual: {actual_number_of_records} record(s)'


@step("I {action} record with params in {table_title} table")
def step_impl(context, action, table_title):
    data = dict(context.table)
    action = action.lower()
    context.record = Table()[table_title].row_by_params(**data)
    if action == 'expand':
        if not context.record.is_expanded:
            context.record.expand_btn().click()
    elif action == 'edit':
        context.record.edit_btn().click()
    elif action == 'copy':
        context.record.copy_btn().click()
    elif action == 'delete':
        context.record.delete_btn().click()
        context.execute_steps("Given I wait for angular")
        ButtonByText('Yes').click()
    elif action in ['create schedule for', 'create schedule']:
        context.record.create_schedule_btn().click()
    else:
        raise Exception('Action must be in [edit, expand, delete, copy, create schedule *for]')


@step("I {action} this record")
def step_impl(context, action):
    if not context.record:
        raise Exception('No record in context')
    action = action.lower()
    if action == 'expand':
        context.record.expand_btn().click()
    elif action == 'edit':
        context.record.edit_btn().click()
    elif action == 'delete':
        context.record.delete_btn().click()
        ButtonByText('Yes').click()
    elif action in ['create schedule for', 'create schedule']:
        context.record.create_schedule_btn().click()
    else:
        raise Exception('Action must be in [edit, expand, delete]')


@then("I don't see delete button opposite record with params in {table_title} table")
def step_impl(context, table_title):
    data = dict(context.table)
    try:
        Table()[table_title].row_by_params(**data).delete_btn().click()
        assert False, 'Expected: no delete button opposite row with params ' + str(data) + \
                      '\nActual: delete button is here'
    except TimeoutException:
        return True


@then("I don't see create schedule button opposite record with params in {table_title} table")
def step_impl(context, table_title):
    data = dict(context.table)
    try:
        Table()[table_title].row_by_params(**data).create_schedule_btn().click()
        assert False, 'Expected: no schedule button opposite row with params ' + str(data) + \
                      '\nActual: schedule button is here'
    except TimeoutException:
        return True


@then("I see that create schedule icon for this form became yellow")
def step_impl(context):
    context.record.create_schedule_btn().s('./button').should(have.attribute('style').value('color: gold;'))


@then("I see that create schedule icon for form with {form_code} code became yellow")
def step_impl(context, form_code):
    data = {'Form Code': form_code}
    context.record = Table()['forms'].row_by_params(**data)
    context.record.create_schedule_btn().s('./button').should(have.attribute('style').value('color: gold;'))


@then("I see that create schedule icon for this form is not yellow")
def step_impl(context):
    try:
        context.record.create_schedule_btn().s('./button').should(have.attribute('style').value('color: gold;'))
    except AssertionError:
        return True


@step('I take a screenshot of whole "{table_title}" table')
def step_impl(context, table_title):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f'_{table_title} table'
    Table()[table_title].take_screenshot(img_title=img_title)


@step('I take a screenshot of headers of "{table_title}" table')
def step_impl(context, table_title):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f'_{table_title} table headers'
    Table()[table_title].header_row.take_screenshot(img_title=img_title)


@step('I take a screenshot of "{header_text}" header in "{table_title}" table')
def step_impl(context, header_text, table_title):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f'_{header_text} header in {table_title} table'
    Table()[table_title].header_row.header_by_text(header_text).take_screenshot(img_title=img_title)


@step('I take a screenshot of row with params in "{table_title}" table')
def step_impl(context, table_title):
    context.screen_num += 1
    data = dict(context.table)
    img_title = str(context.screen_num) + '_' + context.scenario.name + f'_Row with params in {table_title} table'
    Table()[table_title].row_by_params(**data).take_screenshot(img_title=img_title)


@step('I take a screenshot of this row')
def step_impl(context):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + f'_This row'
    context.record.take_screenshot(img_title=img_title)


@step("I take a screenshot of access code")
def step_impl(context):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + ' - access code scr'
    context.access_code_field.take_screenshot(img_title)


@step("I take a screenshot of this form")
def step_impl(context):
    context.screen_num += 1
    img_title = str(context.screen_num) + '_' + context.scenario.name + ' - epro form'
    context.form.take_screenshot(img_title)
