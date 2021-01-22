#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#     -this code is written in Python 3 for for educational purposes to demonstrate
#     experience using a Python based automation framework, i.e showing experience
#     writing writing Page Elements for Page Objects for use with automation
#     framework tests using Python for use with automation tests
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base class to initialize the base page"""

    def __init__(self):
        self.locator = None

    """for setting text to value supplied"""
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    """for getting text of specified object"""
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
