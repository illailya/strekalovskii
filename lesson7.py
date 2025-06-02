#Файлы
from lesson1 import count
from lesson3 import fruits

#Задача 1


#Задача 2

with open("data.txt", "r") as file:
    content = file.read()
    print(content.strip())



#Задача 3
with open("fruits.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#Задача 4

with open("fruits.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
     print(line.strip())

#задача

with open("fruits.txt", "a", encoding="utf-8") as file:
    file.write("\nарбуз")
    print(line.strip())

# задача

with open("my_name.txt", "w", encoding="utf-8") as file:
    file.write("Илья")


with open("my_name.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Привет, {line.strip()}!")


with open("my_name.txt", "a", encoding="utf-8") as file:
    file.write(" Стрекаловский")


with open("my_name.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Привет, {line.strip()}!")


#Задача

with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!")

with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("\nЭто мой первый файл!")
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"В файле {len(content)} символа")

#

with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    if "первый" in content:
        print("Да, слово найдено")
    else:
        print("Нет, такого слова нет")