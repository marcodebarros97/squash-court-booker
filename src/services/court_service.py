from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Elements that we will need here
# Interacting with the Calendar
# Table rows are structured by time- 30 minute increments so 1 hour is two blocks
table_row_time_slot_element = 'data-time'
# Type will be free/taken/blocked so find by free
time_slot_type_element = 'free'
# for example squash 1 is court 1
squash_court_number_title = 'title'


def map_free_squash_courts(free_time_slots, input_time):
    squash_courts = {}

    for time_slot in free_time_slots:
        free_squash_courts = time_slot.find_elements(By.CSS_SELECTOR, '[type="free"]')
        for squash_court in free_squash_courts:
            squash_court_number = squash_court.get_attribute("title")
            squash_courts[squash_court_number] = squash_court

    return squash_courts


def find_all_open_courts(driver: WebDriver, first_time_slot: str):
    table_id = driver.find_element(By.ID, 'tbl_matrix')
    table_body = table_id.find_element(By.TAG_NAME, 'tbody')
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    first_time_slots = []

    for row in table_rows:
        first_time_slots.extend(row.find_elements(By.CSS_SELECTOR, f'[data-time="{first_time_slot}"]'))

    return map_free_squash_courts(first_time_slots, first_time_slot)
