from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

# Initialize Chrome WebDriver
chromedriver_path = "./chromedriver.exe"  # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(by, value):
    attempts = 0
    while attempts < 3:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
            driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
            time.sleep(2)
            driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)
            return element
        except StaleElementReferenceException:
            attempts += 1
    raise Exception(f"Element with {by}={value} could not be interacted with after several attempts")

def find_element(by, value):
    attempts = 0
    while attempts < 3:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
            return element
        except StaleElementReferenceException:
            attempts += 1
    raise Exception(f"Element with {by}={value} is not found after several attempts")

# Open website
driver.get("https://www.interflora.in/?utm_source=LBB&ref=lbbpost")
driver.maximize_window()
time.sleep(1)

# Interact with elements
try:
    person = highlight_element(By.XPATH, "//*[@id='user-menu']/div")
    person.click()
    time.sleep(3)

    email = highlight_element(By.XPATH, "//*[@id='email']")
    email.send_keys("srksrk6590@gmail.com")
    time.sleep(3)

    pwd = highlight_element(By.XPATH, "//*[@id='passwd']")
    pwd.send_keys("123456")
    time.sleep(3)

    proceed = highlight_element(By.XPATH, "//*[@id='row-submit']/div/button")
    proceed.click()
    time.sleep(3)

    flower = highlight_element(By.XPATH, "//*[@id='selection-panel']/div[2]/a[7]")
    flower.click()
    time.sleep(3)

    bbf = highlight_element(By.XPATH, "//*[@id='product-grid']/div[3]")
    bbf.click()
    time.sleep(1)

    pin = highlight_element(By.XPATH, "//*[@id='location-input']")
    pin.send_keys("560060")
    time.sleep(1)

    date = highlight_element(By.XPATH, "//*[@id='show-Select_Date']/div/label/span")
    date.click()
    time.sleep(2)

    date1 = highlight_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
    date1.click()
    time.sleep(5)

    driver.execute_script("window.scrollBy(0,350)", "")

    time_slot = highlight_element(By.XPATH, "//*[@id='timepicker']")
    time_slot.click()
    time.sleep(8)

    t1 = highlight_element(By.XPATH, "//*[@id='timepicker']/div[2]/div[3]")
    t1.click()
    time.sleep(5)

    ac = highlight_element(By.XPATH, "//*[@id='add-cart']")
    ac.click()
    time.sleep(3)

    cwd = highlight_element(By.XPATH, "//*[@id='add-cart']")
    cwd.click()
    time.sleep(3)

    search = highlight_element(By.XPATH, "//*[@id='search-products']/input")
    search.send_keys("Flowers in Box")
    time.sleep(3)

    p = highlight_element(By.XPATH, "//*[@id='search-products']/div/img")
    p.click()
    time.sleep(3)

    fsb = highlight_element(By.XPATH, "//*[@id='product-grid']/div[2]")
    fsb.click()
    time.sleep(1)

    pin1 = highlight_element(By.XPATH, "//*[@id='location-input']")
    pin1.clear()
    pin1.send_keys("560060")
    time.sleep(1)

    dates = highlight_element(By.XPATH, "//*[@id='show-Select_Date']/div/label/span")
    dates.click()
    time.sleep(2)

    date2 = highlight_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
    date2.click()
    time.sleep(5)

    driver.execute_script("window.scrollBy(0,350)", "")

    time_slot1 = highlight_element(By.XPATH, "//*[@id='timepicker']")
    time_slot1.click()
    time.sleep(8)

    t2 = highlight_element(By.XPATH, "//*[@id='timepicker']/div[2]/div[3]")
    t2.click()
    time.sleep(5)

    ac1 = highlight_element(By.XPATH, "//*[@id='add-cart']")
    ac1.click()
    time.sleep(3)

    cwd1 = highlight_element(By.XPATH, "//*[@id='add-cart']")
    cwd1.click()
    time.sleep(3)

    plus = highlight_element(By.XPATH, "//*[@id='inc-quantity-560849']/img")
    plus.click()
    plus.click()
    time.sleep(3)

    plus1 = highlight_element(By.XPATH, "//*[@id='inc-quantity-643072']/img")
    plus1.click()
    plus1.click()
    plus1.click()
    time.sleep(3)

    minus = highlight_element(By.XPATH, "//*[@id='des-quantity-560849']/img")
    minus.click()
    time.sleep(3)

    co = highlight_element(By.XPATH, "//*[@id='enabled-button']/a")
    co.click()
    time.sleep(5)

    co1 = highlight_element(By.XPATH, "//*[@id='deliver-btn-7576748']")
    co1.click()
    time.sleep(4)

    co2 = highlight_element(By.XPATH, "//*[@id='order-summary-wrpr']/div[1]/section[1]/div/div[2]/button")
    co2.click()
    time.sleep(6)

except TimeoutException as e:
    print(f"Element could not be found or interacted with in time: {e}")

# Close the browser
driver.quit()
