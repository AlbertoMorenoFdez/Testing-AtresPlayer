from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.atresplayer.com/'

    def navigate(self):
        self.driver.get(self.url)

    def is_at(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

