from behave import *
from page_objects.help_center_page import HelpPage


@when(u'I acces to edit my profile and select the option \'Centro de ayuda\'')
def step_impl(context):
    try:
        help_page = HelpPage(context)
        help_page.open_user_menu()
        help_page.navigate_to_help()

    except Exception as e:
        print(f"Error: {e}")


@when(u'complete the form and click on "enviar"')
def step_impl(context):
    try:
        help_page = HelpPage(context)
        help_page.select_technical_issue()
        help_page.select_web_issue()
        help_page.enter_message()
        help_page.accept_conditions()
        help_page.click_send()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I should see the option \'Resolve doubt\' and I click on it')
def step_impl(context):
    try:
        help_page = HelpPage(context)
        help_page.check_ok_message()
    except Exception as e:
        print(f"Error: {e}")
