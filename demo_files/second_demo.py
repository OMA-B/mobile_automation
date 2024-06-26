import time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')

element.click()

# type into search box in Chrome
driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Search or type web address"]').send_keys('OMABrayn')

time.sleep(5)

# driver.quit()