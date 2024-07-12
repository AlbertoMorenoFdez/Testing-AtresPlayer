from behave import *
from page_objects.add_favorites_page import FavoritePage


@when(u'I navigate to the program of the chosen channel and by clicking on \'Details\' I can \'follow\' the program')
def step_impl(context):
    add_favorites_page = FavoritePage(context)

    try:
        add_favorites_page.acceder_a_la_casa_de_empenos()
        add_favorites_page.click_on_details()
        add_favorites_page.click_on_follow()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I should see the program in my favorites list')
def step_impl(context):
    add_favorites_page = FavoritePage(context)

    try:
        add_favorites_page.open_user_menu()
        add_favorites_page.click_on_go_to_my_atresplayer()
        add_favorites_page.check_title()
    except Exception as e:
        print(f"Error: {e}")
