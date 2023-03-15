from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Elements that we will need here
# Court end time selection- if not selectable then 1 hour not available
# Type != hidden
end_time_drop_down_name = 'end_time'

# Select block to reserve- reservation screen comes up
# Search for second player
player_search_box_class = 'ms-search'
# Select player from drop down-list of previous players booked against
player_selection_drop_down_class = 'br-user-select search guest br-user-selected'

# Next step of booking
next_step_of_booking_button_class = 'button submit'
next_step_of_booking_button_value = 'Verder'

# Complete booking
complete_booking_button_class = 'button submit'
complete_booking_button_value = 'Bevestigen'


def book_free_squash_court(driver: WebDriver, free_squash_courts: []):
    table_id = driver.find_element(By.ID, 'tbl_matrix')
    table_body = table_id.find_element(By.TAG_NAME, 'tbody')
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
