import time

from behave import *

from helpers.helpers import wait_for_angular

use_step_matcher('re')


@step(r"I sleep for (?P<sleep_time>\d+) seconds")
def step_impl(context, sleep_time):
    time.sleep(int(sleep_time))


@step(r"I wait for angular")
def step_impl(context):
    wait_for_angular()
