from behave import *
from page_objects.register_page import RegisterPage

from variables.variables import *


@when(u'I navigate to register page, I fill in the mandatory fields and click button Continuar')
def step_impl(context):
    try:
        register_page = RegisterPage(context)
        register_page.navigate_to_register()
        register_page.enter_credentials(nombre, email, password)
    except Exception as e:
        print(f"Error: {e}")


@then(u'I should see a confirmation page')
def step_impl(context):
    try:
        register_page = RegisterPage(context)
        register_page.check_redirect()
        print("Registration successful")
    except Exception as e:
        print(f"Error: {e}")


@when(u'I navigate to register page, I fill in the mandatory fields with an invalid email and click button Continuar')
def step_impl(context):
    try:
        register_page = RegisterPage(context)
        register_page.navigate_to_register()
        register_page.enter_invalid_credentials(nombre, email, password)
    except Exception as e:
        print(f"Error: {e}")


@then(u'I can´t click button Continuar')
def step_impl(context):
    try:
        register_page = RegisterPage(context)
        register_page.disable_button_continuar()
    except Exception as e:
        print(f"Error: {e}")
