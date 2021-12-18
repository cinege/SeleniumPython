import unittest, logging, time, json
from main import Main
import PageObjects.PageObject as PageObject

class TTC(Main):
    def test_hibernation(self):
        URL = "https://teveclub.hu/"
        USERNAME = "Minciteve"
        PASSWORD = "gyereide"
        try:
            log = logging.getLogger("TTC.test_hibernation")
            loginpage = PageObject.PageObject(self.driver, 'login.json')
            tevepage = PageObject.PageObject(self.driver, 'teve.json')
            hibernationpage = PageObject.PageObject(self.driver, 'hibernate.json')
            
            loginpage.do("login", [URL, USERNAME, PASSWORD])
            tevepage.do("clickhibernate", [])
            hibernationpage.do("hibernate", [])
            tevepage.do("clickhibernate", [])
            hibernationpage.do("activate", [])
            
        except AssertionError as error:
            print(repr(error))
        
        except Exception as error:
            self.STATUSES.append("Fail")
            self.COMMENTS.append(repr(error).replace('"', ""))
            print(repr(error))
        
        finally:
            log.debug(self.BODY)

if __name__ == "__main__":
    unittest.main()  
        
