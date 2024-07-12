from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParentalPage:
    def __init__(self, context):
        self.context = context

        self.menu_user = (By.XPATH, '//button[@title="Abrir menú de usuario"]')
        self.link_perfiles = (By.LINK_TEXT, 'Perfiles')
        self.button_edit_perfiles = (
            By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/main/div/button/p[text()="Editar perfiles"]')
        self.button_edit_perfil = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/main/div/div/div/div/div[2]')
        self.parental_control_link = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/main/div/div[4]/div/label[3]')
        self.pin_input = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/main/div/div[4]/div[2]/div/input')

    def open_user_menu(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.menu_user)
        ).click()
        print("Clicking on 'Abrir menú de usuario' button...")

    def click_get_perfiles(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable((self.link_perfiles))).click()
            print("Click en perfiles")
        except Exception as e:
            print(f"Error: {e}")

    def click_edit_perfiles(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable((self.button_edit_perfiles))).click()
            print("Click en editar perfiles")
        except Exception as e:
            print(f"Error: {e}")

    def edit_perfil(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(
                    self.button_edit_perfil)).click()
            print("Click en perfil a editar")
        except Exception as e:
            print(f"Error: {e}")

    def click_parental_control(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(
                    self.parental_control_link)).click()
            print("Click en control parental")

        except Exception as e:
            print(f"Error: {e}")

    def send_pin(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.presence_of_element_located(self.pin_input)
            )
            print("Esperando a que el div de pin este presente")

            print("Enviando pin a los inputs")
            for i in range(1, 5):  # Asume que hay 4 elementos de entrada
                input_xpath = f'//*[@id="root"]/div/div[1]/div[3]/main/div/div[4]/div[2]/div/input[{i}]'
                input_element = WebDriverWait(self.context.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, input_xpath))
                )
                input_element.send_keys('1234')
            print("Pin enviado a todos los inputs")

        except Exception as e:
            print(f"Error: {e}")

    def click_guardar(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/main/div/div[6]/button[2]'))).click()
            print("Click en guardar")

        except Exception as e:
            print(f"Error: {e}")

    def check_confirmation_message(self):
        try:
            confirmation_message_element = WebDriverWait(self.context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div/p'))
            )
            assert confirmation_message_element.text == "Tu perfil se ha cambiado correctamente.", (
                f"Tu perfil se ha cambiado "
                f"correctamente.', "
                f"but got '"
                f"{confirmation_message_element.text}'")
            print("Perfil cambiado correctamente")
        except Exception as e:
            print(f"Error: {e}")
