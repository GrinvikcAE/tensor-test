from selenium.webdriver.common.by import By


class FirstScenario:
    FIRST_URL = 'https://sbis.ru/'
    SECOND_URL = 'https://tensor.ru/'
    THIRD_URL = 'https://tensor.ru/about'
    LOCATOR_CONTACTS = (By.LINK_TEXT, 'Контакты')
    LOCATOR_TENSOR_IMAGE = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    LOCATOR_BLOCK_TEXT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    LOCATOR_ABOUT_TEXT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    LOCATOR_WORK_TEXT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    LOCATOR_IMAGE_1 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')
    LOCATOR_IMAGE_2 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img')
    LOCATOR_IMAGE_3 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img')
    LOCATOR_IMAGE_4 = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img')


class SecondScenario:
    FIRST_URL = 'https://sbis.ru/'
    NEW_URL_CONTAINS = '41-kamchatskij-kraj'
    NEW_URL_TITLE_CONTAINS = 'Камчатский'
    LOCATOR_CONTACTS = (By.LINK_TEXT, 'Контакты')
    LOCATOR_PARTNERS = (By.NAME, 'itemsContainer')
    LOCATOR_REGION_CHOICES = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    LOCATOR_REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')


class ThirdScenario:
    FIRST_URL = 'https://sbis.ru/'
    LOCATOR_DOWNLOAD = (By.PARTIAL_LINK_TEXT, 'Скачать')
    LOCATOR_PLUGIN = (By.XPATH, '//*[@name="TabButtons"]/div[2]/div[2]')
    LOCATOR_PLUGIN_DOWNLOAD = (By.PARTIAL_LINK_TEXT, 'Скачать (Exe ')


