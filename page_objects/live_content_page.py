
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LiveContentPage:
    def __init__(self, context):
        self.context = context

        self.linkDirectos = (By.LINK_TEXT, 'Directos')
        self.continuarDirecto = (By.XPATH, '//button[p[text()="Continuar Directo"]]')
        self.expected_url = 'https://www.atresplayer.com/directos/antena3'

    def get_live_content(self):
        try:
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(self.linkDirectos)).click()
            WebDriverWait(self.context.driver, 10).until(
                EC.element_to_be_clickable(self.continuarDirecto)).click()
        except Exception as e:
            print(f"Error: {e}")

    def check_live_content(self):
        try:
            WebDriverWait(self.context.driver, 30).until(EC.url_to_be(self.expected_url))
            assert self.context.driver.current_url == self.expected_url, f"Expected '{self.expected_url}', but got '{self.context.driver.current_url}'"
            print("Live content displayed")
        except Exception as e:
            print(f"Error: {e}")
