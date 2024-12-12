from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException

# Initialize Chrome WebDriver
chromedriver_path = "./chromedriver.exe"  # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def wait_for_element(xpath, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException as e:
        print(f"TimeoutException: Element not found with XPath {xpath}")
        return None

def wait_for_element_clickable(xpath, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element
    except TimeoutException as e:
        print(f"TimeoutException: Element not clickable with XPath {xpath}")
        return None

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

def write_results_to_html(status):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 80%;
                margin: 0 auto;
                padding: 20px;
                background: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                border-radius: 5px;
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            .status {{
                font-size: 1.2em;
                color: #4CAF50;
                text-align: center;
            }}
            .failed {{
                color: #F44336;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Test Results</h1>
            <div id="status" class="status {status}">{status}</div>
        </div>
    </body>
    </html>
    """
    with open("test_results.html", "w") as file:
        file.write(html_content)

def click_element(xpath, retries=3):
    for attempt in range(retries):
        try:
            element = wait_for_element_clickable(xpath)
            if element:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Allow time for scrolling
                element.click()
                return True
        except StaleElementReferenceException:
            print(f"StaleElementReferenceException caught on attempt {attempt + 1}")
            time.sleep(1)
        except ElementClickInterceptedException:
            print(f"ElementClickInterceptedException caught on attempt {attempt + 1}")
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)
    return False

try:
    driver.get("https://www.interflora.in/?utm_source=LBB&ref=lbbpost")
    driver.maximize_window()
    time.sleep(1)

    tests_passed = True

    # List of actions to perform
    actions = [
        ("//*[@id='user-menu']/div", "click"),
        ("//*[@id='email']", "send_keys", "srksrk6590@gmail.com"),
        ("//*[@id='passwd']", "send_keys", "123456"),
        ("//*[@id='row-submit']/div/button", "click"),
        ("//*[@id='selection-panel']/div[2]/a[7]", "click"),
        ("//*[@id='product-grid']/div[3]", "click"),
        ("//*[@id='location-input']", "send_keys", "560060"),
        ("//*[@id='show-Select_Date']/div/label/span", "click"),
        ("//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a", "click"),
        ("//*[@id='timepicker']", "click"),
        ("//*[@id='timepicker']/div[2]/div[3]", "click"),
        ("//*[@id='add-cart']", "click"),
        ("//*[@id='add-cart']", "click"),
        ("//*[@id='search-products']/input", "send_keys", "Flowers in Box"),
        ("//*[@id='search-products']/div/img", "click"),
        ("//*[@id='product-grid']/div[2]", "click"),
        ("//*[@id='location-input']", "clear_and_send_keys", "560060"),
        ("//*[@id='show-Select_Date']/div/label/span", "click"),
        ("//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a", "click"),
        ("//*[@id='timepicker']", "click"),
        ("//*[@id='timepicker']/div[2]/div[3]", "click"),
        ("//*[@id='add-cart']", "click"),
        ("//*[@id='add-cart']", "click"),
        ("//*[@id='inc-quantity-560849']/img", "click_multiple", 2),
        ("//*[@id='inc-quantity-643072']/img", "click_multiple", 3),
        ("//*[@id='des-quantity-560849']/img", "click"),
        ("//*[@id='enabled-button']/a", "click"),
        ("//*[@id='deliver-btn-7576748']", "click"),
        ("//*[@id='order-summary-wrpr']/div[1]/section[1]/div/div[2]/button", "click")
    ]

    for xpath, action, *args in actions:
        element = wait_for_element(xpath)
        if element:
            highlight_element(element)
            if action == "click":
                if not click_element(xpath):
                    tests_passed = False
            elif action == "send_keys":
                element.send_keys(*args)
            elif action == "clear_and_send_keys":
                element.clear()
                element.send_keys(*args)
            elif action == "click_multiple":
                for _ in range(args[0]):
                    if not click_element(xpath):
                        tests_passed = False
            time.sleep(3)
        else:
            tests_passed = False

finally:
    driver.quit()
    result_status = "All Tests Passed!" if tests_passed else "Some Tests Failed!"
    write_results_to_html(result_status)
