from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SharePage:
    def __init__(self, context):
        self.context = context

        self.canales = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[1]/a/span')
        self.megaLink = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[5]/a/span[text()="Mega"]')
        self.casaemepenos = (
            By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/section[1]/div[2]/div/div[1]/div/ul/li[6]/a/div')
        self.detallesLink = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/div[3]/div/ol/li[text()="Detalles"]')
        self.compartirButton = (By.XPATH, '//button[@title="Compartir"]')
        self.facebookButton = (By.XPATH, "//button[@aria-label='facebook']")
        self.nuevaVentana = (By.ID, "content")

    def acceder_a_la_casa_de_empenos(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.canales)
        ).click()
        print("Accedo a canales")

        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.megaLink)
        ).click()
        print("Accedo a Mega")

        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.casaemepenos)
        ).click()
        print("Accedo a La casa de empeños")

    def click_on_details(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(
                self.detallesLink)
        ).click()
        print("Click en Detalles")

    def click_on_compartir(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.compartirButton)
        ).click()
        print("Click en Compartir")

    def click_on_facebook(self):
        button_facebook = WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.facebookButton)
        )
        print("Botón Facebook localizado")
        button_facebook.click()
        print("Click en Facebook")

    def check_new_window(self):
        ventana_nueva = self.context.driver.window_handles[-1]
        self.context.driver.switch_to.window(ventana_nueva)

        elemento_content = WebDriverWait(self.context.driver, 10).until(
            EC.presence_of_element_located(self.nuevaVentana)
        )
        print("Elemento con id 'content' localizado")

        self.context.driver.close()

        ventana_anterior = self.context.driver.window_handles[0]
        self.context.driver.switch_to.window(ventana_anterior)
