from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)


@given(u"I navigated to '(?P<url>.+)'")
def step_impl(context, url):
    context.driver.get(url)
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "acceptAllMain"))
    ).click()
