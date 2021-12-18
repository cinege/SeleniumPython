from .BasePage import BasePage
from selenium.webdriver.common.by import By

class Locators:
    HIBERNATE_BUTTON = (By.NAME, 'hiber')
    ACTIVATE_BUTTON = (By.NAME, 'dehiber')
    
class Hibernate(BasePage):
    """ Login page action methods """
    def hibernate(self):
        self.click(Locators.HIBERNATE_BUTTON)
    def dehibernate(self):
        self.click(Locators.ACTIVATE_BUTTON)