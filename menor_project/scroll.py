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


for i in range(5):
    driver.swipe(start_x=500, start_y=1900, end_x=500, end_y=500, duration=5000)
# action.press(x=500, y=).move_to(x=500, y=275).release().perform()