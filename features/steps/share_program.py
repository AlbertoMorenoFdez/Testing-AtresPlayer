from behave import *
from page_objects.share_page import SharePage


@when(u'When I navigate to the program of the chosen channel and by clicking on \'Details\' I can \'share\' the program')
def step_impl(context):
    share_page = SharePage(context)

    try:
        share_page.acceder_a_la_casa_de_empenos()
        share_page.click_on_details()
        share_page.click_on_compartir()
        share_page.click_on_facebook()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I can see a new window with the social networks to share the program')
def step_impl(context):
    share_page = SharePage(context)

    try:
        share_page.check_new_window()
    except Exception as e:
        print(f"Error: {e}")
