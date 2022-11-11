from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Category import Category
from HomePage import HomePage
from ProductPage import ProductPage
from GeneralOptions import GeneralOptions
from CartPage import CartPage


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

HomePage.get_tablets_category()
Category.click_product_by_id("16")

GeneralOptions.click_elemet_in_path_By_XPATH("//a[@class='ng-binding']")

GeneralOptions.click_elemet_in_path_By_XPATH("//a[@translate='HOME']")

