import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverTests(unittest.TestCase):
    def test_webdriver_setup(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
        self.assertNotEqual(None, search_box)