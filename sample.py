from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Initialize Chrome WebDriver (replace with Firefox WebDriver if needed)
chromedriver_path = "./chromedriver.exe"  # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

# Open Amazon.in
driver.get("https://www.interflora.in/cart")
driver.maximize_window()
time.sleep(2)




Search = driver.find_element(By.XPATH, "//*[@id='search-products']/input")
highlight_element(Search)
Search.send_keys("Flowers in Box")
time.sleep(3)



p = driver.find_element(By.XPATH, "//*[@id='search-products']/div/img")
highlight_element(p)
p.click()
time.sleep(3)