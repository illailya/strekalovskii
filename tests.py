import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Настройка инкогнито режима
options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Авторизация
driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
time.sleep(2)
driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
time.sleep(2)
driver.find_element("xpath", "//input[@id='login-button']").click()
time.sleep(2)

# Дальнейшие действия после успешного входа
# ...

driver.quit()