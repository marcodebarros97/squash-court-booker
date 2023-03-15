import os
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.services import login_service, court_service, booking_information_service
from src.utils import time_slot_util

BASE_URL = str(os.getenv('BASE_URL'))
BOOKING_DATE = str(os.getenv('BOOKING_DATE'))
FIRST_SLOT = str(os.getenv('FIRST_SLOT'))
SLOT_TIME_LIMIT = int(os.getenv('SLOT_TIME_LIMIT'))

# Example of URL to use to get to specific date-
# https://kampongsquash.baanreserveren.nl/reservations/2023-3-7/sport/893

# Take a screenshot of booking and email to me but squash system will also email it

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(BASE_URL)
if driver.find_element(By.ID, 'login-form-container') is not None:
    print('Correct Page Retrieved, Performing Login')
    logging.info('Correct Page Retrieved, Performing Login')
    login_successful = login_service.perform_login(driver)

    if login_successful:
        driver.get(f'https://kampongsquash.baanreserveren.nl/reservations/{BOOKING_DATE}/sport/893')
        booking_system_date = driver.find_element(By.ID, "matrix_date_title").text

        if BOOKING_DATE in booking_system_date:
            print(f'Calendar set to day: {booking_system_date}')
            logging.info(f'Calendar set to day: {booking_system_date}')

            slot_end_time = time_slot_util.add_one_hour_to_time(first_slot=FIRST_SLOT, minutes_to_add=SLOT_TIME_LIMIT)

            free_squash_courts = court_service.find_all_open_courts(driver, FIRST_SLOT)

            if free_squash_courts.__sizeof__() > 0:
                booking_information_service.book_free_squash_court(driver=driver, free_squash_courts=free_squash_courts,
                                                                   end_time=slot_end_time)
            else:
                print("No free courts")

            driver.quit()
