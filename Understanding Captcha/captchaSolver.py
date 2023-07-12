from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
import time

driver = webdriver.Chrome()
driver.get('https://captcha.com/demos/features/captcha-demo.aspx')

img = driver.find_element(By.ID, 'demoCaptcha_CaptchaImageDiv')
img.screenshot('captcha_image.png')

api_key = 'd9f4df8fc75b17e484d12cc4851047c5'

solveCaptcha = TwoCaptcha(api_key)

try:
    res = solveCaptcha.normal('captcha_image.png')

except Exception as e:
    print(e)

else:
    captchaText = res['code']
    driver.find_element(By.ID, 'captchaCode').send_keys(captchaText)
    time.sleep(3)

    driver.find_element(By.ID, 'validateCaptchaButton').click()


input()


