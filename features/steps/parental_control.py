from behave import *
from page_objects.common_steps_page import CommonStepsPage
from page_objects.parental_page import ParentalPage


@when(u'I acces to edit my profile y select the option to activate parental control by adding the pin')
def step_impl(context):
    parental_page = ParentalPage(context)

    try:
        parental_page.open_user_menu()
        parental_page.click_get_perfiles()
        parental_page.click_edit_perfiles()
        parental_page.edit_perfil()
        parental_page.click_parental_control()
        parental_page.send_pin()
        parental_page.click_guardar()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I should see a message that confirms that my profile has been update')
def step_impl(context):
    try:
        parental_page = ParentalPage(context)
        parental_page.check_confirmation_message()
    except Exception as e:
        print(f"Error: {e}")
