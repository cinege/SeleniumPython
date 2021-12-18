# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import PageObjects.LoginPage as LoginPage
import unittest, logging

class Main(unittest.TestCase):
    STATUSES = []
    COMMENTS = []
    def setUp(self):
        self.open_Chrome()

    def open_Chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()
      
    def assertion(self, success, success_message, fail_message):
        """ if success True than success message is added otherwise failure message and the script terminates with an assert exception""" 
        self.STATUSES.append(("Failed", "Passed", ) [success])
        self.COMMENTS.append((fail_message, success_message) [success])
        print(self.COMMENTS)
        print(success)
        assert success
        
