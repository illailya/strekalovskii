import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка инкогнито режима
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")

#Локаторы авторизации
USER_NAME = ("xpath", "//input[@id='user-name']")
PASSWORD = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

wait = WebDriverWait(driver, 10,1)
# Авторизация
wait.until(EC.visibility_of_element_located(USER_NAME)).send_keys("standard_user")
time.sleep(2)
wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("secret_sauce")
time.sleep(2)
wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()
time.sleep(2)

# Дальнейшие действия после успешного входа
# ...

driver.quit()