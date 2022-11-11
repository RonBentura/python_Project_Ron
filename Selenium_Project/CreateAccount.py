from selenium import webdriver
from selenium.webdriver.common.by import By


class CreateAccount:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def registration(self,username,email,password):
        registration = self.driver.find_element(By.ID, "registration_btnundefined")
        registration.click()
        self.send_keys_on_username_registration_page(username)
        self.send_keys_on_email_registration_page(email)
        self.send_keys_on_password_registration_page(password)
        self.send_keys_on_password_confirm_registration_page(password)
        self.click_on_privacy_notice()
        self.click_on_registration_btn()

    def click_on_username_registration_page(self):
        username_field = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username_field.click()

    def send_keys_on_username_registration_page(self, username):
        username_field = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username_field.click()
        username_field.send_keys(username)

    def click_on_password_registration_page(self):
        password_field = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password_field.click()

    def send_keys_on_password_registration_page(self, password):
        password_field = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password_field.click()
        password_field.send_keys(password)

    def click_on_password_confirm_registration_page(self):
        password_confirm_field = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        password_confirm_field.click()

    def send_keys_on_password_confirm_registration_page(self, password_confirm):
        password_confirm_field = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        password_confirm_field.click()
        password_confirm_field.send_keys(password_confirm)

    def click_on_email_registration_page(self):
        email_field = self.driver.find_element(By.NAME, "emailRegisterPage")
        email_field.click()

    def send_keys_on_email_registration_page(self, email):
        email_field = self.driver.find_element(By.NAME, "emailRegisterPage")
        email_field.click()
        email_field.send_keys(email)

    def click_on_privacy_notice(self):
        privacy_notice = self.driver.find_element(By.NAME, "i_agree")
        privacy_notice.click()

    def click_on_registration_btn(self):
        register_button = self.driver.find_element(By.ID, "register_btnundefined")
        register_button.click()

