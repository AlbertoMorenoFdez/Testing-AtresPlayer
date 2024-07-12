from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonStepsPage:
    def __init__(self, driver):
        self.driver = driver

    def acceder_a_la_casa_de_empenos(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[1]/a/span'))
        ).click()
        print("Accedo a canales")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="menu-sections"]/nav/div/div[1]/ul/li[5]/a/span[text()="Mega"]'))
        ).click()
        print("Accedo a Mega")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="root"]/div/div[1]/div[3]/div/main/section[1]/div[2]/div/div['
                                        '1]/div/ul/li[6]/a/div'))
        ).click()
        print("Accedo a La casa de empeños")

    def click_on_details(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/main/div[3]/div/ol/li[text()="Detalles"]'))
        ).click()
        print("Click en Detalles")

    def open_user_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@title="Abrir menú de usuario"]'))
        ).click()
        print("Clicking on 'Abrir menú de usuario' button...")
