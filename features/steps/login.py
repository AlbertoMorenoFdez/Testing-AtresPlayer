from behave import *
from selenium.common import WebDriverException
from page_objects.login_page import LoginPage

from variables.variables import *


@when(
    u'I navigated to login section and I enter valid email address, and valid password into the fields and click on '
    u'Login Button')
def step_impl(context):
    try:
        login_page = LoginPage(context)
        login_page.navigate_to_login()
        login_page.enter_credentials(email, password)
        login_page.click_login()
        print("click en login")
    except WebDriverException as e:
        print(f"Error during login: {e}")


@then(u'I should get logged in and redirected to the home page or subscription page')
def step_impl(context):
    try:
        print("comprobando url")
        login_page = LoginPage(context)
        if login_page.check_redirect():
            print("Login successful")
    except WebDriverException as e:
        print(f"Error checking URL: {e}")


@when(u'I navigated to login section and I enter invalid email address, and invalid password into the fields and '
      u'click on Login Button')
def step_impl(context):
    try:
        login_page = LoginPage(context)
        login_page.navigate_to_login()
        login_page.enter_invalid_credentials(email, password)
        login_page.click_login()
        print("click en login")
    except WebDriverException as e:
        print(f"Error during login: {e}")


@then(u'I should get an error message and stay on the login page')
def step_impl(context):
    try:
        login_page = LoginPage(context)
        login_page.check_error_message()
        print("El mensaje de error está presente en la página.")
    except WebDriverException as e:
        print(f"Error checking error message: {e}")
