#!/usr/bin/env python3
#   Bryan Cutkelvin
#   2020
#     -this code is written in Python 3 for for educational purposes to demonstrate
#     experience using a Python based automation framework, i.e showing experience
#     writing Locator strings for Page Objects for use with automation tests
from selenium.webdriver.common.by import By


class HomePageLocators(object):
    PLAYSTATION_BUTTON = (By.CLASS_NAME, 'btn-primary btn-lg')
