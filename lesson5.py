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