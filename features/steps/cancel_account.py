from behave import *
from page_objects.cancel_account_page import CancelPage
from page_objects.common_steps_page import CommonStepsPage


@when(
    u'I access the \'My Account\' section and select \'Configuration\' and click \'dar de baja\' I see a new page '
    u'where I can click \'Eliminar cuenta\'')
def step_impl(context):
    cancel_account_page = CancelPage(context)

    try:
        cancel_account_page.open_user_menu()
        cancel_account_page.click_configuracion()
        cancel_account_page.click_dar_de_baja()
        cancel_account_page.click_eliminar_cuenta()
    except Exception as e:
        print(f"Error: {e}")


@then(u'I see a confirmation message that my account has been deleted')
def step_impl(context):
    cancel_account_page = CancelPage(context)
    try:
        cancel_account_page.check_confirmation_message()
    except Exception as e:
        print(f"Error: {e}")
