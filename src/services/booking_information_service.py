import os

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

SECOND_PLAYER_FIRST_NAME = str(os.getenv('SECOND_PLAYER_FIRST_NAME'))
SECOND_PLAYER_LAST_NAME = str(os.getenv('SECOND_PLAYER_LAST_NAME'))


def book_free_squash_court(driver: WebDriver, free_squash_courts: dict, end_time: str):
    for key, value in free_squash_courts.items():
        value.click()
        form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

        end_time_field = form.find_element(By.NAME, end_time_drop_down_name)
        if end_time_field.get_attribute("type") == 'hidden':
            driver.find_element(By.CSS_SELECTOR, '[onclick*="return hideLightbox(), false"]').click()
            continue
        else:
            end_time_drop_down_select = Select(form.find_element(By.NAME, end_time_drop_down_name))
            end_time_drop_down_select.select_by_visible_text(end_time)

            search_box = form.find_element(By.CLASS_NAME, 'ms-search')
            search_box.send_keys(SECOND_PLAYER_FIRST_NAME)

            driver.implicitly_wait(10)

            search_box_select = Select(form.find_element(By.NAME, 'players[2]'))

            selected_player = search_box_select.select_by_visible_text('Stehan Du Ploy')
            print(selected_player.get_attribute('value'))
