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