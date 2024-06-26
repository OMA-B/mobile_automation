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
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main',
}

url = f'http://localhost:4723'
# driver = webdriver.Remote(url, options=cap)
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

wait = WebDriverWait(driver=driver, timeout=30)


# check if terms and conditions pops up, then taka apposite action
if wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.android.chrome:id/signin_fre_dismiss_button'))).is_displayed(): # com.android.chrome:id/terms_accept
    wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.android.chrome:id/signin_fre_dismiss_button'))).click()
    wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.android.chrome:id/negative_button'))).click()

# type into search bar and enter
search_text = 'https://rahulshettyacademy.com/angularAppdemo/'
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.android.chrome:id/search_box_text'))).send_keys(search_text)
wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, f'//android.widget.TextView[@text="{search_text}"]'))).click()
# open navigation menu
wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, '//android.widget.Button[@text="Toggle navigation"]'))).click()
# click on product bar
wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, '//android.widget.TextView[@text="Products"]'))).click()
# toggle navbar to close
wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, '//android.widget.Button[@text="Toggle navigation"]'))).click()
# check for devops text
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward(2)')))
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward(2)')))
text = wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, '//android.widget.TextView[@text="Devops"]')))
print(text.text)
assert text.text == 'Devops'