import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


opt = webdriver.ChromeOptions()

opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

opt.add_argument("--disable-blink-features=AutomationControlled") 
opt.add_experimental_option("excludeSwitches", ["enable-automation"]) 
opt.add_experimental_option("useAutomationExtension", False) 


driver = webdriver.Chrome(options = opt)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

driver.get('https://accounts.google.com/')

username = driver.find_element(By.ID, 'identifierId')
username.click()
username.send_keys('fazeelzbackup@gmail.com')
next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
next.click()
time.sleep(5)

password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('xxxxxxxxx')
next = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
next.click()
time.sleep(5)

driver.get('https://meet.google.com/drv-rjky-phm')

time.sleep(5)

actions = ActionChains(driver)

actions.send_keys(Keys.CONTROL, 'D') #For mic
actions.send_keys(Keys.CONTROL, 'E') #For camera

join = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')
join.click()

input()
