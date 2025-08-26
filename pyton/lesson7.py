#Файлы

#Задача 1


#Задача 2

with open("../data.txt", "r") as file:
    content = file.read()
    print(content.strip())



#Задача 3
with open("../fruits.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#Задача 4

with open("../fruits.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
     print(line.strip())

#задача

with open("../fruits.txt", "a", encoding="utf-8") as file:
    file.write("\nарбуз")
    print(line.strip())

# задача

with open("../my_name.txt", "w", encoding="utf-8") as file:
    file.write("Илья")


with open("../my_name.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Привет, {line.strip()}!")


with open("../my_name.txt", "a", encoding="utf-8") as file:
    file.write(" Стрекаловский")


with open("../my_name.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Привет, {line.strip()}!")


#Задача

with open("../hello.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!")

with open("../hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("../hello.txt", "a", encoding="utf-8") as file:
    file.write("\nЭто мой первый файл!")
with open("../hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"В файле {len(content)} символа")

#

with open("../hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    if "первый" in content:
        print("Да, слово найдено")
    else:
        print("Нет, такого слова нет")


#

with open("../numbers.txt", "w", encoding="utf-8") as file:
    for number in range(1,11):
     file.write(f"{number}\n")


#

with open("../greeting.txt", "w", encoding="utf-8") as file:
    file.write( "Hello, World!")
with open("../greeting.txt", "r", encoding="utf-8")as file:
    content = file.read()
print(content)

#

with open("../colors.txt", "w", encoding="utf-8") as file:
    file.write("синий\n" "белый\n" "зеленый")
with open("../colors.txt", "r", encoding="utf-8") as file:
    content = file.readline()
    print(content)


#

with open("../data.txt", "w", encoding="utf-8") as file:
    file.write("Python\n3.9\n")
with open("../data.txt", "r", encoding="utf-8") as file:
    content = file.readlines()[::-1]
    print(''.join(content))


#

with open("animals.txt", "w", encoding="utf-8") as animal:
    animal.write("кот\nсобака\nпопугай\n")
with open("animals.txt", "r", encoding="utf-8")as animal:
    animals = animal.readlines()
    print(animals)

#

with open("../numbers.txt", "w", encoding="utf-8") as numbers:
    for number in range(1,6):
      numbers.write(f"{number}\n")
with open("../numbers.txt", "r", encoding="utf-8") as numbers:
    number = numbers.readlines()
    for num in number:
     print(num.strip())


#

with open("../greeting.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")
with open("../greeting.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)


#

with open("../data.txt", "w", encoding="utf-8") as file:
    file.write("apple\nbanana\norange\n")
with open("../data.txt", "r", encoding="utf-8") as file:
    result = file.readlines()
    print("".join(result))
    print(f"Количество строк: {len(result)}")
with open("../data.txt", "a", encoding="utf-8") as file:
    file.write("watermelon")
with open("../data.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)


#

with open("../words.txt", "w", encoding="utf-8") as file:
    file.write("яблоко\nгруша\nананас\nвишня\nарбуз\n")
with open("../words.txt", "r", encoding="utf-8") as file:
    results = file.read().splitlines()
    max_result = ""
    max_length = 0
    for result in results:
        if len(result) > max_length:
            max_result = result
            max_length = len(result)
print(f" Самое длинное слово {max_result} состоит из {max_length} слов")

#

with open("../numbers.txt", "w", encoding="utf-8") as file:
    file.write("1\n2\n3\n4\n5\n")
with open("../numbers.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)


#

with open("../data.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")
with open("../data.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)


#

with open("../notes.txt", "w", encoding="utf-8") as file:
    file.write("Понедельник: учеба\n")
with open("../notes.txt", "a", encoding="utf-8")as file:
    file.write("Вторник: практика\n")
with open("../notes.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)

#

with open("../secret.txt", "w", encoding="utf-8")as file:
    file.write("Секретный текст")
with open("../secret.txt", "r", encoding="utf-8") as file:
    text = "Файл не найден, создайте его!" if not file.read() else print(file.read())

#

with open("../test.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")
with open("../test.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)

#

with open("../output.txt", "w", encoding="utf-8") as file:
    file.write("Python is awesome!")

#

with open("../notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")


#

with open("../data.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)

#

with open("../log.txt", "w", encoding="utf-8") as file:
    file.write("2023-11-15")

#

with open("../lines.txt", "w", encoding="utf-8") as file:
    file.write("1: первая строка,\n2: вторая строка,\n3: третья строка\n")
with open("../lines.txt", "r", encoding="utf-8") as file:
    result = file.read()
print(result)


#

#P.S. Для проверки существования файла нужно:

import os
if os.path.exists("../lines.txt"):
    print("Файл найден")
else:
    print( "Файл не найден")


#(Построчное чтение с нумерацией):
with open("../lines.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\nВторая строка\nТретья строка")

with open("../lines.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")