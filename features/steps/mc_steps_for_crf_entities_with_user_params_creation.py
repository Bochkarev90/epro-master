from behave import given


class Entities:

    def __init__(self, field_label, value):
        self._value = value
        self._field_label = field_label
        self._common_fields = None
        self._pseudos_and_selectors = None
        self._checkboxes = None

    @property
    def step(self):
        if self._field_label in self._common_fields:
            return f"\nAnd I put {self._value} in {self._field_label} field"
        elif self._field_label in self._pseudos_and_selectors:
            return f"\nAnd I choose {self._value} option in {self._field_label} field"
        elif self._field_label in self._checkboxes:
            if self._value.lower() != 'false':
                return f"\nAnd I click on {self._field_label} checkbox"
            else:
                return ""
        else:
            exception = f"""No field {self._field_label} on adding popup. Fields that can be used: {
            ', '.join(self._common_fields + self._pseudos_and_selectors + self._checkboxes)}. 
            If you see this message, but you're sure that the field is on popup -
            add it into Entities class in mc_entities_creation module"""
            raise Exception(exception)


class Visit(Entities):

    def __init__(self, field_label, value):
        super().__init__(field_label, value)
        self._common_fields = ['Visit Name', 'Visit Code', 'Order', 'Max Repeat Number']
        self._pseudos_and_selectors = ['Visit Type', 'Epoch', 'Forms']
        self._checkboxes = ['Is Repeated', 'Is Mandatory']


class Form(Entities):

    def __init__(self, field_label, value):
        super().__init__(field_label, value)
        self._common_fields = ['Form Name', 'Form Code', 'Order', 'Description']
        self._pseudos_and_selectors = ['Visit', 'Epoch', 'Form Type']


class Section(Entities):

    def __init__(self, field_label, value):
        super().__init__(field_label, value)
        self._common_fields = ['Section Name', 'Section Code', 'Order', 'Description', 'Max Repeat Number']
        self._pseudos_and_selectors = ['Section template', 'DataSet']
        self._checkboxes = ['is Repeating', 'is Mandatory', 'In table format', 'Auto numbering']


class Item(Entities):

    def __init__(self, field_label, value):
        super().__init__(field_label, value)
        self._common_fields = ['Title', 'Code', 'Code:', 'Order', 'Description', 'Length', 'Default', 'Columns Width']
        self._pseudos_and_selectors = ['Field Type', 'Data Type', 'Control Type']
        self._checkboxes = ['Is Critical', 'Is Mandatory', 'Is Lab Data', 'Is Data Transfer']


class Schedule(Entities):

    def __init__(self, field_label, value):
        super().__init__(field_label, value)
        self._common_fields = []
        self._pseudos_and_selectors = ['Schedule Type', 'Please, define a pattern for your schedule']
        self._checkboxes = []


@given("I create visit with params")
def step_impl(context):
    steps_to_execute = """
        When I click on VISIT STRUCTURE button
        And I click on ADD VISIT button
    """
    for param in context.table:
        steps_to_execute += Visit(field_label=param['param'], value=param['value']).step
    steps_to_execute += "\nAnd I click on SAVE button"
    context.execute_steps(steps_to_execute)


@given("I create form with params")
def step_impl(context):
    steps_to_execute = """
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
    """
    for param in context.table:
        steps_to_execute += Form(field_label=param['param'], value=param['value']).step
    steps_to_execute += "\nAnd I click on SAVE button"
    context.execute_steps(steps_to_execute)


@given("I create section with params in form with {form_code} code")
def step_impl(context, form_code):
    steps_to_execute = f"""
        When I click on CRF DESIGNING button
        And I expand record with params in forms table
            | column header     | td value               |
            | Form Code         | {form_code}            |
        And I click on ADD SECTION button
    """
    for param in context.table:
        steps_to_execute += Section(field_label=param['param'], value=param['value']).step
    steps_to_execute += "\nAnd I click on SAVE button"
    context.execute_steps(steps_to_execute)


@given("I create item with params in section with {section_code} code")
def step_impl(context, section_code):
    steps_to_execute = f"""       
        When I expand record with params in sections table
            | column header     | td value               |
            | Section Code      | {section_code}         |
        And I click on ADD NEW ITEM button
    """
    for param in context.table:
        steps_to_execute += Item(field_label=param['param'], value=param['value']).step
    steps_to_execute += "\nAnd I click on SAVE button"
    context.execute_steps(steps_to_execute)


@given("I create schedule with params for form with {form_code} form code")
def step_impl(context, form_code):
    schedule_params = dict(context.table)
    raise Exception("Not implemented")
    # TODO
    # steps_to_execute = f"""
    #     When I click on CRF DESIGNING button
    #     And I create schedule for record with params in forms table
    #         | column header     | td value            |
    #         | Form Code         | {form_code}         |
    #     And I click on ADD NEW ITEM button
    # """
    # for param in context.table:
    #     steps_to_execute += Item(field_label=param['param'], value=param['value']).step
    # steps_to_execute += "\nAnd I click on SAVE button"
    # context.execute_steps(steps_to_execute)
