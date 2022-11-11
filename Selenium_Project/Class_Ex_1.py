from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from Category import Category
from HomePage import HomePage
from Category import Category
from ProductPage import ProductPage
from GeneralOptions import GeneralOptions

service_chrome = Service(r"C:\Users\IMOE001\Desktop\רון (לא לגעת) !!!\WEB Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/")

#driver.maximize_window()

driver.implicitly_wait(50)

Category = Category(driver)
HomePage = HomePage(driver)
ProductPage = ProductPage(driver)
GeneralOptions = GeneralOptions(driver)

HomePage.get_mice_category()

Category.click_product_by_id("29")

a = 2
for i in range(a):
    ProductPage.add_one_plus_quantity()

ProductPage.click_on_save_to_cat_btn()

GeneralOptions.click_go_home_btn()

HomePage.get_speakers_category()

Category.click_product_by_id("20")

b = 1
for i in range(b):
    ProductPage.add_one_plus_quantity()

ProductPage.click_on_save_to_cat_btn()

num_of_items = GeneralOptions.num_of_items_in_cart()

print(num_of_items)

if num_of_items == (b+1+a+1):
    print("ok")
