from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import random
from threading import Thread   #youtube_mute
import threading
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
actions = ActionChains(driver)
actions2 = ActionChains(driver)
actions3 = ActionChains(driver)
driver.get("https://discord.com/register")
try:
 driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div/div/div[1]/div[1]/div[2]')
except NoSuchElementException:
  pass



sleep(2)

username = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
email = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + '@' + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") +  '.' + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") + random.choice("abcdefghijklmnopqrstuvwxyz") 
password = random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890") + random.choice("abcdefghijklmnopqrstuvwxyz1234567890")

year = [1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]
months = ['//*[@id="react-select-2-option-0"]', '//*[@id="react-select-2-option-1"]', '//*[@id="react-select-2-option-2"]', '//*[@id="react-select-2-option-3"]', '//*[@id="react-select-2-option-4"]', '//*[@id="react-select-2-option-5"]', '//*[@id="react-select-2-option-6"]', '//*[@id="react-select-2-option-7"]', '//*[@id="react-select-2-option-8"]', '//*[@id="react-select-2-option-9"]', '//*[@id="react-select-2-option-10"]', '//*[@id="react-select-2-option-11"]']
monthwords = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
day = str(random.randint(1,28))
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[1]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[1]/div/input').send_keys(email)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[2]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[2]/div/input').send_keys(username)


driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[3]/div/input').click() 
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[3]/div/input').send_keys(password)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div/div[1]').click()
driver.find_element_by_xpath(random.choice(months)).click()
actions.send_keys(Keys.ENTER)
actions.send_keys(day)
actions.send_keys(Keys.ENTER)
actions.send_keys(str(random.choice(year)))
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[5]/label/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[6]/button').click()
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div[1]/div[1]').click.send_keys(monthwords).send_keys(Keys.ENTER)

print('')
print('   __ _ _ _   _                         _       _           ')
print('  / _(_) | | (_)                       | |     | |          ')
print(' | |_ _| | |  _ _ __     ___ __ _ _ __ | |_ ___| |__   __ _ ')
print(' |  _| | | | | | `_ \   / __/ _` | `_ \| __/ __| `_ \ / _` |')
print(' | | | | | | | | | | | | (_| (_| | |_) | || (__| | | | (_| |')
print(' |_| |_|_|_| |_|_| |_|  \___\__,_| .__/ \__\___|_| |_|\__,_|')
print('                                 | |                        ')
print('                                 |_|                        ')


''' # ignnore this
tokenask = input('Type Y to get 0Auth token.  ')

if tokenask == 'ntcfyugvtcrydrtgvytdyftgbtufyguv56ygfr56yh': 
 pass

if tokenask != 'ntcfyugvtcrydrtgvytdyftgbtufyguv56ygfr56yhntcfyugvtcrydrtgvytdyftgbtufyguv56ygfr56yhntcfyugvtcrydrtgvytdyftgbtufyguv56ygfr56yh': 
 localstorage =  driver.execute_script("let popup; popup = window.open('', '', width=1,height=1); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token")
'''
sleep(5)

print(f'email:password:username')
print(f'{email}:{password}:{username}')