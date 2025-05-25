#Словари

#Задача1

student = {
    "name": "Алекс",
    "age": 20,
    "course": 1
}
print(student)

#Задача2

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
model = car["model"]
print(model)
car["year"] = 2022
car["color"] = "red"
print(car)

#адача3

laptop = {
    "brand": "HP",
    "ram": 16,
    "ssd": 512,
    "os": "Windows"
}
del laptop["os"]
print(laptop)
if "ssd" in laptop:
    print("SSD присутствует")
else:
    print("SSD отсутствует")
if 16 in laptop.values():
    print("ram 16 есть в словаре")
else:
    print("ram 16 отсутствует в словаре")


#Задача 4

country = {
    "name": "Япония",
    "capital": "Токио",
    "population": 126_500_000,
    "island": True
}

keys_list = country.keys()
values_list = country.values()
has_tokyo = "Токио" in values_list
print(f"Ключи: {keys_list}\nЗначения: {values_list} Значение 'Токио' присутствует: {has_tokyo}")

#Задача 5

fruit = {
"name": "яблоко",
"color": "зелёное",
"price": 50
}
print(fruit)

#задача 6

book = {
    "title": "Гарри Поттер",
    "author": "Дж. Роулинг",
    "year": 1997
}
print(book["author"])

#Задача 7

phone = {
    "brand": "Samsung",
    "model": "Galaxy S21"
}
phone["year"] = 2021
print(phone)

#Задача 8

user = {
    "login": "super_user",
    "email": "user@mail.com",
    "age": 25,
    "is_verified": False
}
age = user.pop("age")
print(age)
if "is_verified" in user:
    print(user["is_verified"])
else:
    print("Ключ отсутствует")