import logging
import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username_input_box_name = 'username'
password_input_box_name = 'password'
calendar_title = 'calendar_date_title'
login_button = "//div[@class='form-submit3']//button[@class='button3 fw']"

USERNAME = str(os.getenv('USERNAME'))
PASSWORD = str(os.getenv('PASSWORD'))


def perform_login(driver: WebDriver):
    username_input_field = driver.find_element(By.NAME, username_input_box_name)
    password_input_field = driver.find_element(By.NAME, password_input_box_name)

    if username_input_field is not None and password_input_field is not None:
        username_input_field.send_keys(USERNAME)
        password_input_field.send_keys(PASSWORD)
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, calendar_title)))
        if driver.find_element(By.ID, calendar_title):
            print('Login to booking system was successful')
            logging.info('Login to booking system was successful')
            return True
        else:
            return False
