from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class RegisterPage:
    def __init__(self, context):
        self.context = context

        self.entry_button = (By.XPATH, '//button[@title="Entra o Regístrate"]')
        self.cuenta_gratis = (By.XPATH, '//a/span[contains(text(), "Crea tu cuenta gratis")]')
        self.gratisButton = (
            By.XPATH,
            '//button[@class="style__StyledStandardButton-sc-16vuxcz-2 hmhcmZ free_package"][p[text()="Gratis"]]')
        self.use_your_email = (By.XPATH, '//*[text()="Utiliza tu email"]')
        self.name_input = (By.ID, 'name')
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'password')
        self.year_select = (By.NAME, 'year')
        self.yearValue = '1978'
        self.gender_select = (By.NAME, 'gender')
        self.hombreValue = 'hombre'
        self.term_and_conditions = (By.ID, 'termsAndConditions')
        self.continuar_button = (By.XPATH,
                                 '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[2]/div[3]/button/p[text()="Continuar"]')
        self.expected_url = 'https://www.atresplayer.com/registro/confirmacion'

    def navigate_to_register(self):
        print("Navigating to register")
        try:
            self.context.driver.find_element(*self.entry_button).click()
            print("Click en Entra o Regístrate")

            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(self.cuenta_gratis)
            ).click()
            print("Click en el elemento de registro.")

            WebDriverWait(self.context.driver, 10).until(
                EC.presence_of_element_located(self.gratisButton)
            ).click()
            print("Click en el botón Gratis")
        except Exception as e:
            print(f"Error en navigate_to_register: {e}")

    def enter_credentials(self, name, email, password):
        print("Introduciendo credenciales")
        try:
            self.context.driver.find_element(*self.name_input).send_keys(name)
            self.context.driver.find_element(*self.email_input).send_keys(email)
            self.context.driver.find_element(*self.password_input).send_keys(password)
            select = Select(self.context.driver.find_element(*self.year_select))
            select.select_by_value(self.yearValue)
            select = Select(self.context.driver.find_element(*self.gender_select))
            select.select_by_value(self.hombreValue)
            self.context.driver.find_element(*self.term_and_conditions).click()
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(self.continuar_button)
            ).click()

            print("Credenciales introducidas y botón Continuar presionado")
        except Exception as e:
            print(f"Error en enter_credentials: {e}")

    def enter_invalid_credentials(self, name, bad_email, password):
        print("Introduciendo credenciales inválidas")
        bad_mail = 'bad_email@noexiste,com'
        try:
            self.context.driver.find_element(*self.name_input).send_keys(name)
            self.context.driver.find_element(*self.email_input).send_keys(bad_mail)
            print(f"Email inválido: {bad_mail}")
            self.context.driver.find_element(*self.password_input).send_keys(password)
            select = Select(self.context.driver.find_element(*self.year_select))
            select.select_by_value(self.yearValue)
            select = Select(self.context.driver.find_element(*self.gender_select))
            select.select_by_value(self.hombreValue)
            self.context.driver.find_element(*self.term_and_conditions).click()
            print("Credenciales inválidas introducidas y botón Continuar presionado")
        except Exception as e:
            print(f"Error en enter_invalid_credentials: {e}")

    def check_redirect(self):
        try:
            WebDriverWait(self.context.driver, 30).until(EC.url_to_be(self.expected_url))
            assert self.context.driver.current_url == self.expected_url, f"Expected '{self.expected_url}', but got '{self.context.driver.current_url}'"
            print("Registration successful")
        except Exception as e:
            print(f"Error en check_redirect: {e}")

    def disable_button_continuar(self):
        try:
            boton_continuar = WebDriverWait(self.context.driver, 10).until(
                EC.presence_of_element_located(self.continuar_button)
            )

            if boton_continuar.get_attribute("disabled") is not None:
                print("El botón Continuar está deshabilitado.")
            else:
                print("El botón Continuar está habilitado.")
        except Exception as e:
            print(f"Error en disable_button_continuar: {e}")
