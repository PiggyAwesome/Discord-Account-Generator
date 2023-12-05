## NOTE: If you are looking for a better account generator, look at https://sellix.io/Pig-Services

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string
from handlers import *

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.get("https://discord.com/register")


##############

speedMultiplier = 5 # Higher speed = more difficult captcha

##########

class InputSelectors:
    emailinput = "#uid_5"
    displaynameInput = "#uid_6"
    usernameInput = "#uid_7"
    passwordInput = "#uid_8"
    continueButton = "button[type='submit']"
    tosCheckbox = '#app-mount > div.appAsidePanelWrapper__714a6 > div.notAppAsidePanel__9d124 > div.app_b1f720 > div > div > div > form > div.centeringWrapper__319b0 > div > div.flex_f5fbb7.horizontal__992f6.justifyStart__42744.alignCenter__84269.noWrap__5c413.marginTop20_d88ee7 > label > div.checkbox_c7f690.box__66058'


# try:
#     driver.find_element(By.XPATH, phonecancel).click() # Check if the register with phone number window appears
# except NoSuchElementException:
#     pass



sleep(2)

### Generate the login details ###
username = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
email = ''.join(random.choice(string.ascii_letters) for i in range(5)) + '@' +  ''.join(random.choice(string.digits + string.ascii_letters) for i in range(5)) + '.' + ''.join(random.choice(string.ascii_letters) for i in range(3))  
password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
##################################


# Find the email input field and type the email
elmnt = Element(driver.find_element(By.NAME, "email"))
elmnt.click().typeSlow(email, speedMultiplier)


# Find the display name input field and type the display name
elmnt = Element(driver.find_element(By.NAME, "global_name"))
elmnt.click().typeSlow(username, speedMultiplier)


# Find the username input field and type the username
elmnt = Element(driver.find_element(By.NAME, "username"))
elmnt.click().typeSlow(username, speedMultiplier)


# Find the password input field and type the password
elmnt = Element(driver.find_element(By.NAME, "password"))
elmnt.click().typeSlow(password, speedMultiplier)




dobber = DOBNavigator(driver)

dobber.openMenu("day")
selection = dobber.chooseElement(dobber.getMenuObject().getChildren())
selection.scrollIntoView(actions).click()
sleep(0.5/speedMultiplier)


dobber.openMenu("month")
selection = dobber.chooseElement(dobber.getMenuObject().getChildren())
selection.scrollIntoView(actions).click()
sleep(0.5/speedMultiplier)


dobber.openMenu("year")
selection = dobber.chooseElement(dobber.getMenuObject().getChildren())
selection.scrollIntoView(actions).click()
sleep(0.5/speedMultiplier)


try:
    driver.find_element(By.CSS_SELECTOR, InputSelectors.tosCheckbox).click() # Accept TOS
    sleep(0.3/speedMultiplier)
except NoSuchElementException:  # Sometimes the checkbox doesnt appear
    pass


driver.find_element(By.CSS_SELECTOR, InputSelectors.continueButton).click()      # Continue

print('')
print(r'   __ _ _ _   _                         _       _           ')
print(r'  / _(_) | | (_)                       | |     | |          ')
print(r' | |_ _| | |  _ _ __     ___ __ _ _ __ | |_ ___| |__   __ _ ')
print(r' |  _| | | | | | `_ \   / __/ _` | `_ \| __/ __| `_ \ / _` |') 
print(r' | | | | | | | | | | | | (_| (_| | |_) | || (__| | | | (_| |')   # Tells user to solve captcha
print(r' |_| |_|_|_| |_|_| |_|  \___\__,_| .__/ \__\___|_| |_|\__,_|')
print(r'                                 | |                        ')
print(r'                                 |_|                        ')


input('Press ENTER to get 0Auth token.')  # Waits for user to solve captcha before moving on


token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"') # Get the token


sleep(5)

print(f'Made account:')
print(f'{email}:{password}:{username}:{token}')

sleep(5)
driver.close() 
