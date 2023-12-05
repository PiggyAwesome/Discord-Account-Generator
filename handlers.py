from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver import Chrome

class Element:
    def __init__(self, precursor: WebElement) -> None:
        self.precursor = precursor
        
    def click(self):
        self.precursor.click()
        return self

    def typeSlow(self, text: str, speedMultiplier):
        for x in text:
            self.precursor.send_keys(x)
            sleep(random.choice([0.1, 0.2, 0.3, 0.5])/speedMultiplier)
        return self
    
    def getChildren(self, tag="div"):
        return self.precursor.find_elements(By.TAG_NAME, tag)

    def scrollIntoView(self, actor: ActionChains):
        actor.move_to_element(self.precursor).perform()
        return self
    
class DOBNavigator:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.actiondriver = ActionChains(driver)
        self.min_year = 1970
        self.max_year = 2000
        self.section_type = None
        pass

    def openMenu(self, section_type):
        self.section_type = section_type

        match section_type:
            case "day":
                value = "[class*='day_']"
            case "month":
                value = "[class*='month_']"
            case "year":
                value = "[class*='year_']"
        self.driver.find_element(By.CSS_SELECTOR, value).click()
        return True

    def getMenuObject(self):
        return Element(self.driver.find_element(By.CSS_SELECTOR, "[class*='-menu']"))

    def chooseElement(self, elementList: list[WebElement]):
        chosen_element = random.choice(elementList)
        
        if self.section_type == "year":
            while int(chosen_element.text) < self.min_year or int(chosen_element.text) > self.max_year:
                chosen_element = random.choice(elementList)
                
        return Element(chosen_element)
