from behave import *
from page_objects.live_content_page import LiveContentPage


@when(u'I click on \'Directos\' in the banner and click on \'Continuar Directo\'')
def step_impl(context):
    live_content_page = LiveContentPage(context)
    live_content_page.get_live_content()


@then(u'I should see the live content')
def step_impl(context):
    live_content_page = LiveContentPage(context)
    live_content_page.check_live_content()
