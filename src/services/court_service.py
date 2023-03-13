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


def find_all_open_courts(driver: WebDriver, first_time_slot: str, second_time_slot: str):
    squash_courts = []
    table_id = driver.find_element(By.ID, 'tbl_matrix')
    table_body = table_id.find_element(By.TAG_NAME, 'tbody')
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    for row in table_rows:
        first_time_slots = row.find_elements(By.CSS_SELECTOR, f'[data-time="{first_time_slot}"]')
        second_time_slots = row.find_elements(By.CSS_SELECTOR, f'[data-time="{second_time_slot}"]')

        for time_slot in first_time_slots:
            free_time_slot = time_slot.find_element(By.CSS_SELECTOR, '[type="free"]')
            squash_court = free_time_slot.get_attribute("title")
            squash_courts.append(squash_court + first_time_slot)

        for time_slot in second_time_slots:
            free_time_slot = time_slot.find_element(By.CSS_SELECTOR, '[type="free"]')
            squash_court = free_time_slot.get_attribute("title")
            squash_courts.append(squash_court + second_time_slot)

    return squash_courts
