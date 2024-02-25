from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:
    _web_driver = None

    def __init__(self, web_driver, url='', time=10):
        self._web_driver = web_driver
        self.get(url, time)

    def get(self, url, time=10):
        self._web_driver.get(url)
        sleep(time)

    def get_current_url(self):
        current_url = ''
        try:
            current_url = self._web_driver.current_url
        except:
            print('Can\'t get current url')
        return current_url

    def get_title(self):
        current_title = ''
        try:
            current_title = self._web_driver.title
        except:
            print('Can\'t get current title')
        return current_title

    def find_element(self, locator, time=10):
        return WebDriverWait(self._web_driver, time).until(EC.presence_of_element_located(locator),
                                                           message=f'Can\'t find {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self._web_driver, time).until(EC.presence_of_all_elements_located(locator),
                                                           message=f'Can\'t find {locator}')

    def click_element(self, locator, time=10):
        return self.find_element(locator, time).click()
