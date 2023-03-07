import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.getenv('BASE_URL')

# Example of URL to use to get to specific date-
# https://kampongsquash.baanreserveren.nl/reservations/2023-3-7/sport/893

# Take a screenshot of booking and email to me but squash system will also email it

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(BASE_URL)
