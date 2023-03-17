import os

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

end_time_drop_down_name = 'end_time'

SECOND_PLAYER_FIRST_NAME = str(os.getenv('SECOND_PLAYER_FIRST_NAME'))
SECOND_PLAYER_LAST_NAME = str(os.getenv('SECOND_PLAYER_LAST_NAME'))

form_element = 'form'
hidden = 'hidden'
disabled_dropdown = '[onclick*="return hideLightbox(), false"]'
search_box_element = 'ms-search'
player_select_element = 'players[2]'


def book_free_squash_court(driver: WebDriver, free_squash_courts: dict, end_time: str):
    for key, value in free_squash_courts.items():
        value.click()
        form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, form_element)))
        end_time_field = form.find_element(By.NAME, end_time_drop_down_name)
        if end_time_field.get_attribute('type') == hidden:
            driver.find_element(By.CSS_SELECTOR, disabled_dropdown).click()
            continue
        else:
            try:
                player_name = SECOND_PLAYER_FIRST_NAME + " " + SECOND_PLAYER_LAST_NAME
                end_time_drop_down_select = Select(form.find_element(By.NAME, end_time_drop_down_name))
                end_time_drop_down_select.select_by_visible_text(end_time)

                search_box = form.find_element(By.CLASS_NAME, search_box_element)
                search_box.send_keys(SECOND_PLAYER_FIRST_NAME)
                search_box_select = Select(driver.find_element(By.NAME, player_select_element))
                search_box_select.select_by_visible_text(player_name)

                if search_box_select.first_selected_option.get_attribute('text') == player_name:
                    print("Correct Player Selected")
                    # form.find_element(By.ID, '__make_submit').click()
                    # # driver.save_screenshot('booking_confirmation.png')
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '__make_submit2'))).click()
                    return free_squash_courts[key].get_attribute('title')

            except UnexpectedAlertPresentException:
                print(driver.switch_to.alert.text)
            break
