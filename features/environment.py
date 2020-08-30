from selene.api import browser

from driver_management.drivers import Drivers
from helpers.helpers import wait_for_angular
from helpers.start_from_cli import kill_drivers


def before_all(context):
    kill_drivers()
    browser.config.save_screenshot_on_failure = True
    browser.config.save_page_source_on_failure = False
    browser.config.timeout = 5


def before_scenario(context, scenario):
    context.environment = ''
    context.screen_num = 0
    context.created_entities = {
        'visits': [],
        'forms': [],
        'sections': [],
        'items': [],
        'schedules': [],
    }


def before_step(context, step):
    if context.environment == 'web' and step.name not in ['I start the browser',
                                                          'I click on button with Go to visit structure title',
                                                          'I click on CRF DESIGNING button']:
        wait_for_angular()


def before_tag(context, tag):
    if tag.lower() == 'android':
        Drivers().start_android()


def after_scenario(context, scenario):
    Drivers().clean_web().quit_android()
    # if context.environment == 'web':
    #     for entity_type, value in context.created_entities.items():
    #         for entity in value:
    #             print(entity.title + ': ' + entity.guid)
    #     for entity in context.created_entities['visits'] + context.created_entities['forms']:
    #         entity.delete()
    #     context.created_entities.clear()


def after_all(context):
    Drivers().quit_web().quit_android()
