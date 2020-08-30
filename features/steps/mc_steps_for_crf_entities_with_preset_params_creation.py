from behave import *

from api.api_supporting_requests import APISupportingRequests
from entities_objects.crf_form import CRFForm
from entities_objects.crf_item import CRFItem
from entities_objects.crf_schedule import CRFSchedule
from entities_objects.crf_section import CRFSection
from entities_objects.crf_visit import CRFVisit


@given("I create visit: type={v_type}, title={v_title}, code={v_code} using {web_or_api}")
def step_impl(context, v_type, v_title, v_code, web_or_api):
    new_visit = CRFVisit(v_type=v_type, v_title=v_title, v_code=v_code)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_visit.steps)
        new_visit.guid = APISupportingRequests().visit_guid_by_title(v_title)
    elif web_or_api.lower() == 'api':
        new_visit.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['visits'].append(new_visit)


@given("I create form in this visit: type={f_type}, title={f_title}, code={f_code}, order={f_order} using {web_or_api}")
def step_impl(context, f_type, f_title, f_code, f_order, web_or_api):
    this_visit = context.created_entities['visits'][-1]
    new_form = CRFForm(f_type=f_type, f_title=f_title, f_code=f_code, f_order=f_order, v_title=this_visit.title,
                       v_guid=this_visit.guid)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_form.steps)
        new_form.guid = APISupportingRequests().form_guid_by_code(f_code)
    elif web_or_api.lower() == 'api':
        new_form.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['forms'].append(new_form)


@given("I create form: type={f_type}, title={f_title}, code={f_code}, order={f_order}, visit title={v_title} "
       "using {web_or_api}")
def step_impl(context, f_type, f_title, f_code, f_order, v_title, web_or_api):
    new_form = CRFForm(f_type=f_type, f_title=f_title, f_code=f_code, f_order=f_order, v_title=v_title)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_form.steps)
        new_form.guid = APISupportingRequests().form_guid_by_code(f_code)
    elif web_or_api.lower() == 'api':
        new_form.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['forms'].append(new_form)


@given("I create section in this form: title={s_title}, code={s_code}, order={s_order} using {web_or_api}")
def step_impl(context, s_title, s_code, s_order, web_or_api):
    this_form = context.created_entities['forms'][-1]
    new_section = CRFSection(s_title=s_title, s_code=s_code, s_order=s_order, f_code=this_form.code,
                             f_guid=this_form.guid)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_section.steps)
        new_section.guid = APISupportingRequests().section_guid_by_form_and_section_codes(f_code=this_form.code,
                                                                                          s_code=s_code)
    elif web_or_api.lower() == 'api':
        new_section.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['sections'].append(new_section)


@given("I create section: title={s_title}, code={s_code}, order={s_order}, form code={f_code} using {web_or_api}")
def step_impl(context, s_title, s_code, s_order, f_code, web_or_api):
    new_section = CRFSection(s_title=s_title, s_code=s_code, s_order=s_order, f_code=f_code)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_section.steps)
        new_section.guid = APISupportingRequests().section_guid_by_form_and_section_codes(f_code=f_code,
                                                                                          s_code=s_code)
    elif web_or_api.lower() == 'api':
        new_section.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['sections'].append(new_section)


@given("I create item in this section: title={i_title}, code={i_code}, order={i_order} using {web_or_api}")
def step_impl(context, i_title, i_code, i_order, web_or_api):
    this_section = context.created_entities['sections'][-1]
    new_item = CRFItem(i_title=i_title, i_code=i_code, i_order=i_order, f_code=this_section.form_code,
                       s_code=this_section.code, s_guid=this_section.guid)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_item.steps)
    elif web_or_api.lower() == 'api':
        new_item.create_by_api()
    else:
        raise Exception("Choose web or api method")


@given("I create item: title={i_title}, code={i_code}, order={i_order}, form code={f_code}, section code={s_code} "
       "using {web_or_api}")
def step_impl(context, i_title, i_code, i_order, f_code, s_code, web_or_api):
    new_item = CRFItem(i_title=i_title, i_code=i_code, i_order=i_order, f_code=f_code, s_code=s_code)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_item.steps)
    elif web_or_api.lower() == 'api':
        new_item.create_by_api()
    else:
        raise Exception("Choose web or api method")


# @given("I create item in this section: title={i_title}, code={i_code}, order={i_order}, "
#        "field type={field_type}, data type={data_type}, control type={control_type} using {web_or_api}")
# def step_impl(context, i_title, i_code, i_order, field_type, data_type, control_type, web_or_api):
#     this_section = context.created_entities['sections'][-1]
#     new_item = Item(i_title=i_title, i_code=i_code, i_order=i_order, f_code=this_section.form_code,
#                     s_code=this_section.code, s_guid=this_section.guid).\
#         field_type(field_type).data_type(data_type).control_type(control_type)
#     if web_or_api.lower() == 'web':
#         context.execute_steps(new_item.steps)
#     elif web_or_api.lower() == 'api':
#         new_item.create_by_api()
#     else:
#         raise Exception("Choose web or api method")
#
#
# @given("I create item: title={i_title}, code={i_code}, order={i_order}, form code={f_code}, section code={s_code}, "
#        "field type={field_type}, data type={data_type}, control type={control_type} using {web_or_api}")
# def step_impl(context, i_title, i_code, i_order, f_code, s_code, field_type, data_type, control_type, web_or_api):
#     new_item = Item(i_title=i_title, i_code=i_code, i_order=i_order, f_code=f_code, s_code=s_code).\
#         field_type(field_type).data_type(data_type).control_type(control_type)
#     if web_or_api.lower() == 'web':
#         context.execute_steps(new_item.steps)
#     elif web_or_api.lower() == 'api':
#         new_item.create_by_api()
#     else:
#         raise Exception("Choose web or api method")


@given("I create individual schedule for this form using {web_or_api}")
def step_impl(context, web_or_api):
    this_form = context.created_entities['forms'][-1]
    new_schedule = CRFSchedule(s_type='Individual', f_code=this_form.code, f_guid=this_form.guid)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_schedule.steps)
    elif web_or_api.lower() == 'api':
        new_schedule.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['schedules'].append(new_schedule)


@given("I create pattern schedule for this form: repeat type={repeat_type}, repeat period={repeat_period}, "
       "valid during={valid_during}, times={times} using {web_or_api}")
def step_impl(context, repeat_type, repeat_period, valid_during, times, web_or_api):
    this_form = context.created_entities['forms'][-1]
    new_schedule = CRFSchedule(s_type='Pattern', f_code=this_form.code, f_guid=this_form.guid).\
        repeat_type(repeat_type).times(times).repeat_period(repeat_period).valid_during(valid_during)
    if web_or_api.lower() == 'web':
        context.execute_steps(new_schedule.steps)
    elif web_or_api.lower() == 'api':
        new_schedule.create_by_api()
    else:
        raise Exception("Choose web or api method")
    context.created_entities['schedules'].append(new_schedule)
