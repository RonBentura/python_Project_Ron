from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Category import Category
from HomePage import HomePage
from ProductPage import ProductPage
from GeneralOptions import GeneralOptions
from CartPage import CartPage
from CreateAccount import CreateAccount
from OrderPayment import OrderPayment
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_chrome = Service(r"C:\Users\IMOE001\Desktop\רון (לא לגעת) !!!\WEB Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)
driver.implicitly_wait(20)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

Category = Category(driver)
HomePage = HomePage(driver)
ProductPage = ProductPage(driver)
GeneralOptions = GeneralOptions(driver)
CartPage = CartPage(driver)
CreateAccount = CreateAccount(driver)
OrderPayment = OrderPayment(driver)

HomePage.get_speakers_category()

Category.click_product_by_id("20")

ProductPage.click_color_by_css_selector("#rabbit[title='BLACK']")

# plus_quantity = driver.find_element(By.CLASS_NAME, "plus")
# a = 3
# for i in range(a):
a = 3
for i in range(a):
    ProductPage.add_one_plus_quantity()

ProductPage.click_on_save_to_cat_btn()

checkout_pop_up = driver.find_element(By.ID, "checkOutPopUp")
checkout_pop_up.click()

CreateAccount.registration("rontil122", "ronbn28122@gmail.com", "Ronbn28")

next_button = driver.find_element(By.ID, "next_btn")
next_button.click()

OrderPayment.fill_safepay_details("rontil122", "Ronbn28")

GeneralOptions.go_to_cart_page()
GeneralOptions.go_to_oredrs_history()
GeneralOptions.delete_account_from_any_page()
GeneralOptions.confirm_delete()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "speakersImg")))
