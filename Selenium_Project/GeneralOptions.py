from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class GeneralOptions:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def go_home_btn(self):
        return self.driver.find_element(By.ID, "Layer_1")

    def click_go_home_btn(self):
        self.go_home_btn().click()

    def cart_icon(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def go_to_cart_page(self):
        self.cart_icon().click()

    def num_of_items_in_cart(self):
        ActionChains(self.driver).move_to_element(self.cart_icon()).perform()
        item_in_cart = self.driver.find_element(By.CSS_SELECTOR, "label[class='roboto-regular ng-binding']")
        return int(item_in_cart.text[1:2])

    def elemet_on_path_By_XPATH(self, xpth:str):
        return self.driver.find_element(By.XPATH, xpth)

    def click_elemet_in_path_By_XPATH(self,xpth:str):
        self.elemet_on_path_By_XPATH(xpth).click()

    def remove_item_from_cart(self,x_index:int):
        cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        ActionChains(self.driver).move_to_element(cart_icon).perform()
        x_list = self.driver.find_elements(By.CLASS_NAME, "removeProduct")
        x_list[x_index].click()

    def go_to_account_page(self):
        account_menu = self.driver.find_element(By.ID, "menuUserSVGPath")
        account_menu.click()
        my_account_button = self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_account'][class='option roboto-medium ng-scope']")
        my_account_button.click()

    def go_to_oredrs_history(self):
        account_menu = self.driver.find_element(By.ID, "menuUserSVGPath")
        account_menu.click()
        orders_history = self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']")
        orders_history.click()

    def delete_account_from_any_page(self):
        self.go_to_account_page()
        delete_account = self.driver.find_element(By.CLASS_NAME, "deleteBtnText")
        delete_account.click()

    def delete_account_from_account_page(self):
        delete_account = self.driver.find_element(By.CLASS_NAME, "deleteBtnText")
        delete_account.click()

    def confirm_delete(self):
        confirm_delete = self.driver.find_element(By.CSS_SELECTOR, "[data-ng-click='deleteAccountConfirmed()']")
        confirm_delete.click()
