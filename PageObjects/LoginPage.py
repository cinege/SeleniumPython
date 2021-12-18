from .BasePage import BasePage
from selenium.webdriver.common.by import By

class Locators:
    LOGIN_USERNAME = (By.ID, 'focusme')
    LOGIN_PASSWORD = (By.NAME, 'pass')
    LOGIN_BUTTON = (By.XPATH, "//input[@type='image']")
    
class LoginPage(BasePage):
    def login(self, URL, USERNAME, PASSWORD):
        """ Triggers the login """
        self.openurl(URL)
        self.fill(Locators.LOGIN_USERNAME, USERNAME)
        self.fill(Locators.LOGIN_PASSWORD, PASSWORD)
        self.click(Locators.LOGIN_BUTTON)
        
        
        

