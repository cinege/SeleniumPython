from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)
       self.logs = self.driver.get_log("browser")
    def openurl(self, locator, URL):
       self.driver.get(URL)
    def is_element_present(self, locator, argument):
       try: self.driver.find_element(*locator)
       except NoSuchElementException as e: return False
       return True
    def fill(self, locator, value):
       self.wait.until(lambda driver: driver.find_element(*locator))
       self.driver.find_element(*locator).clear()
       self.driver.find_element(*locator).send_keys(value)
    def click(self, locator, argument):
       self.wait.until(lambda driver: driver.find_element(*locator))
       self.driver.find_element(*locator).click()
    def selectbytext(self, locator, visibletext):
       self.wait.until(lambda driver: driver.find_element(*locator))
       select = Select(self.driver.find_element(*locator)).select_by_visible_text(visibletext)
    def selectbyindex(self, locator, index):
       self.wait.until(lambda driver: driver.find_element(*locator))
       Select(self.driver.find_element(*locator)).select_by_index(index)
    def gettext(self, locator, argument):
       self.wait.until(lambda driver: driver.find_element(*locator))
       elements =  self.driver.find_elements(*locator)
       return "Not found" if len(elements) == 0 else elements[0].text
    def getselection(self, locator, argument):
       self.wait.until(lambda driver: driver.find_element(*locator))
       return Select(self.driver.find_element(*locator)).first_selected_option.text
    def ischecked(self, locator, argument):
       self.wait.until(lambda driver: driver.find_element(*locator))
       return self.driver.find_element(*locator).is_selected()
    def is_alert_present(self, locator, argument):
       try: self.driver.switch_to_alert()
       except NoAlertPresentException as e: return False
       return True
    def close_alert_and_get_its_text(self, locator, argument):
       try:
          alert = self.driver.switch_to_alert()
          alert_text = alert.text
          if self.accept_next_alert:
            alert.accept()
          else:
            alert.dismiss()
            return alert_text
       finally: self.accept_next_alert = True
    def count_elements(self, locator, argument):
       return len(self.driver.find_elements(*locator))