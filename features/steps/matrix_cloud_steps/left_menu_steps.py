from behave import *

from page_objects.leftmenu import LeftMenu

use_step_matcher('re')


@step("I expand main menu")
def step_impl(context):
    LeftMenu().expand()


@step("I expand (?P<menu_title>.*)? menu")
def step_impl(context, menu_title):
    LeftMenu()[menu_title].expand()


@then("(?:I see that)? main menu is expanded")
def step_impl(context):
    assert LeftMenu().is_expanded, "Expected: Main menu is expanded\n" \
                                   "Actual: Main menu is collapsed"


@then("(?:I see that)? (?P<menu_title>.*) menu is expanded")
def step_impl(context, menu_title):
    assert LeftMenu()[menu_title]._is_expanded, f"Expected: Menu with {menu_title} title is expanded\n" \
                                               f"Actual: Menu is collapsed"


@then("(?:I see that)? (?P<menu_title>.*) (?:sub)?menu is visible")
def step_impl(context, menu_title):
    left_menu = LeftMenu()
    assert menu_title in left_menu, f"Expected: {menu_title} menu is visible\n" \
                                    f"Actual: Only these menus are visible: {str(left_menu)}"


@step("I (?:click on|open) (?P<submenu_title>.*) submenu")
def step_impl(context, submenu_title):
    LeftMenu()[submenu_title].click()
