import pprint
from appium.webdriver.extensions.android.nativekey import AndroidKey
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
    'appPackage': 'com.androidsample.generalstore',
    'appActivity': 'com.androidsample.generalstore.SplashActivity',
}

url = f'http://localhost:4723'
# driver = webdriver.Remote(url, options=cap)
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

wait = WebDriverWait(driver=driver, timeout=30)

# login interface
# select dropdown and scroll to select country
country = 'Argentina'
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.androidsample.generalstore:id/spinnerCountry'))).click()
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{country}"))')))
wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, f'//android.widget.TextView[@text="{country}"]'))).click()
# fill in Name
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.androidsample.generalstore:id/nameField'))).send_keys('Debbie')
# select gender
gender = 'Female'
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, f'com.androidsample.generalstore:id/radio{gender}'))).click()
# submit to start shopping
wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.androidsample.generalstore:id/btnLetsShop'))).click()

# check for error message
# toast_message = wait.until(EC.presence_of_element_located(locator=(AppiumBy.XPATH, '//android.widget.Toast[1]'))).get_attribute('name')
# shop_message = wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.androidsample.generalstore:id/btnLetsShop'))).get_attribute('name')
# print(toast_message)
# print(shop_message)

# get_products
item = 'LeBron Soldier 12 '
# wait.until(EC.presence_of_element_located(locator=(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{item}"))')))
product_list = []

for _ in range(10):
    product_list_el = wait.until(EC.presence_of_element_located(locator=(AppiumBy.ID, 'com.androidsample.generalstore:id/rvProductList')))

    products = product_list_el.find_elements(AppiumBy.XPATH, '//android.widget.RelativeLayout')
    product_list += products

    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollForward(2)')))


pprint.pprint(product_list)
print(len(product_list))

for product in product_list:
    try:
        print(product.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/productName').text)
        # if product.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/productName').text == item:
        #     print('found it')
        #     product.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/productAddCart').click()
        #     print('added to cart successfully')
    except: 
        print('unable to display.')
        # product.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/productAddCart').click()
        # print('added to cart successfully')

# print(products_name)
# print(len(products_name))