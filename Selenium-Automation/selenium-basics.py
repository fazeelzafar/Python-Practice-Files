from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://czone.com.pk')

findElement = driver.find_element(By.ID, "header1_search1_txtSearch")
findElement.send_keys("mousepad")
time.sleep(3)

clickButton = driver.find_element(By.ID ,"header1_search1_btnSearch")
clickButton.click()


# Find all elements

# driver = webdriver.Chrome()
# driver.get('https://czone.com.pk/laptops-pakistan-ppt.74.aspx')

# findElement = driver.find_elements(By.TAG_NAME, "h4")

# for i in findElement:
#     print(i.text)

