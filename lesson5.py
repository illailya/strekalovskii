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


#

fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
print(fruit_colors)

ages = {"Alice": 25, "Bob": 30, "Charlie": 22}
bob_age = ages["Bob"]
print(f"Возраст: {bob_age} лет")

#

country_capitals = {"France": "Paris", "Japan": "Tokyo"}
country_capitals["Germany"] = "Berlin"
country_capitals["Japan"] = "Kyoto"
print(country_capitals)

#

inventory = {"apple": 10, "banana": 5, "orange": 8}
del inventory["banana"]
print(inventory)


book = {"title": "1984", "author": "Orwell", "year": 1949}
print(book.values())
print(book.keys())
print(book.items())

#

user = {"name": "Alice", "age": 25, "email": "alice@example.com"}
if "age" in user.keys():
    print(True)
else:
    print(False)
if "bob@example.com" in user.values():
    print(True)
else:
    print(False)


#

student = {"name": "Alex", "age": 20, "courses": ["Math", "Physics"]}
print(student["age"])

#

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
car["color"] = "red"
car["year"] = 2022
print(car)

#

inventory = {"apples": 10, "bananas": 5, "oranges": 8, "grapes": 15}
del inventory["bananas"]
print(inventory)

#

print("Ключ есть:", "name" in user)
print("Значение есть:", "alice@example.com" in user.values())

#

book = {"title": "1984", "author": "George Orwell", "year": 1949}
print("Ключи: ", book.keys())
print("Значения: ", book.values())
print("Пары:", book.items())


#

car = {"Toyota": 1998, "BMW": 2005, "mersedes": 1998, "audi": 2001}
print(car)
mers = list(car.keys())[2]
result = car[mers]
print(result)

#

cities = {"Москва": 12500, "Санкт-Петербург": 5400, "Омск": 5478, "Пермь": 4745}
maximum = max(cities, key=cities.get)
print(maximum)
cities["Казань"] = 1300
for city in cities:
    cities[city] = int(cities[city] * 1.05)
print(cities)

#

countries = {
    "Франция": {"capital": "Париж", "population": 67.4, "languages": ["французский"]},
    "Канада": {"capital": "Оттава", "population": 38.0, "languages": ["английский", "французский"]},
"Россия": {"capital": "Москва", "population": 165.4, "languages": ["Русский"]}
}
countries["Беларусь"] = {"capital": "Минск", "population": 16.4, "languages": ["Русский"]}
print(countries)

#

colors = {"red": "красный", "blue": "синий", "green": "зеленый"}
print("синий" in colors.values())

#

person = {"name": "Сергей", "age": 25}
person.update({"city": "Казань"})
print(person)

#

original = {"a": 1, "b": 2}
copi1 = original.copy()
copi1.update({"c": 3})
print(copi1)
print(original)

#

data = {"id": 101, "status": "active", "score": 45}
delet = data.pop("status")
print(data)
print(delet)

#

user = {"name": "Анна", "email": "anna@example.com", "age": 28}
delet1 = user.pop("phone", None)
print(delet1)
if delet1 is None:
    print("Ключ 'phone' отсутствует")


#

fruit_colors = {
    "Яблоко": "Красный",
    "Банан": "Желтый",
    "Апельсин": "Оранжевый"
}
print(fruit_colors)

#

capitals = {"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"}
result = capitals["Франция"]
result2 = capitals["Япония"]
print(result, result2)

#

inventory = {"яблоки": 10, "бананы": 5}
inventory["апельсин"] = 8
inventory["яблоки"] = 15
print(inventory)

#

student = {"name": "Алексей", "age": 20, "course": "Python", "grade": "A"}
del student["grade"]
deleted = student.pop("age")
print(student)
print(deleted)

#

book = {
    "title": "Гарри Поттер",
    "author": "Дж.К. Роулинг",
    "year": 1997
}
print(book.keys())
print(book.values())
print(book.items())

#

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022
}
print("color" in car)
print("Camry" in car.values())
print(car.get("model"))

#

grades = {}
grades["Алексей"] = 5
grades["Мария"] = 4
grades["Иван"] = 3
print(grades)
grades["Алексей"] += 1
print(grades)
print("Екатерина" in grades.keys())

#

device = {
    "type": "smartphone",
    "brand": "Xiaomi",
    "price": 25000
}
copi_device = device.copy()
device.clear()
print(copi_device)
print(device)

#

# exchange = {"USD": 75.5, "EUR": 80.2, "CNY": 11.3}
# currency = input("Введите сумму: ").upper()

#

# prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
# name_fruit = input("Введите название фрукта: ").lower()
# if name_fruit in prices:
#     print(f"Цена {name_fruit} - {prices[name_fruit]}")
# else:
#     print("Фрукт не найден")

#

student = {
    'name': 'Alex',
    'age': 20,
    'university': 'MIT'
}
print(student["age"])

#

car = {
    'brand': 'Toyota',
    'model': 'Corolla'
}
car["year"] = 2020
car["model"] = 'Camry'
print(car)

#

laptop = {
    'brand': 'Dell',
    'RAM': '16GB',
    'price': 1500,
    'color': 'silver'
}
del laptop['price']
print(laptop)

#

book = {
    'title': 'Гарри Поттер',
    'author': 'Дж.К. Роулинг',
    'year': 1997,
    'pages': 400
}
print(list(book))
print(list(book.values()))

#

movie = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}
print(f"Есть ключ 'rating'? {"rating" in movie}")
print(f"Есть значение 'Christopher Nolan'? {'Christopher Nolan' in movie.values()}")

#

smartphone = {
    'model': 'Galaxy S21',
    'brand': 'Samsung',
    'storage': 128,
    'color': 'black'
}
smartphone["price"] = 800
del smartphone["color"]
print(f"Обновлённый словарь: {smartphone}")
print(f"Ключ 'brand' есть? {'brand' in smartphone}")

#

student = {
    'name': 'Алексей',
    'grades': {
        'math': 90,
        'physics': 85,
        'history': 78
    }
}
physics_grade = student['grades']["physics"]
print(f"Оценка по физике: {physics_grade}")
student['grades']['chemistry'] = 82
print(f"Обновленный словарь: {student}")