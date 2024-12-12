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
driver.get("https://www.interflora.in/?utm_source=LBB&ref=lbbpost")
driver.maximize_window()
time.sleep(1)


person=driver.find_element(By.XPATH,"//*[@id='user-menu']/div")
highlight_element(person)
person.click()
time.sleep(3)





email = driver.find_element(By.XPATH, "//*[@id='email']")
highlight_element(email)
email.send_keys("srksrk6590@gmail.com")
time.sleep(3)

pwd = driver.find_element(By.XPATH, "//*[@id='passwd']")
highlight_element(pwd)
pwd.send_keys("123456")
time.sleep(3)


proceed = driver.find_element(By.XPATH, "//*[@id='row-submit']/div/button")
highlight_element(proceed)
proceed.click()
time.sleep(3)



flower= driver.find_element(By.XPATH,"//*[@id='selection-panel']/div[2]/a[7]")
highlight_element(flower)
flower.click()
time.sleep(3)



bbf= driver.find_element(By.XPATH,"//*[@id='product-grid']/div[3]")
highlight_element(bbf)
bbf.click()
time.sleep(1)


pin = driver.find_element(By.XPATH, "//*[@id='location-input']")
highlight_element(pin)
pin.send_keys("560060")
time.sleep(1)


date= driver.find_element(By.XPATH,"//*[@id='show-Select_Date']/div/label/span")
highlight_element(date)
date.click()
time.sleep(2)

date1= driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
highlight_element(date1)
date1.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0,350)","")


time_slot= driver.find_element(By.XPATH,"//*[@id='timepicker']")
highlight_element(time_slot)
time_slot.click()
time.sleep(8)

t1= driver.find_element(By.XPATH,"//*[@id='timepicker']/div[2]/div[3]")
highlight_element(t1)
t1.click()
time.sleep(5)



ac= driver.find_element(By.XPATH,"//*[@id='add-cart']")
highlight_element(ac)
ac.click()
time.sleep(3)


cwd= driver.find_element(By.XPATH,"//*[@id='add-cart']")
highlight_element(cwd)
cwd.click()
time.sleep(3)


Search = driver.find_element(By.XPATH, "//*[@id='search-products']/input")
highlight_element(Search)
Search.send_keys("Flowers in Box")
time.sleep(3)



p = driver.find_element(By.XPATH, "//*[@id='search-products']/div/img")
highlight_element(p)
p.click()
time.sleep(3)


fsb= driver.find_element(By.XPATH,"//*[@id='product-grid']/div[2]")
highlight_element(fsb)
fsb.click()
time.sleep(1)


pin1 = driver.find_element(By.XPATH, "//*[@id='location-input']")
highlight_element(pin1)
pin1.clear()
pin1.send_keys("560060")
time.sleep(1)


dates= driver.find_element(By.XPATH,"//*[@id='show-Select_Date']/div/label/span")
highlight_element(dates)
dates.click()
time.sleep(2)

date2= driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a")
highlight_element(date2)
date2.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0,350)","")


time_slot1= driver.find_element(By.XPATH,"//*[@id='timepicker']")
highlight_element(time_slot1)
time_slot1.click()
time.sleep(8)

t2= driver.find_element(By.XPATH,"//*[@id='timepicker']/div[2]/div[3]")
highlight_element(t2)
t2.click()
time.sleep(5)




ac1= driver.find_element(By.XPATH,"//*[@id='add-cart']")
highlight_element(ac1)
ac1.click()
time.sleep(3)


cwd1= driver.find_element(By.XPATH,"//*[@id='add-cart']")
highlight_element(cwd1)
cwd1.click()
time.sleep(3)


plus= driver.find_element(By.XPATH,"//*[@id='inc-quantity-560849']/img")
highlight_element(plus)
plus.click()
plus.click()
time.sleep(3)

plus1= driver.find_element(By.XPATH,"//*[@id='inc-quantity-643072']/img")
highlight_element(plus1)
plus1.click()
plus1.click()
plus1.click()
time.sleep(3)


minus= driver.find_element(By.XPATH,"//*[@id='des-quantity-560849']/img")
highlight_element(minus)
minus.click()
time.sleep(3)

co= driver.find_element(By.XPATH,"//*[@id='enabled-button']/a")
highlight_element(co)
co.click()
time.sleep(5)

co1= driver.find_element(By.XPATH,"//*[@id='deliver-btn-7576748']")
highlight_element(co1)
co1.click()
time.sleep(4)

co2= driver.find_element(By.XPATH,"//*[@id='order-summary-wrpr']/div[1]/section[1]/div/div[2]/button")
highlight_element(co2)
co2.click()
time.sleep(6)
