from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#speakersImg")

    def mice_category(self):
        return self.driver.find_element(By.ID, "miceImg")

    def tablets_category(self):
        return self.driver.find_element(By.ID, "tabletsImg")

    def get_speakers_category(self):
        self.speakers_category().click()

    def get_mice_category(self):
        self.mice_category().click()

    def get_tablets_category(self):
        self.tablets_category().click()