from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from CartPage import CartPage
from Category import Category
from HomePage import HomePage
from ProductPage import ProductPage
from GeneralOptions import GeneralOptions
from time import sleep

service_chrome = Service(r"C:\selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(60)
# driver.maximize_window()

Category = Category(driver)
HomePage = HomePage(driver)
ProductPage = ProductPage(driver)
GeneralOptions = GeneralOptions(driver)
CartPage = CartPage(driver)


HomePage.get_speakers_category()
Category.click_product_by_id("20")
prod1name = ProductPage.product_name()
ProductPage.click_color_by_css_selector("#rabbit[title='BLACK']")
a = 3
for i in range(a):
    ProductPage.add_one_plus_quantity()
qty1 = a+1
prod1price = ProductPage.product_price_float()
ProductPage.click_on_save_to_cat_btn()
GeneralOptions.click_go_home_btn()

HomePage.get_speakers_category()
Category.click_product_by_id("25")
prod2name = ProductPage.product_name()
ProductPage.click_color_by_css_selector("#bunny[title='TURQUOISE']")
a = 2
for i in range(a):
    ProductPage.add_one_plus_quantity()
qty2 = a+1
prod2price = ProductPage.product_price_float()
ProductPage.click_on_save_to_cat_btn()
GeneralOptions.click_go_home_btn()

HomePage.get_speakers_category()
Category.click_product_by_id("24")
prod3name = ProductPage.product_name()
ProductPage.click_color_by_css_selector("#bunny[title='GRAY']")
a = 1
for i in range(a):
    ProductPage.add_one_plus_quantity()
qty3 = a+1
prod3price = ProductPage.product_price_float()
ProductPage.click_on_save_to_cat_btn()
GeneralOptions.click_go_home_btn()

GeneralOptions.go_to_cart_page()
list2 = []
for i in CartPage.list_of_prices():
    list2.append(i.text.replace("$","").replace(",",""))
list2 = list2[::-1]
print(list2)

print(prod3name ,"cost", prod3price,"*", qty3, "=", list2[2])
print(prod2name ,"cost", prod2price,"*", qty2, "=", list2[1])
print(prod1name ,"cost", prod1price,"*", qty1, "=", list2[0])

sleep(10)