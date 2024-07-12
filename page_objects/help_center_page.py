from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelpPage:
    def __init__(self, context):
        self.context = context

        self.menu_user = (By.XPATH, '//button[@title="Abrir menú de usuario"]')
        self.centroAyudaLink = (By.LINK_TEXT, 'Centro de ayuda')
        self.technical_issue = (By.XPATH, '//*[@id="formIncidents"]/label[2]/div/select')
        self.web_issue = (By.XPATH, '//*[@id="formIncidents"]/label[3]/div/select')
        self.inputMessage = (By.ID, 'inputMessage')
        self.inputConditions = (By.ID, 'inputConditions')
        self.button_enviar = (By.CSS_SELECTOR, '.style__StyledButton-sc-7c5qki-1.dWUoVC.button-primary'
                                               '.style__StyledButton-sc-1gb8dpy-12.cJGrJe.vjs-btn-enviar')
        self.ok_message = (By.XPATH, '//p[text()=\'Tu mensaje se ha enviado correctamente.\']')

    def open_user_menu(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.menu_user)
        ).click()
        print("Clicking on 'Abrir menú de usuario' button...")

    def navigate_to_help(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.centroAyudaLink)
        ).click()
        print("Clicking on 'Centro de ayuda' link...")

        expected_url = 'https://www.atresplayer.com/usuario/centro-de-ayuda'
        assert self.context.driver.current_url == expected_url, f"Expected url: '{expected_url}', but got '{self.context.driver.current_url}'"
        print(f"Current url: {self.context.driver.current_url}")

    def select_technical_issue(self):
        dropdown = WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.technical_issue)
        )
        select = Select(dropdown)
        select.select_by_visible_text('Técnica')
        print("Clicking on 'Técnica' dropdown...")

    def select_web_issue(self):
        dropdown2 = WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.web_issue)
        )
        select2 = Select(dropdown2)
        select2.select_by_visible_text('Web')
        print("Clicking on 'Web' dropdown...")

    def enter_message(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.inputMessage)
        ).send_keys('Otros asuntos')
        print("Entering message...")

    def accept_conditions(self):
        checkbox = WebDriverWait(self.context.driver, 30).until(
            EC.presence_of_element_located(self.inputConditions)
        )
        self.context.driver.execute_script("arguments[0].click();", checkbox)
        print("Accepting checkbox conditions...")

    def click_send(self):
        button_enviar = WebDriverWait(self.context.driver, 30).until(
            EC.element_to_be_clickable(self.button_enviar)
        )
        button_enviar.click()
        print("Clicking on Enviar")

    def check_ok_message(self):
        mensaje_enviado = WebDriverWait(self.context.driver, 30).until(
            EC.presence_of_element_located(self.ok_message)
        )
        print("Message sent successfully")
