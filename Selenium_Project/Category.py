from selenium import webdriver
from selenium.webdriver.common.by import By


class Category:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_product_by_id(self, id_num: str):
        return self.driver.find_element(By.ID, id_num)

    def click_product_by_id(self, id_num: str):
        self.find_product_by_id(id_num).click()
