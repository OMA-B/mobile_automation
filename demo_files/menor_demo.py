import time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    # 'appPackage': 'br.gov.rs.procergs.mprs'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='MenorPrecoNotaGaucha')
# element = driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.nexuslauncher:id/icon')

element.click()

# type into login boxes in Menor app
time.sleep(10)

driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="main-content"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('1234567890')

time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="main-content"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('34890')

time.sleep(5)

# driver.quit()