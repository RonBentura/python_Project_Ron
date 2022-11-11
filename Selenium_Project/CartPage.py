from selenium import webdriver
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def list_of_prices(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"p[class='price roboto-regular ng-binding']")
