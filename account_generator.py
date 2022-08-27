## NOTE: If you are looking for a better account generator, look at https://sellix.io/Pig-Services

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
actions = ActionChains(driver)
actions2 = ActionChains(driver)
actions3 = ActionChains(driver)
driver.get("https://discord.com/register")


##############

speedMultiplier = 5 # Higher speed = more difficult captcha

##########

phonecancel = "/html/body/div/div[2]/div/div/form/div/div/div[1]/div[1]/div[2]"
emailinput = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[1]/div/input"
usernameInput = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[2]/div/input"
passwordInput = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[3]/div/input"
dayInput = '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[1]/div/div/div/div[1]/div[1]'
continueButton = '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/button/div'
tosCheckbox = '/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/label/input'


def typeSlow(string):
  for x in string:
    actions.send_keys(x)
    actions.perform()
    sleep(random.choice([0.1, 0.2, 0.3, 0.5])/speedMultiplier)

try:
  driver.find_element(By.XPATH, phonecancel).click() # Check if the register with phone number window appears
except NoSuchElementException:
  pass



sleep(2)
### Generate the login details ###
username = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
email = ''.join(random.choice(string.ascii_letters) for i in range(5)) + '@' +  ''.join(random.choice(string.digits + string.ascii_letters) for i in range(5)) + '.' + ''.join(random.choice(string.ascii_letters) for i in range(3))  
password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
##################################

### Generate the bith date ###
year = str(random.randint(1970, 2000))
monthwords = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
day = str(random.randint(1,28))
###############################

# Find the email input field and type the email
driver.find_element(By.XPATH, emailinput).click()
typeSlow(email)

# Find the username input field and type the username
# driver.find_element(By.XPATH, usernameInput).click() 
driver.find_element(By.XPATH, usernameInput).click()
typeSlow(username)


# Find the password input field and type the password
driver.find_element(By.XPATH, passwordInput).click()
typeSlow(password)

# Find the Date of Birth section and fill it in
driver.find_element(By.XPATH, dayInput).click()
sleep(1/speedMultiplier)


typeSlow(str(day)) # Day
actions.send_keys(Keys.ENTER)
actions.perform()

sleep(0.5/speedMultiplier)

typeSlow(random.choice(monthwords)) # Month
actions.send_keys(Keys.ENTER)
actions.perform()



sleep(0.4/speedMultiplier)

typeSlow(year) # Year
actions.send_keys(Keys.ENTER)
actions.perform()

sleep(0.5/speedMultiplier)

try:
 driver.find_element(By.XPATH, tosCheckbox).click() # Accept TOS
except NoSuchElementException:  # Sometimes the checkbox doesnt appear
  pass

sleep(0.3/speedMultiplier)

driver.find_element(By.XPATH, continueButton).click()      # Continue

print('')
print('   __ _ _ _   _                         _       _           ')
print('  / _(_) | | (_)                       | |     | |          ')
print(' | |_ _| | |  _ _ __     ___ __ _ _ __ | |_ ___| |__   __ _ ')
print(' |  _| | | | | | `_ \   / __/ _` | `_ \| __/ __| `_ \ / _` |') 
print(' | | | | | | | | | | | | (_| (_| | |_) | || (__| | | | (_| |')   # Tells user to solve captcha
print(' |_| |_|_|_| |_|_| |_|  \___\__,_| .__/ \__\___|_| |_|\__,_|')
print('                                 | |                        ')
print('                                 |_|                        ')


input('Press ENTER to get 0Auth token.')  # Waits for user to solve captcha before moving on


token = driver.execute_script('location.reload();var i=document.createElement("iframe");document.body.appendChild(i);return i.contentWindow.localStorage.token').strip('"') # Get the token


sleep(5)

print(f'Made account:')
print(f'{email}:{password}:{username}:{token}')

sleep(5)
driver.close() 
