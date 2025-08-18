# import time
#
# from selenium import webdriver
# from selenium.webdriver import Keys
#
#
# driver = webdriver.Chrome()
# driver.get("http://the-internet.herokuapp.com/key_presses")
#
# filed = driver.find_element("xpath", "//input[@id='target']")
# filed.send_keys("hello")
# time.sleep(3)
# filed.send_keys(Keys.CONTROL+"A")
# time.sleep(3)
# filed.send_keys(Keys.BACK_SPACE)
# time.sleep(3)
#
# # first_name_filed = driver.find_element("xpath", "//input[@placeholder='Full Name']")
# # first_name_filed.send_keys("Илья")
# # first_name_filed.get_attribute("value")
# # assert first_name_filed.get_attribute("value") == "Илья", "error in first_name"
# #
# # Email_filed = driver.find_element("xpath", "//input[@id='userEmail']")
# # Email_filed.send_keys("frf@jg.com")
# # Email_filed.get_attribute("value")
# # assert Email_filed.get_attribute("value") == "frf@jg.com", "error in Email_filed"
# #
# # Adres_filed = driver.find_element("xpath", "//textarea[@id='currentAddress']")
# # Adres_filed.send_keys("lenina")
# # Adres_filed.get_attribute("value")
# # assert Adres_filed.get_attribute("value") == "lenina", "error in Adres_filed"
# # time.sleep(3)
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# # options.add_argument("--incognito")
# # options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
# # options.page_load_strategy = "eager"
#
# FILE_UPLOAD = ("xpath", "//input[@id='uploadFile']")
#
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://demoqa.com/upload-download")
#
# fild_field = driver.find_element(*FILE_UPLOAD)
# fild_field.send_keys(r"D:\pyton\example.jpeg")
# time.sleep(3)
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("--windows-size=1920,1080")
#
# VISIBLE_AFTER = ("xpath", "//button[@id='visibleAfter']")
# ANABLE_AFTER = ("xpath", "//button[@id='enableAfter']")
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://demoqa.com/dynamic-properties")
#
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# wait.until(EC.element_to_be_clickable(ANABLE_AFTER))
#
# time.sleep(5)
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import  WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = webdriver.ChromeOptions()
# options.add_argument("--windows-size=1920, 1080")
# options.add_argument("--disable-dlink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)


# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver,10,1)
# driver.get("https://demoqa.com/alerts")
#
# driver.find_element("xpath","//button[@id='promtButton']").click()
# alert = wait.until(EC.alert_is_present())
# time.sleep(3)
# alert.send_keys("ilua")
# time.sleep(3)
# alert.accept()
#
# time.sleep(3)

# import json
# import time
# from cookies_manager import CookieManager
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=1920,1080")
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.freeconferencecall.com/ru/ru/login")
#
#
#
# cookies_manager = CookieManager(driver)
# cookies_manager.load()
# time.sleep(3)
#
#
# fruits = ["яблоко", "банан", "апельсин"]
# for fruit in fruits:
#     print(fruit)
#
#
# for num in range(2,11,2):
#     print(num)
#
#
# a = 5
# while  a >= 1:
#
#     print(a)
#     a -= 1
#
# numbers = [10, 20, 30, 40, 50]
# for number in numbers:
#     print(number)
#     if number == 30:
#         break
#
# for num in range(1,6):
#     print(num**2)
#
# nums = [3, 7, 12, 8, 5, 10]
# for num in nums:
#     if num %2==0:
#         print(num)
#
# # total = 0
# # while True:
# #  num = int(input("Введите число: "))
# #  if num == 0:
# #      break
# #  total += num
# # print(f"Сумма {total}")
#
# for num in range(10,0,-1):
#     print(num)
#
# temps = [25, 30, 15, 32, 10, 28]
# for temp in temps:
#     if temp > 28:
#         print("Жарко")
#     elif temp < 15:
#         print("Холодно")
#     else:
#         print("Нормально")
#
# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, Python!")
# with open("test.txt", "r", encoding="utf-8") as file:
#     result = file.read()
#     print(result)
#
# with open("notes.txt", "w") as file:
#     file.write(f"Первый запуск программы")
# with open("notes.txt", "a") as file:
#     file.write("\nДобавлена новая запись")
# with open("notes.txt", "r") as file:
#     result = file.read()
#     print(result)
#
#
# with open("lines.txt", "w") as file:
#     file.write("Первая строка\nВторая строка\nТретья строка")
# with open("lines.txt", "r") as file:
#     results = file.readlines()
#     for result in results:
#         print(result.strip())
#
#
#
# data = ["Python", "JavaScript", "C++"]
# for text in data:
#     with open("languages.txt", "a") as file:
#         file.write(f"{text}\n")
# with open("languages.txt", "r") as file:
#     for lang in file:
#         print(lang)
#
#
# def greet():
#     print("Привет, мир!")
#
# def multiply(a, b):
#     return a * b
# print(multiply(5,5))
#
#
# def welcome(name, greeting="Привет"):
#     return f"{greeting}, {name}!"
# print(welcome("ilya"))
#
# def is_even(number):
#     if number % 2 ==0:
#         return True
#     else:
#         return False
# print(is_even(5))
#
#
# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
# @uppercase_decorator
# def text():
#     return "Привет"
# print(text())