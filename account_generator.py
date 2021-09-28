## NOTE:his gen shit lolz

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
try:
 driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div/div/div[1]/div[1]/div[2]').click() # Check if the register with phone number window appears
except NoSuchElementException:
  pass



sleep(2)
### Generate the login details ###
username = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
email = ''.join(random.choice(string.ascii_letters) for i in range(10)) + '@' +  ''.join(random.choice(string.digits + string.ascii_letters) for i in range(7)) + '.' + ''.join(random.choice(string.digits + string.ascii_letters) for i in range(3))  
password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
##################################

### Generate the bith date ###
year = [1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]
months = ['//*[@id="react-select-2-option-0"]', '//*[@id="react-select-2-option-1"]', '//*[@id="react-select-2-option-2"]', '//*[@id="react-select-2-option-3"]', '//*[@id="react-select-2-option-4"]', '//*[@id="react-select-2-option-5"]', '//*[@id="react-select-2-option-6"]', '//*[@id="react-select-2-option-7"]', '//*[@id="react-select-2-option-8"]', '//*[@id="react-select-2-option-9"]', '//*[@id="react-select-2-option-10"]', '//*[@id="react-select-2-option-11"]']
monthwords = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
day = str(random.randint(1,28))
###############################

# Find the email input field and type the email
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(email)

# Find the username input field and type the username
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(username)

# Find the password input field and type the password
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(password)

# Find the Date of Birth section and fill it in
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div[1]').click()
driver.find_element_by_xpath(random.choice(months)).click() # Month
actions.send_keys(Keys.ENTER)

actions.send_keys(day) # Day
actions.send_keys(Keys.ENTER)

actions.send_keys(str(random.choice(year))) # Year
actions.send_keys(Keys.ENTER)

actions.perform()

try:
 driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[5]/label/input').click() # Accept TOS
except NoSuchElementException:  # Sometimes the checkbox doesnt appear
  pass
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[5]/button').click()      # Continue
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div[1]/div[1]').click.send_keys(monthwords).send_keys(Keys.ENTER)

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
