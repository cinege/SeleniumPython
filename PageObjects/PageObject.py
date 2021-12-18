import json, os
from .BasePage import BasePage
from selenium.webdriver.common.by import By

class PageObject(BasePage):
    def __init__(self, driver, json_filename):
        super().__init__(driver)
        json_path = os.path.realpath('') + "\\PageObjects\\" + json_filename
        self.json_file_handle = open(json_path, 'r')
        self.dict = json.load(self.json_file_handle)
        self.json_file_handle.close()
        
    def do(self, method, arguments):
        """ Triggers the login """
        function = None
        for f in self.dict.get("Functions"):
            if f.get("name") == method:
                function = f
                break
        args_dict = dict(zip(function.get("arguments"), arguments))
        for action in function.get("actions"):
            methodname = action.get("method")
            locatorname = action.get("locator")
            locator = None
            for locator_entry in self.dict.get("Locators"):
                if locator_entry.get("name") == locatorname:
                   tag = locator_entry.get("tag")
                   value = locator_entry.get("value")
                   if tag == "ID":
                      locator = (By.ID, value)
                   elif tag == "NAME":
                      locator = (By.NAME, value)
                   elif tag == "XPATH":
                      locator = (By.XPATH, value)
                   break
            argument = args_dict.get(action.get("argument_variable"))
            func = getattr(self, methodname)
            result = func(locator, argument)
            
        return result

