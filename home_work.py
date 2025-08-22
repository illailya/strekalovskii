import time


from selenium import webdriver



options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
assert driver.title == "Swag Labs", "Error in title"
time.sleep(2)

user_name = driver.find_element("xpath", "//input[@id='user-name']")
user_name.send_keys("standard_user")
# time.sleep(2)
password = driver.find_element("xpath", "//input[@id='password']")
password.send_keys("secret_sauce")
# time.sleep(2)
login = driver.find_element("xpath", "//input[@id='login-button']").click()
assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products"
# time.sleep(2)

# Добавляю в корзину первый определенный товар
Backpack = driver.find_element("xpath", "//a[@id='item_4_title_link']").click()
assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in Backpack"
time.sleep(2)

add_Backpack = driver.find_element("xpath", "//button[@id='add-to-cart']").click()
assert driver.find_element("xpath", "//button[@id='remove']"), "Error in add_Sauce_Labs"
time.sleep(2)

back_to_products = driver.find_element("xpath", "//button[@id='back-to-products']").click()
assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products"
time.sleep(2)

# Добавляю в корзину второй определенный товар
Bike_Light = driver.find_element("xpath", "//a[@id='item_0_title_link']").click()
time.sleep(2)
assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in Bike Light"
add_Bike_Light = driver.find_element("xpath", "//button[@id='add-to-cart']").click()
assert driver.find_element("xpath", "//button[@id='remove']"), "Error in add_Sauce_Labs"
time.sleep(2)

back_to_products = driver.find_element("xpath", "//button[@id='back-to-products']").click()
assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products"
time.sleep(2)

#Перехожу в корзину
basket = driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
time.sleep(2)
assert driver.find_element("xpath", "//span[text()='Your Cart']"), "Error in basket"
assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in basket-Backpack"
assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in basket-Bike Light"
#Перехожу к оформлению
Checkout = driver.find_element("xpath", "//button[@id='checkout']").click()
assert driver.find_element("xpath", "//span[text()='Checkout: Your Information']"), "Error in Checkout"
time.sleep(2)

#Ввожу имя
firstName = driver.find_element("xpath", "//input[@data-test='firstName']")
firstName.clear()
firstName.send_keys("Илья")
assert driver.find_element("xpath", "//input[@value='Илья']"), "Error in firstName"
time.sleep(2)

#Ввожу фамилию
lastName = driver.find_element("xpath", "//input[@data-test='lastName']")
lastName.clear()
lastName.send_keys("Стрекаловский")
assert driver.find_element("xpath", "//input[@value='Стрекаловский']"), "Error in lastName"
time.sleep(2)

#Ввожу zip/postal-code
postal_code = driver.find_element("xpath", "//input[@data-test='postalCode']")
postal_code.clear()
postal_code.send_keys("1234")
assert driver.find_element("xpath", "//input[@value='1234']"), "Error in postal_code"
time.sleep(2)

#Подтверждаю
continue_click = driver.find_element("xpath", "//input[@id='continue']").click()
assert driver.find_element("xpath", "//span[text()='Checkout: Overview']"), "Error in Checkout"
assert driver.find_element("xpath", "//div[text()='Sauce Labs Backpack']"), "Error in Checkout-Backpack"
assert driver.find_element("xpath", "//div[text()='Sauce Labs Bike Light']"), "Error in Checkout-Bike Light"
time.sleep(2)

#Завершаю заказ
finish = driver.find_element("xpath", "//button[@id='finish']").click()
assert driver.find_element("xpath", "//span[text()='Checkout: Complete!']"), "Error in Checkout: Complete!"
time.sleep(2)

#Возвращаюсь на начальную страницу
Back_Home = driver.find_element("xpath", "//button[@id='back-to-products']").click()
assert driver.find_element("xpath", "//span[text()='Products']"), "Error in products finish"

time.sleep(5)