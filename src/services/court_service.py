from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

table_row_time_slot_element = 'data-time'
slot_type = '[type="free"]'
squash_court_number_title = 'title'
table_name = 'tbl_matrix'
tr = 'tr'
tbody = 'tbody'


def map_free_squash_courts(free_time_slots, input_time):
    squash_courts = {}

    for time_slot in free_time_slots:
        free_squash_courts = time_slot.find_elements(By.CSS_SELECTOR, slot_type)
        for squash_court in free_squash_courts:
            squash_court_number = squash_court.get_attribute(squash_court_number_title)
            squash_courts[squash_court_number] = squash_court

    return squash_courts


def find_all_open_courts(driver: WebDriver, first_time_slot: str):
    corresponding_time_slot = f'[data-time="{first_time_slot}"]'
    table_id = driver.find_element(By.ID, table_name)
    table_body = table_id.find_element(By.TAG_NAME, tbody)
    table_rows = table_body.find_elements(By.TAG_NAME, tr)
    first_time_slots = []

    for row in table_rows:
        first_time_slots.extend(row.find_elements(By.CSS_SELECTOR, corresponding_time_slot))

    return map_free_squash_courts(first_time_slots, first_time_slot)
