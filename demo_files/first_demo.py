import time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/title" and @text="Battery"]')

element.click()

time.sleep(5)

driver.quit()