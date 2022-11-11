from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_chrome = Service(r"C:\Users\IMOE001\Desktop\רון (לא לגעת) !!!\WEB Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)
driver.implicitly_wait(20)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

speakers_category = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
speakers_category.click()

speakers_product_id_20 = driver.find_element(By.ID, "20")
speakers_product_id_20.click()

speakers_product_id_20_color = driver.find_element(By.CSS_SELECTOR, "#rabbit[title='BLACK']")
speakers_product_id_20_color.click()

plus_quantity = driver.find_element(By.CLASS_NAME, "plus")
a = 1
for i in range(a):
    plus_quantity.click()

add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")
add_to_cart_button.click()

cart_button = driver.find_element(By.ID, "menuCart")
cart_button.click()

cart_path = driver.find_element(By.CSS_SELECTOR, "a[class='select  ng-binding']")
if cart_path.text == "SHOPPING CART":
    print("great success")
else:
    print("failed")

sleep(3)