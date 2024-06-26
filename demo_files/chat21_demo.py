import time, os, json
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

wait_user1 = object()
wait_user2 = object()

with open(file='users.json', mode='r') as user_file:
    user_data = json.load(fp=user_file)

with open(file='chat21.json', mode='r') as chat_file:
    chat_data = json.load(fp=chat_file)


for user in user_data:

    cap:Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'appPackage': 'chat21.android.demo',
        'appActivity': 'chat21.android.demo.SplashActivity',
        'udid': user["device"],
    }

    url = f'http://localhost:{user["appium_port"]}'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

    wait = WebDriverWait(driver=driver, timeout=30)

    if user["user"] == 'USER1': wait_user1 = wait
    else: wait_user2 = wait

    # login section
    if wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/login'))).is_displayed():
        # input email
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/email'))).send_keys(os.getenv(user["user"]))
        # input password
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/password'))).send_keys(os.getenv('PASSWORD'))
        # click login button
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/login'))).click()

        print('Logging in...')

    # home screen
    if wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="HOME"]'))).is_displayed():

        print(f'User: {os.getenv(user["user"])} login successful!\nnow HOME.')
        # go to chat section
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="CHAT"]'))).click()

# USER1 will click on start new chat button
wait_user1.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/button_new_conversation'))).click()
# click on search icon
wait_user1.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/action_search'))).click()
# search for USER2
user2 = 'oma test2'
wait_user1.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/search_src_text'))).send_keys(user2)
# click on found USER2 to open conversation
wait_user1.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="fullname" and @text="{user2}"]'))).click()

# populate message box with text to send
wait_user1.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/main_activity_chat_bottom_message_edittext'))).send_keys('hello there')
# click send
wait_user1.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/main_activity_send'))).click()


















    # # go to profile
    # wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="PROFILE"]'))).click()
    # # logging out user
    # if wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/logout'))).is_displayed():

    #     wait.until(EC.presence_of_element_located((AppiumBy.ID, 'chat21.android.demo:id/logout'))).click()

    #     print(f'User: {os.getenv(f"{user_inputs[2]}")} successfully logged out!')
        

