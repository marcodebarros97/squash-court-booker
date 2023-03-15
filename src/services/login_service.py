# Elements that we will need here
import logging
import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

username_input_box_name = 'username'
password_input_box_name = 'password'
login_button_class = 'button3 fw'

USERNAME = str(os.getenv('USERNAME'))
PASSWORD = str(os.getenv('PASSWORD'))


def perform_login(driver: WebDriver):
    username_input_field = driver.find_element(By.NAME, 'username')
    password_input_field = driver.find_element(By.NAME, 'password')

    if username_input_field is not None and password_input_field is not None:
        username_input_field.send_keys(USERNAME)
        password_input_field.send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//div[@class='form-submit3']//button[@class='button3 fw']").click()
        if driver.find_element(By.ID, 'calendar_date_title'):
            print('Login to booking system was successful')
            logging.info('Login to booking system was successful')
            return True
        else:
            return False
