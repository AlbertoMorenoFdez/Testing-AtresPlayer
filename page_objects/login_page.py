from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from variables.variables import *

class LoginPage:
    def __init__(self, context):
        self.context = context

        self.entry_button= (By.XPATH, '//button[@title="Entra o Regístrate"]')
        self.email_input = (By.ID, 'email')
        self.password_input = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[3]/div[2]/input')
        self.login_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[3]/button')
        self.error_message = (By.XPATH, '//div[text()="Usuario o contraseña no válidas"]')

    def navigate_to_login(self):
        self.context.driver.find_element(*self.entry_button).click()

    def enter_credentials(self, email, password):
        WebDriverWait(self.context.driver, 10).until(EC.presence_of_element_located(self.email_input)).send_keys(email)
        self.context.driver.find_element(*self.password_input).send_keys(password)

    def enter_invalid_credentials(self, email, password):
        WebDriverWait(self.context.driver, 10).until(EC.presence_of_element_located(
            self.email_input)).send_keys(generate_invalid_email())
        self.context.driver.find_element(*self.password_input).send_keys(generate_invalid_password())

    def click_login(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def check_redirect(self):
        if WebDriverWait(self.context.driver, 10).until(EC.url_contains('https://www.atresplayer.com/')):
            return True
        elif WebDriverWait(self.context.driver, 10).until(
                EC.url_contains('https://atresplayer.com/usuario/cuenta/suscripcion-y-paquetes')):
            home_button_xpath = '//img[@alt="Inicio Atresplayer"]'
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, home_button_xpath))
            ).click()
            WebDriverWait(self.context.driver, 10).until(EC.url_contains('https://www.atresplayer.com/'))
            return True
        else:
            return False

    def check_error_message(self):
        mensaje_error = WebDriverWait(self.context.driver, 30).until(
            EC.presence_of_element_located(self.error_message)
        )
        print("El mensaje de error está presente en la página.")
