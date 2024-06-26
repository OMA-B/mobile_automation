import time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

wait = WebDriverWait(driver=driver, timeout=30)

# go to contacts
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="Contacts"])[1]'))).click()
# click create contact btn
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Create contact"]'))).click()
# fill in first name
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="First name"]'))).send_keys('Michael')
# fill in last name
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Last name"]'))).send_keys('Adesh')
# fill in phone number
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Phone"]'))).send_keys('+2349056198240')
# fill in email address
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Email"))'))).send_keys('michaelking4christ@gmail.com')
# click save
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.contacts:id/toolbar_button"]'))).click()

# time.sleep(5)

# driver.quit()