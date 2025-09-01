# import time
#
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)
#
# #Локаторы авторизации
# USER_NAME = ("xpath", "//input[@id='user-name']")
# PASSWORD = ("xpath", "//input[@id='password']")
# LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")
# #Локаторы добавления товаров
# BACKPACK = ("xpath", "//a[@id='item_4_title_link']")
# ADD = ("xpath", "//button[@id='add-to-cart']")
# BACK_TO_PRODUCTS = ("xpath", "//button[@id='back-to-products']")
# BIKE_LIGHT = ("xpath", "//a[@id='item_0_title_link']")
# #Локаторы корзины
# CART_LINK = ("xpath", "//a[@class='shopping_cart_link']")
# CHECKOUT = ("xpath", "//button[@id='checkout']")
# #Локаторы перс данных и оформления
# FIRST_NAME = ("xpath", "//input[@data-test='firstName']")
# LAST_NAME = ("xpath", "//input[@data-test='lastName']")
# POSTAL_CODE = ("xpath", "//input[@data-test='postalCode']")
# CONTINUE = ("xpath", "//input[@id='continue']")
# FINISH = ("xpath", "//button[@id='finish']")
#
# driver.get("https://www.saucedemo.com/")
# assert driver.title == "Swag Labs", "Error in title"
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10,1)
# # Авторизация
# wait.until(EC.visibility_of_element_located(USER_NAME)).send_keys("standard_user")
# time.sleep(2)
# wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("secret_sauce")
# time.sleep(2)
# wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()
# time.sleep(2)
#
# # Добавляю в корзину первый определенный товар
# wait.until(EC.visibility_of_element_located(BACKPACK)).click()
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in Backpack"
# time.sleep(2)
#
# wait.until(EC.visibility_of_element_located(ADD)).click()
# assert driver.find_element("xpath", "//button[@id='remove']"), "Error in add_Sauce_Labs"
# time.sleep(2)
#
# wait.until(EC.visibility_of_element_located(BACK_TO_PRODUCTS)).click()
# assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products"
# time.sleep(2)
#
# # Добавляю в корзину второй определенный товар
# wait.until(EC.visibility_of_element_located(BIKE_LIGHT)).click()
# time.sleep(2)
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in Bike Light"
#
# wait.until(EC.visibility_of_element_located(ADD)).click()
# assert driver.find_element("xpath", "//button[@id='remove']"), "Error in add_Sauce_Labs"
# time.sleep(2)
#
# wait.until(EC.visibility_of_element_located(BACK_TO_PRODUCTS)).click()
# assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products"
# time.sleep(2)
#
# #Перехожу в корзину
# wait.until(EC.visibility_of_element_located(CART_LINK)).click()
# time.sleep(2)
# assert driver.find_element("xpath", "//span[text()='Your Cart']"), "Error in basket"
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in basket-Backpack"
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in basket-Bike Light"
# #Перехожу к оформлению
# wait.until(EC.visibility_of_element_located(CHECKOUT)).click()
# assert driver.find_element("xpath", "//span[text()='Checkout: Your Information']"), "Error in Checkout"
# time.sleep(2)
#
# #Ввожу имя
# wait.until(EC.visibility_of_element_located(FIRST_NAME)).clear()
# wait.until(EC.visibility_of_element_located(FIRST_NAME)).send_keys("Илья")
# assert driver.find_element("xpath", "//input[@value='Илья']"), "Error in firstName"
# time.sleep(2)
#
# #Ввожу фамилию
# wait.until(EC.visibility_of_element_located(LAST_NAME)).clear()
# wait.until(EC.visibility_of_element_located(LAST_NAME)).send_keys("Стрекаловский")
# assert driver.find_element("xpath", "//input[@value='Стрекаловский']"), "Error in lastName"
# time.sleep(2)
#
# #Ввожу zip/postal-code
# wait.until(EC.visibility_of_element_located(POSTAL_CODE)).clear()
# wait.until(EC.visibility_of_element_located(POSTAL_CODE)).send_keys("1234")
# assert driver.find_element("xpath", "//input[@value='1234']"), "Error in postal_code"
# time.sleep(2)
#
# #Подтверждаю
# wait.until(EC.visibility_of_element_located(CONTINUE)).click()
# assert driver.find_element("xpath", "//span[text()='Checkout: Overview']"), "Error in Checkout"
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in Checkout-Backpack"
# assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in Checkout-Bike Light"
# time.sleep(2)
#
# #Завершаю заказ
# wait.until(EC.visibility_of_element_located(FINISH)).click()
# assert driver.find_element("xpath", "//span[text()='Checkout: Complete!']"), "Error in Checkout: Complete!"
# time.sleep(2)
#
# #Возвращаюсь на начальную страницу
# wait.until(EC.visibility_of_element_located(BACK_TO_PRODUCTS)).click()
# assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products finish"
#
# time.sleep(5)