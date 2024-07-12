from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlayContentPage:
    def __init__(self, context):
        self.context = context

        self.canalesLink = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[1]/a/span')
        self.megaLink = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[5]/a/span[text()="Mega"]')
        self.casaempenos = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/section[1]/div[2]/div/div[1]/div/ul/li[6]/a/div')
        self.verAhoraButton = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/div[1]/section/div/div[2]/div[3]/div/button/p[text()="Ver ahora"]')
        self.modal = (By.ID, 'portal-modal-container')
        self.click_ultima_temporada = (By.XPATH, '//*[@id="portal-modal-container"]/div/div/div/div/div/button[1]/p[text()="Última temporada"]')
        self.containerVideo = (By.CLASS_NAME, 'playerContainer video ')
        self.barraProgreso = (By.CLASS_NAME, 'vjs-load-progress')

    def acceder_a_la_casa_de_empenos(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.canalesLink)
        ).click()
        print("Accedo a canales")

        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.megaLink)
        ).click()
        print("Accedo a Mega")

        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.casaempenos)
        ).click()
        print("Accedo a La casa de empeños")

    def click_on_ver_ahora(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.verAhoraButton)
        ).click()
        print("Click en Ver ahora")

    def click_on_ultima_temporada(self):
        WebDriverWait(self.context.driver, 30).until(EC.visibility_of_element_located(self.modal))
        print("Localizado modal")
        self.context.driver.find_element(*self.click_ultima_temporada).click()
        print("Click en última temporada")

    def check_video_container(self):
        ads_container = WebDriverWait(self.context.driver, 30).until(
            EC.visibility_of_element_located(self.containerVideo))
        print("Localizado contenedor de video")
        try:
            barra_progreso = WebDriverWait(self.context.driver, 30).until(
                EC.visibility_of_element_located(self.barraProgreso))
            print("La barra de progreso se encontró exitosamente.")
        except Exception as e:
            print("El botón no se encontró.")