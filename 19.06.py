# ############ Задание 1
#
#
#
#
# number = 42
# number_str = str(number)
#
# text = "The answer is: "
# result = number_str + text
#
# print(type(number))
# print(type(number_str))
# print(type(text))
# print(type(result))
#
#
# ############## Задание 2
#
# name = "Илья"
# age = 33
# print(f"Меня зовут {name}, мне {age} лет.")
#
#
# ############## Задание 3
#
# my_list = [1, 2, 3]
# copy_list = my_list.copy()
# copy_list[0] = 10
# print(my_list)
# print(copy_list)
#
#
# ############## Задание 4
#
# # text = float(input("Введите число: "))
# # if text > 0:
# #     print("Положительное")
# # elif text < 0:
# #     print("Отрицательное")
# # else:
# #     print("Ноль")
#
#
# ############## Задание 5
#
#
# person = {
#
#       "name": {
#
#           "first_name": "Иван",
#
#           "last_name": "Иванов"
#
# },
#
#    "address": {
#
#        "city": "Москва",
#
#       "country": "Россия"
#
#     }
#
# }
# person["address"]["city"] =  "Санкт-Петербург"
# person["postal_code"] =  "333777"
# print(person)
#
# ############## Задание 6
#
# x = 1
# while x <= 20:
#     if not x  % 4 == 0:
#      print(x)
#     x += 1
#
#
# ############## Задание 7
#
# with open("fruits.txt", "w", encoding="utf-8") as file:
#     file.write("яблоко,\nбанан,\nапельсин\n")
# with open("fruits.txt", "r", encoding="utf-8") as file:
#     result = file.readlines()
#     print(result)
#
#
# ############## Задание 8
#
# # def greet_user(user_role, user_name = None):
# #     if not None is user_name:
# #         return f"Привет, {user_name}! Ваша роль: {user_role}"
# # result = greet_user()
# # print(result)
#
#
# ############## Задание 9
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def Student(self):
#         print(f"{self.name} {self.age}")
# s = Student("Илья", 33)
# s.Student()
#
# ############## Задание 10
#
# class Animal:
#     name = "Шарик"
#     species = "Собака"
#     def eat(self):
#         pass
#     def sleep(self):
#         pass
# a = Animal()
#
# class Dog(Animal):
#     def bark(self):
#         print("Лаять")
# d = Dog
# d.bark()

import json
import time
from cookies_manager import CookieManager

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://www.freeconferencecall.com/ru/ru/login")

input()

cookies = driver.get_cookies()
with open("cookies.json", "w")as file:
    json.dump(cookies, file, indent=4)
time.sleep(5)