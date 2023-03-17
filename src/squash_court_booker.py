import os
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from services import login_service, court_service, booking_information_service
from utils import date_util
from utils import time_slot_util

EMPTY_STRING = ''
EMPTY_SPACE = ' '
BASE_URL = str(os.getenv('BASE_URL'))
BOOKING_DATE = str(os.getenv('BOOKING_DATE'))
FIRST_SLOT = str(os.getenv('FIRST_SLOT'))
SLOT_TIME_LIMIT = int(os.getenv('SLOT_TIME_LIMIT'))


options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(BASE_URL)

login_form_container = 'login-form-container'
page_title = 'matrix_date_title'

if driver.find_element(By.ID, login_form_container) is not None:

    print('Correct Page Retrieved, Performing Login')
    logging.info('Correct Page Retrieved, Performing Login')
    login_successful = login_service.perform_login(driver)

    if login_successful:
        print(BOOKING_DATE)
        if BOOKING_DATE is None or BOOKING_DATE == EMPTY_STRING or BOOKING_DATE == EMPTY_SPACE:
            BOOKING_DATE = date_util.add_one_week_to_date()

        date_to_book_url = f'https://kampongsquash.baanreserveren.nl/reservations/{BOOKING_DATE}/sport/893'
        driver.get(date_to_book_url)
        booking_system_date = driver.find_element(By.ID, page_title).text

        if BOOKING_DATE in booking_system_date:
            print(f'Calendar set to day: {booking_system_date}')
            logging.info(f'Calendar set to day: {booking_system_date}')
            slot_end_time = time_slot_util.add_one_hour_to_time(first_slot=FIRST_SLOT, minutes_to_add=SLOT_TIME_LIMIT)
            free_squash_courts = court_service.find_all_open_courts(driver, FIRST_SLOT)
            if free_squash_courts.__sizeof__() > 0:
                squash_court_booked = booking_information_service.book_free_squash_court(driver=driver,
                                                                                         free_squash_courts=free_squash_courts,
                                                                                         end_time=slot_end_time)
                print(f'Squash Court Booked {squash_court_booked}')
            else:
                print("No free courts")
