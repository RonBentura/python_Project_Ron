from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


service_chrome = Service(r"C:\Users\IMOE001\Desktop\רון (לא לגעת) !!!\WEB Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)
driver.implicitly_wait(20)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

account_menu = driver.find_element(By.ID, "menuUserLink")
account_menu.click()

# create_account_button = driver.find_element(By.CLASS_NAME, "create-new-account")
# create_account_button.click()

element = driver.find_element(By.CLASS_NAME, "create-new-account")
driver.execute_script("arguments[0].click();",element)

username_field = driver.find_element(By.NAME, "usernameRegisterPage")
username_field.click()
username_field.send_keys("rontil122")

password_field = driver.find_element(By.NAME, "passwordRegisterPage")
password_field.click()
password_field.send_keys("Ronbn28")

password_confirm_field = driver.find_element(By.NAME, "confirm_passwordRegisterPage")
password_confirm_field.click()
password_confirm_field.send_keys("Ronbn28")

email_field = driver.find_element(By.NAME, "emailRegisterPage")
email_field.click()
email_field.send_keys("ronbn28122@gmail.com")

first_name_field = driver.find_element(By.NAME, "first_nameRegisterPage")
first_name_field.click()
first_name_field.send_keys("ron")

last_name_field = driver.find_element(By.NAME, "last_nameRegisterPage")
last_name_field.click()
last_name_field.send_keys("bentura")

phone_number_field = driver.find_element(By.NAME, "phone_numberRegisterPage")
phone_number_field.click()
phone_number_field.send_keys("0587974847")

country_field = driver.find_element(By.CSS_SELECTOR, "[label='Israel']")
country_field.click()

city_field = driver.find_element(By.NAME, "cityRegisterPage")
city_field.click()
city_field.send_keys("netanya")

address_field = driver.find_element(By.NAME, "addressRegisterPage")
address_field.click()
address_field.send_keys("wolfson 34")

state_province_region_field = driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage")
state_province_region_field.click()
state_province_region_field.send_keys("merkaz")

postal_code_field = driver.find_element(By.NAME, "postal_codeRegisterPage")
postal_code_field.click()
postal_code_field.send_keys("4237434")

privacy_notice = driver.find_element(By.NAME, "i_agree")
privacy_notice.click()

register_button = driver.find_element(By.ID, "register_btnundefined")
register_button.click()

account_menu = driver.find_element(By.ID, "menuUserSVGPath")
account_menu.click()

sign_out = driver.find_element(By.CSS_SELECTOR, "[translate='Sign_out'][role='link']")
sign_out.click()

# element = driver.find_element(By.ID, "menuUserLink")
# ActionChains(driver).move_to_element(element).perform()

account_menu = driver.find_element(By.ID, "menuUserLink")
account_menu.click()

username_field_log_in = driver.find_element(By.NAME, "username")
username_field_log_in.click()
username_field_log_in.send_keys("rontil122")

password_field_log_in = driver.find_element(By.NAME, "password")
password_field_log_in.click()
password_field_log_in.send_keys("Ronbn28")

# element = driver.find_element(By.ID, "menuUserLink")
# ActionChains(driver).move_to_element(element).perform()

account_menu = driver.find_element(By.ID, "menuUserLink")
account_menu.click()

my_account_button = driver.find_element(By.CSS_SELECTOR, "label[translate='My_account'][class='option roboto-medium ng-scope']")
my_account_button.click()

delete_account = driver.find_element(By.CLASS_NAME, "deleteBtnText")
delete_account.click()

confirm_delete = driver.find_element(By.CSS_SELECTOR, "[data-ng-click='deleteAccountConfirmed()']")
confirm_delete.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "speakersImg")))

sign_in = driver.find_element(By.CSS_SELECTOR, "#sign_in_btnundefined")
sign_in.click()

account_menu = driver.find_element(By.ID, "menuUserSVGPath")
account_menu.click()

orders_history = driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']")
orders_history.click()

account_menu = driver.find_element(By.ID, "menuUserSVGPath")
account_menu.click()

my_account_button = driver.find_element(By.CSS_SELECTOR, "label[translate='My_account'][class='option roboto-medium ng-scope']")
my_account_button.click()

delete_account = driver.find_element(By.CLASS_NAME, "deleteBtnText")
delete_account.click()

confirm_delete = driver.find_element(By.CSS_SELECTOR, "[data-ng-click='deleteAccountConfirmed()']")
confirm_delete.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "speakersImg")))

