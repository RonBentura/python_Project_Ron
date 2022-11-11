from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_color_by_css_selector(self, css_selector: str):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def click_color_by_css_selector(self, css_selector: str):
        self.find_color_by_css_selector(css_selector).click()

    def plus_quantity_sign(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def add_one_plus_quantity(self):
        self.plus_quantity_sign().click()

    def product_price_jeneral(self):
        return self.driver.find_element(By.XPATH, "//*[@id='Description']/h2")

    def product_price_float(self):
        return float(self.product_price_jeneral().text.replace("$",""))

    def save_to_cart_btn(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def click_on_save_to_cat_btn(self):
        self.save_to_cart_btn().click()

    def product_name_element(self):
        return self.driver.find_element(By.CSS_SELECTOR,"h1[class='roboto-regular screen768 ng-binding']")

    def product_name(self):
        return self.product_name_element().text