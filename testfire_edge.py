from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Driver setup (yaha driver ka path dalna)
service = Service("C:/WebDriver/bin/msedgedriver.exe")
driver = webdriver.Edge(service=service)

# 1. Open website
driver.get("https://demo.testfire.net/")
driver.save_screenshot("page1_home.png")   # Home page screenshot

# 2. Click Sign In
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(2)
driver.save_screenshot("page2_login.png")  # Login page screenshot

# 3. Login (username + password)
driver.find_element(By.ID, "uid").send_keys("admin")
driver.find_element(By.ID, "passw").send_keys("admin")
driver.find_element(By.NAME, "btnSubmit").click()
time.sleep(2)
driver.save_screenshot("page3_account.png")  # Account page screenshot

# 4. Transfer Funds page
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
time.sleep(2)
driver.save_screenshot("page4_transfer.png")

# 5. Contact Us page
driver.find_element(By.LINK_TEXT, "Contact Us").click()
time.sleep(2)
driver.save_screenshot("page5_contact.png")

# Close browser
driver.quit()
