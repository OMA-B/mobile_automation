import time, json, os
from dotenv import load_dotenv
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

cap:Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
}

url = 'http://localhost:4723'


bar_codes = ['7896032501010', '7896412819520']
required_amount = 10


def launch_driver_to_open_the_app(bar_code):

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

    wait = WebDriverWait(driver=driver, timeout=10)

    # click on the app on home screen to launch
    if wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Predicted app: MenorPrecoNotaGaucha'))).is_displayed(): wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Predicted app: MenorPrecoNotaGaucha'))).click()
    else:
        driver.swipe(start_x=525, start_y=1500, end_x=525, end_y=500)
        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'MenorPrecoNotaGaucha'))).click()

    # check if app remains at login screen, login then
    try:
        if wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Image[@text="marcalogin"]'))).is_displayed():
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="main-content"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'))).send_keys(os.getenv('USERNAME'))
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="main-content"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'))).send_keys(os.getenv('PASSWORD'))
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="ENTRAR"]'))).click()
    except Exception as e: print('Login page was not shown.')

    # check if policy detail screen is displayed, scroll down and confirm
    try:
        if wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Política do Aplicativo"]'))).is_displayed():
            driver.swipe(start_x=500, start_y=1960, end_x=500, end_y=500)
            # wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
    except Exception as e: print('Policy page was not shown.')

    # search for products
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="PESQUISAR PRODUTOS"]'))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))).click()
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))).send_keys(bar_code)
    driver.press_keycode(66)

    try:
        result_amount = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "resultados encontrados")]'))).text.split(' ')[0]
        print(result_amount)
    except: pass

    # time.sleep(10)

    driver.quit()

    return int(result_amount)


items_data_list = []
supplier_checklist = []

def gather_data_from_app():

    # check if amount needed has been reached
    if len(items_data_list) >= required_amount: return

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps=cap))

    wait = WebDriverWait(driver=driver, timeout=5)
    
    
    for index in range(6):
        # check if amount needed has been reached
        if len(items_data_list) >= required_amount: break

        try:
            index += 1
            # get the parent element first
            # retrieve the title and time
            # get all the items by time
            item_by_time = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'(//android.widget.Image[@text="time outline"])[{index}]')))

            parent_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.view.View[@resource-id="main-content"]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[{index}]')))
            try:
                time.sleep(3)
                # Derive child elements within each parent
                child_elements = parent_element.find_elements(AppiumBy.XPATH, './/android.widget.TextView')
                # Process child elements
                prod_Title = child_elements[1].text.strip()
                prod_Price = child_elements[2].text.strip()
                prod_Supplier = child_elements[3].text.strip()

                item_by_time.click()
                time.sleep(3)

                try:
                    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="tab-button-lista"]/android.view.View'))).click()
                except:
                    # grab the item info
                    price = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[2]'))).text.strip()
                    supplier = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[3]'))).text.strip()
                    address_1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[4]'))).text.strip()
                    address_2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[5]'))).text.strip()
                    telephone = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[6]'))).text.strip()
                    maybe_date = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[7]'))).text.strip()
                    try: date = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[8]'))).text.strip()
                    except Exception as e: pass

                    if prod_Price == price and prod_Supplier == supplier and supplier not in supplier_checklist:
                        item_data = {'name_of_product': prod_Title, 'price': price, 'name_of_supplier': supplier, 'address': f'{address_1} - {address_2}', 'telefone': telephone.replace('Telefone ', '') if 'Telefone' in telephone else '', 'date': date if 'Telefone' in telephone else maybe_date}
                        items_data_list.append(item_data)
                        supplier_checklist.append(supplier)
                        print(item_data)
            except Exception as e:
                print(e)

            if wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="share COMPARTILHAR"]'))).is_displayed():
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="back"]'))).click()

                time.sleep(3)
        except Exception as e:
            print(f"Couldn't find item parent at the index {index}")
    
    driver.swipe(start_x=500, start_y=1957, end_x=500, end_y=200, duration=5000)

    driver.quit()
        

result_amount = launch_driver_to_open_the_app(bar_code=bar_codes[1])

for _ in range(int(result_amount/5)):
    gather_data_from_app()

with open(file=f'items_data_for_{bar_codes[1]}.json', mode='w') as file:
    json.dump(obj=items_data_list, fp=file)
