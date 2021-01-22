#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#     -this code is written in Python 3 to demonstrate Python based automation framework showing experience writing
#     automation tests using Python and using Selenium and building test frameworks with unittest API

import unittest
from selenium import webdriver

from src.main.python.com.bryancutkelvin.page import HomePageObject


class PythonAutomationDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("src/main/python/com/bryancutkelvin/drivers/chromedriver")
        self.driver.get("https://bryancutkelvin.com/")

    def test_window_create(self):
        driver = self.driver
        print("test_window_create")
        self.assertIn("https://bryancutkelvin.com/", driver.current_url, 'FAIL - Not on page')

    def test_home_page(self):
        # load page
        homepageload = HomePageObject.HomePage(self.driver)
        assert homepageload.test_page_title(), "FAIL - page title is incorrect"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
