from selenium import webdriver
from selenium.webdriver.common.by import By



class OrderPayment:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_safepay_details(self, username, password):
        self.click_on_safepay_btn()
        self.insert_to_safepay_username(username)
        self.insert_to_safepay_password(password)
        self.pay_now_safepay_btn()

    def click_on_next_to_payment(self):
        self.driver.find_element(By.ID, "next_btn").click()

    def click_on_safepay_btn(self):
        self.driver.find_element(By.NAME, "safepay").click()

    def insert_to_safepay_username(self, username):
        savepay_username = self.driver.find_element(By.NAME, "safepay_username")
        savepay_username.click()
        savepay_username.send_keys(username)

    def insert_to_safepay_password(self, password):
        savepay_password = self.driver.find_element(By.NAME, "safepay_password")
        savepay_password.click()
        savepay_password.send_keys(password)

    def pay_now_safepay_btn(self):
        pay_now_button = self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")
        pay_now_button.click()

    def fill_mastercredit_details(self, card_number, cvv_number, m_index, y_index, card_holder_name):
        self.mastercredit_btn()
        self.send_keys_on_creditcard_field(card_number)
        self.send_keys_on_cvv_field(cvv_number)
        self.month_expaired(m_index)
        self.year_expaired(y_index)
        self.send_keys_on_card_holder_name(card_holder_name)
        self.click_on_pay_now_manual_pay_btn()


    def mastercredit_btn(self):
        mastercard_button = self.driver.find_element(By.NAME, "masterCredit")
        mastercard_button.click()

    def click_on_creditcard_field(self):
        credit_card_field = self.driver.find_element(By.ID, "creditCard")
        credit_card_field.click()

    def send_keys_on_creditcard_field(self, card_number):
        credit_card_field = self.driver.find_element(By.ID, "creditCard")
        credit_card_field.click()
        credit_card_field.send_keys(card_number)

    def click_on_cvv_field(self):
        cvv_field = self.driver.find_element(By.NAME, "cvv_number")
        cvv_field.click()

    def send_keys_on_cvv_field(self, cvv_number):
        cvv_field = self.driver.find_element(By.NAME, "cvv_number")
        cvv_field.click()
        cvv_field.send_keys(cvv_number)

    # def month_expaired(self, m_index: int):
    #     month_dropdown = self.driver.find_elements(By.NAME, "mmListbox")
    #     month_dropdown = month_dropdown[m_index]
    #     month_dropdown.get_attribute("value")


    # def year_expaired(self, y_index: int):
    #     year_dropdown = self.driver.find_elements(By.NAME, "yyyyListbox")
    #     year_dropdown = year_dropdown[y_index]
    #     year_dropdown.get_attribute("value")



    def click_on_card_holder_name(self):
        cardholder_name = self.driver.find_element(By.NAME, "cardholder_name")
        cardholder_name.click()

    def send_keys_on_card_holder_name(self, card_holder_name):
        cardholder_name = self.driver.find_element(By.NAME, "cardholder_name")
        cardholder_name.click()
        cardholder_name.send_keys(card_holder_name)

    def click_on_pay_now_manual_pay_btn(self):
        pay_now_button = self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
        pay_now_button.click()
