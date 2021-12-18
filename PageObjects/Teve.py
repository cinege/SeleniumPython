from .BasePage import BasePage
from selenium.webdriver.common.by import By

class Locators:
    HIBERNATE_MENU_BUTTON = (By.XPATH, u"//img[@alt='Hibernálom / felolvasztom a tevémet!']")
    
class Teve(BasePage):
    """ Login page action methods """
    def hibernate(self):
        self.click(Locators.HIBERNATE_MENU_BUTTON)
