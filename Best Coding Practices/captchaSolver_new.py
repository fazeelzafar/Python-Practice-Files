from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
import time


def open_webpage():
    """
    Opens a webpage using Selenium's WebDriver.
    """
    driver = webdriver.Chrome()
    driver.get('https://captcha.com/demos/features/captcha-demo.aspx')
    return driver


def capture_captcha_image(driver):
    """
    Captures the captcha image from the webpage and saves it as 'captcha_image.png'.
    """
    img = driver.find_element(By.ID, 'demoCaptcha_CaptchaImageDiv')
    img.screenshot('captcha_image.png')


def solve_captcha(api_key):
    """
    Solves the captcha using the TwoCaptcha API.
    Returns the captcha text.
    """
    solveCaptcha = TwoCaptcha(api_key)

    try:
        res = solveCaptcha.normal('captcha_image.png')
    except Exception as e:
        print(e)
        return None

    captchaText = res['code']
    return captchaText


def enter_captcha_text(driver, captcha_text):
    """
    Enters the captcha text into the webpage.
    """
    driver.find_element(By.ID, 'captchaCode').send_keys(captcha_text)
    time.sleep(3)


def validate_captcha(driver):
    """
    Clicks the 'validate' button to submit the captcha.
    """
    driver.find_element(By.ID, 'validateCaptchaButton').click()


def main():
    """
    Main function to execute the entire process.
    """
    api_key = 'd9f4df8fc75b17e484d12cc4851047c5'
    driver = open_webpage()
    capture_captcha_image(driver)
    captcha_text = solve_captcha(api_key)

    if captcha_text:
        enter_captcha_text(driver, captcha_text)
        validate_captcha(driver)

    input()


# Execute the main function
if __name__ == '__main__':
    main()