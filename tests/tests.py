import os
# import logging
from config import DOWNLOAD_DIR
from selenium import webdriver
from pages.base import BasePage
from pages.scenario import FirstScenario, SecondScenario, ThirdScenario
from config import SLEEP_TIME, LOCAL_REGION
from time import sleep


def test_first_scenario(driver=webdriver.Chrome()):
    main_page = BasePage(driver, FirstScenario.FIRST_URL, SLEEP_TIME)
    main_page.click_element(FirstScenario.LOCATOR_CONTACTS, SLEEP_TIME)

    main_page.click_element(FirstScenario.LOCATOR_TENSOR_IMAGE, SLEEP_TIME)
    driver.switch_to.window(driver.window_handles[1])
    assert main_page.get_current_url() == FirstScenario.SECOND_URL
    main_page.find_element(FirstScenario.LOCATOR_BLOCK_TEXT, SLEEP_TIME)

    button = main_page.find_element(FirstScenario.LOCATOR_ABOUT_TEXT, SLEEP_TIME)

    driver.execute_script('arguments[0].click();', button)
    assert main_page.get_current_url() == FirstScenario.THIRD_URL
    main_page.find_element(FirstScenario.LOCATOR_WORK_TEXT, SLEEP_TIME)
    size_1 = main_page.find_element(FirstScenario.LOCATOR_IMAGE_1, SLEEP_TIME).size
    size_2 = main_page.find_element(FirstScenario.LOCATOR_IMAGE_2, SLEEP_TIME).size
    size_3 = main_page.find_element(FirstScenario.LOCATOR_IMAGE_3, SLEEP_TIME).size
    size_4 = main_page.find_element(FirstScenario.LOCATOR_IMAGE_4, SLEEP_TIME).size
    assert size_1 == size_2 == size_3 == size_4


def test_second_scenario(driver=webdriver.Chrome()):
    main_page = BasePage(driver, SecondScenario.FIRST_URL, SLEEP_TIME)
    main_page.click_element(SecondScenario.LOCATOR_CONTACTS, SLEEP_TIME)
    sleep(SLEEP_TIME)
    assert main_page.find_element(SecondScenario.LOCATOR_REGION_CHOICES, SLEEP_TIME).text == LOCAL_REGION
    partners = main_page.find_element(SecondScenario.LOCATOR_PARTNERS, SLEEP_TIME).text
    main_page.click_element(SecondScenario.LOCATOR_REGION_CHOICES, SLEEP_TIME)
    sleep(SLEEP_TIME)
    main_page.click_element(SecondScenario.LOCATOR_REGION, SLEEP_TIME)
    sleep(SLEEP_TIME)
    assert SecondScenario.NEW_URL_CONTAINS in main_page.get_current_url()
    assert partners != main_page.find_element(SecondScenario.LOCATOR_PARTNERS, SLEEP_TIME).text
    assert SecondScenario.NEW_URL_TITLE_CONTAINS in main_page.get_title()


def test_third_scenario(driver=webdriver.Chrome()):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'download.default_directory': DOWNLOAD_DIR})
    driver = webdriver.Chrome(options=chrome_options)

    main_page = BasePage(driver, ThirdScenario.FIRST_URL, SLEEP_TIME)
    button = main_page.find_element(ThirdScenario.LOCATOR_DOWNLOAD, SLEEP_TIME)
    driver.execute_script('arguments[0].click();', button)
    sleep(SLEEP_TIME)
    main_page.click_element(ThirdScenario.LOCATOR_PLUGIN, SLEEP_TIME)
    sleep(SLEEP_TIME)
    download_text = main_page.find_element(ThirdScenario.LOCATOR_PLUGIN_DOWNLOAD, SLEEP_TIME).text.split()[-2]
    main_page.click_element(ThirdScenario.LOCATOR_PLUGIN_DOWNLOAD, SLEEP_TIME)
    sleep(30)
    if os.listdir(DOWNLOAD_DIR)[0].startswith('.'):
        file = os.listdir(DOWNLOAD_DIR)[1]
    else:
        file = os.listdir(DOWNLOAD_DIR)[0]
    file_size = round(os.stat(f'{DOWNLOAD_DIR}{file}').st_size / 1024 / 1024, 2)
    assert float(download_text) - 0.5 < file_size < float(download_text) + 0.5
    driver.quit()
