from behave import *
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from variables.variables import *

use_step_matcher("re")


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)


@given(u"I navigated to 'https://www.atresplayer.com/' and I logged into my account")
def step_impl(context):
    url = 'https://www.atresplayer.com/'
    context.driver.get(url)
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "acceptAllMain"))
    ).click()

    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Entra o Regístrate"]'))
    ).click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(email)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[3]/div[2]/input').send_keys(
        password)
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[2]/div[3]/button'))
    ).click()

    try:
        print("comprobando url")
        if WebDriverWait(context.driver, 10).until(url_contains('https://www.atresplayer.com/')):
            print("Login successful")
        elif WebDriverWait(context.driver, 10).until(
                url_contains('https://atresplayer.com/usuario/cuenta/suscripcion-y-paquetes')):
            home_button_xpath = '//img[@alt="Inicio Atresplayer"]'
            WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, home_button_xpath))
            ).click()
            WebDriverWait(context.driver, 10).until(url_contains('https://www.atresplayer.com/'))
            print("Login successful")
    except WebDriverException as e:
        print(f"Error checking URL: {e}")
