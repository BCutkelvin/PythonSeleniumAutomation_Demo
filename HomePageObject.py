#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#     -this code is written in Python 3 to demonstrate Python based automation framework
#     showing experience writing Page Objects for use with automation tests using Python,
#     Selenium, JavaScript css selectors and DOM elements


class BasePage(object):
    """Base class to initialize the base page"""
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def test_page_title(self):
        """Verify page title is correct"""
        print("test page title")
        return "Bryan Cutkelvin: Web Development Portfolio" in self.driver.title
