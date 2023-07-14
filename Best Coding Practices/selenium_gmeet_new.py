import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def configure_driver():
    """Configure the Chrome driver with specific options and settings."""
    options = webdriver.ChromeOptions()
    
    # Maximize the window and disable extensions
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    
    # Set preferences for media, geolocation, and notifications
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    
    # Disable automation features to avoid detection
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False) 
    
    # Create and configure the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver


def login_google_account(driver, username, password):
    """Log in to a Google account using the provided username and password."""
    driver.get('https://accounts.google.com/')
    
    # Find the username field, enter the username, and click Next
    username_field = driver.find_element(By.ID, 'identifierId')
    username_field.click()
    username_field.send_keys(username)
    next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    next_button.click()
    time.sleep(5)
    
    # Find the password field, enter the password, and click Next
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_field.click()
    password_field.send_keys(password)
    next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
    next_button.click()
    time.sleep(5)


def join_google_meet(driver, meet_url):
    """Join a Google Meet session using the provided Meet URL."""
    driver.get(meet_url)
    time.sleep(5)
    
    # Configure actions to control mic and camera settings
    actions = ActionChains(driver)
    actions.send_keys(Keys.CONTROL, 'D')  # Enable/disable mic
    actions.send_keys(Keys.CONTROL, 'E')  # Enable/disable camera
    
    # Find the join button and click it
    join_button = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')
    join_button.click()


# Usage example:
driver = configure_driver()
login_google_account(driver, 'fazeelzbackup@gmail.com', 'xxxxxxxx')
join_google_meet(driver, 'https://meet.google.com/drv-rjky-phm')
input()
