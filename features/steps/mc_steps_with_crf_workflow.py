from behave import *

from api.crf_api_requests import CRFAPIRequests
from page_elements.matrixcloud.field import FieldByLabel

use_step_matcher("re")


@step("I create new CRF version")
def step_impl(context):
    context.execute_steps("And I click on CREATE NEW VERSION button")
    new_version_title = str(int(FieldByLabel('ECM Version').field.text) + 0.1)
    context.execute_steps(f"""
        And I put {new_version_title} in Version Name field
        And I click on SAVE button
    """)


@given("I deploy crf to (?P<environment>Sandbox|Test|Training|Production) using (?P<web_or_api>web|api)")
def step_impl(context, environment, web_or_api):
    if web_or_api == 'web':
        if environment == 'Sandbox':
            context.execute_steps("""
                Given I logged in as crfdesigner
                And I go to CRF
                And I click on DEPLOY button
                And I choose Sandbox option in Please select an Environment type field
                And I click on CREATE button
                And I logout
            """)
        elif environment == 'Test':
            context.execute_steps("""
                Given I logged in as crfdesigner
                And I go to CRF
                And I click on CRF To Review button
                And I click on YES button
                And I click on DEPLOY button
                And I choose Test option in Please select an Environment type field
                And I put Test in Edc Name field
                And I mark Automatically update CRF for all subjects checkbox
                And I click on CREATE button
                And I click on REJECT button
                And I logout
            """)
        elif environment == 'Training':
            context.execute_steps("""
                Given I logged in as crfdesigner
                And I go to CRF
                And I click on CRF To Review button
                And I click on YES button
                And I logout
                And I logged in as crfreviewer
                And I click on APPROVE button
                And I click on TEST button
                And I click on YES button
                And I click on APPROVE button
                And I click on DEPLOY button
                And I choose Training option in Please select an Environment type field
                And I put Training in Edc Name field
                And I mark Automatically update CRF for all subjects checkbox
                And I click on CREATE button
                And I click on REJECT button
                And I logout
            """)
        elif environment == 'Production':
            raise Exception("Not implemented. We don't have a mono role with permissions to deploy to prod. It should "
                            "be a Project Manager, but he doesn't see CRF menu")
            # context.execute_steps("""
            #     Given I logged in as crfdesigner
            #     And I go to CRF
            #     And I click on CRF To Review button
            #     And I click on YES button
            #     And I logout
            #     And I logged in as crfreviewer
            #     And I click on APPROVE button
            #     And I click on TEST button
            #     And I click on YES button
            #     And I click on APPROVE button
            #     And I logout
            #     And I logged in as projectmanager
            #     And I click on DEPLOY button
            #     And I choose Production option in Please select an Environment type field
            #     And I put Production in Edc Name field
            #     And I mark Automatically update CRF for all subjects checkbox
            #     And I click on CREATE button
            #     And I create new CRF version
            #     And I logout
            # """)
    elif web_or_api == 'api':
        crf_api = CRFAPIRequests()
        if environment == 'Sandbox':
            crf_api.deploy_to_sandbox()
        elif environment == 'Test':
            crf_api.to_review().deploy_to_test('test').first_reject()
        elif environment == 'Training':
            crf_api.to_review().first_approve().to_test().second_approve().deploy_to_training('training').\
                second_reject()
        elif environment == 'Production':
            crf_api.to_review().first_approve().to_test().second_approve().deploy_to_production('production')
