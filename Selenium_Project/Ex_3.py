from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
a = 3
for i in range(a):
    plus_quantity.click()

add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")
add_to_cart_button.click()

speakers_on_path = driver.find_element(By.XPATH, "//a[@class='ng-binding']")
speakers_on_path.click()

speakers_product_id_25 = driver.find_element(By.ID, "25")
speakers_product_id_25.click()

speakers_product_id_25_color = driver.find_element(By.CSS_SELECTOR, "#bunny[title='TURQUOISE']")
speakers_product_id_25_color.click()

plus_quantity = driver.find_element(By.CLASS_NAME, "plus")
a = 2
for i in range(a):
    plus_quantity.click()

add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")
add_to_cart_button.click()

home_button = driver.find_element(By.CSS_SELECTOR, "div.logo>a>span.roboto-medium")
home_button.click()

sleep(10)

element = driver.find_element(By.ID, "shoppingCartLink")
ActionChains(driver).move_to_element(element).perform()

remove_item = driver.find_element(By.CLASS_NAME, "removeProduct")
remove_item.click()

sleep(3)