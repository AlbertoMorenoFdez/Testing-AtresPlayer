from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FavoritePage:
    def __init__(self, context):
        self.context = context

        self.canales = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[1]/a/span')
        self.megaLink = (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[5]/a/span[text()="Mega"]')
        self.casaemepenos = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/section[1]/div[2]/div/div['
                                       '1]/div/ul/li[6]/a/div')
        self.detallesLink = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/div[3]/div/ol/li[text()="Detalles"]')
        self.botonSeguir = (By.XPATH, '//button[@title="Seguir este contenido"]')
        self.menu_user = (By.XPATH, '//button[@title="Abrir menú de usuario"]')
        self.miAtresplayerLink = (By.XPATH, '//a[@title="Ir a Mi Atresplayer"]')
        self.titleContenidoSeguido = (By.XPATH, '//a[@title="La casa de empeños"]')

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

    def click_on_follow(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.botonSeguir)
        ).click()

    def open_user_menu(self):
        WebDriverWait(self.context.driver, 10).until(
            EC.element_to_be_clickable(self.menu_user)
        ).click()
        print("Clicking on 'Abrir menú de usuario' button...")

    def click_on_go_to_my_atresplayer(self):
        try:
            my_atresplayer_link = WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(self.miAtresplayerLink)
            )
            my_atresplayer_link.click()
            print("Clicking on 'Ir a Mi Atresplayer' link...")
        except WebDriverException as e:
            print(f"Error al buscar el enlace 'Ir a Mi Atresplayer': {e}")

    def check_title(self):
        try:
            element = WebDriverWait(self.context.driver, 10).until(
                EC.visibility_of_element_located(self.titleContenidoSeguido)
            )

            element_title = element.get_attribute("title")

            assert element_title == "La casa de empeños", (f"El título del enlace es {element_title}, se esperaba 'La "
                                                           f"casa de empeños'")

            print("El texto del atributo title coincide con 'La casa de empeños'")
        except Exception as e:
            print(f"Error: {str(e)}")
