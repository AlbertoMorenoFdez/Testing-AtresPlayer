from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CancelPage:
    def __init__(self, context):
        self.context = context

        self.menu_user = (By.XPATH, '//button[@title="Abrir menú de usuario"]')
        self.link_configuracion = (By.LINK_TEXT, 'Configuración')
        self.link_baja = (By.LINK_TEXT, 'dar de baja')
        self.eliminar_cuenta_button = (By.XPATH, '//button/p[text()="Eliminar cuenta"]')
        self.msj_confirmacion = (
            By.XPATH, '//p[text()="Te hemos enviado un correo para que confirmes la eliminación de tu cuenta."]')

    def open_user_menu(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.menu_user)
        ).click()
        print("Clicking on 'Abrir menú de usuario' button...")

    def click_configuracion(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.link_configuracion)
        ).click()
        print("Clicking on 'Configuración' link...")

        expected_url = 'https://www.atresplayer.com/usuario/configuracion'
        try:
            WebDriverWait(self.context.driver, 10).until(EC.url_to_be(expected_url))
            assert self.context.driver.current_url == expected_url
            print("La URL es correcta.")
        except TimeoutException:
            print(f"La URL esperada no se cargó en el tiempo esperado. URL actual: {self.context.driver.current_url}")
        except AssertionError:
            print(f"La URL esperada: '{expected_url}', pero se obtuvo '{self.context.driver.current_url}'")

    def click_dar_de_baja(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.link_baja)
        ).click()
        print("Clicking on 'dar de baja' link...")

        expected_url_eliminar = 'https://www.atresplayer.com/usuario/configuracion/eliminar-cuenta'
        try:
            WebDriverWait(self.context.driver, 10).until(EC.url_to_be(expected_url_eliminar))
            assert self.context.driver.current_url == expected_url_eliminar
            print("La URL es correcta.")
        except AssertionError:
            print(f"La URL esperada: '{expected_url_eliminar}', pero se obtuvo '{self.context.driver.current_url}'")

    def click_eliminar_cuenta(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.eliminar_cuenta_button)
        ).click()
        print("Clicking on 'Eliminar cuenta' button...")

    def check_confirmation_message(self):
        mensaje_confirmacion = WebDriverWait(self.context.driver, 30).until(
            EC.presence_of_element_located(
                self.msj_confirmacion
            )
        )
        print("El mensaje de confirmación está presente en la página.")
