#Строки
#Задание 1
from os import replace

from lesson3 import fruits

text = "Hello, Python!"

print(f"Первые 5 символов: text[:5]")
print(f"Символы с индексами от 7 до 12: text[7:13]")
print(f"Последние 3 символа: text[-3:]")
print(f"Каждый второй символ строки: text[::2]")

#Задание 2
message = "  hello, World!  "

result1 = message.strip()
print(f"Убирает пробелы в начале и конце строки: {result1}")
result2 = result1.upper()
print(f"Приводит строку к верхнему регистру: {result2}")
result3 = result2.replace('WORLD' , 'Python')
print(f"Заменяет 'WORLD' на 'Python': {result3} ")
result4 = result3.startswith('HELLO')
print(f"Проверяет, начинается ли строка с 'HELLO' (после преобразований): {result4}")
result5 = result3.split(',')
print(f"Разделяет строку по запятой (получится список из 2 элементов): {result5} ")


name = "Алексей"
age = 25
hobby = "программированию"

age_str = str(age)
concatenation = "Меня зовут " + name + ", мне " + age_str + " лет, я учусь " + hobby
print(concatenation)
print(f"Меня зовут {name}, мне {age} лет, я учусь {hobby}")


#Задача 3

text = "Программирование на Python - это увлекательно!"

result5 = text.lower()
print(f"Привести строку к нижнему регистру: {result5}")
result6 = result5.replace('увлекательно', 'полезно')
print(f"Заменить слово 'увлекательно' на 'полезно': {result6}")
result7 = 'python' in result6
print(f"Проверить, содержит ли строка подстроку 'python' (после преобразований): {result7}")
result8 =result6.split()
print(f"Разделить строку по пробелам (чтобы получить список слов): {result8}")
#Вывести итоговую строку и результаты проверки (пункт 3)
print(result8)
print(result7)


#Задача 4

secret = "a1b2c3d4e5f6"

result = secret[::2]
print(f"Извлечь все символы на чётных индексах (0, 2, 4...): {result}")
result2 =secret[1::2]
print(f"Извлечь все символы на нечётных индексах (1, 3, 5...): {result2}")
print(f"Четные: {result}. Нечетные: {result2}")

#Задача 5

message = "!!Данные_2023: Важный_Текст; Надо_Обработать!!"

result = message.strip("!")
print(f"Убрать восклицательные знаки по краям: {result}")
result2 = result.replace("_" , " ")
print(f"Заменить все подчёркивания на пробелы: {result2}")
result3 = result2.split(";")
print(f"Разделить строку по точке с запятой (получится 2 части): {result3}")
result4 = result3[1].lower()
print(f"Вторую часть перевести в нижний регистр: {result4}")
result5 = "Результат:" + " " + result3[0] + result4
print(f"Соединить результат: {result5}")

#Задача 6

text = "  Зимний вечер, снег идёт...  "

result = text.strip().replace(" ", "_").upper()

print(f"Итоговый результат: {result}")


#Задача 7


#Создать строку в формате:
#"Погода в Москве: -5°C, снег."

city = "Москва"
city = "Москве"
temperature = -5
weather = "снег"
print(f"Погода в {city}: {temperature}°C, {weather}.")

#задача 8

fruit = "Апельсин"
print(fruit)

#Задача9

item = "автоматизация"
print(item[2])

#Задача10

item = "программирование"
print(item[4:10])

#Задача11

item = "Hello, World!"
result = len(item)
print(result)

#Задача12

word1 = "Привет"
word2 = "Мир"
result =  word1 + " " +  word2
print(result)

#Задача13

name = "Алексей"
age = 25
print(f"Меня зовут {name}, мне {age} лет")

#Задача14

text = "  python is awesome!  "
print(text.strip())

#Задача15

s = "Съешь ещё этих мягких французских булок"
length = len(s)
result = s.split()[-1]
result2 = s.upper()
print(f"Длина: {length}\nПоследнее слово: {result}\nВерхний регистр: {result2}")

#Задача16

word = "ОКОЛО"
result = word[::-1]
print(word==result)

#Задача17

text = "Я изучаю Python"
result = text.replace("изучаю", "люблю")
result2 = result.lower()
print(result2)

#Задача18

text = "Привет, мир!"
print(text)

#Задача19

word = "Кодинг"
print(word[2])

#Задача20

text = "Автоматизация"
print(text[2:7])

#Задача21

message = "Python"
print(len(message))

#Задача22

word1 = "Hello"
word2 = "World"
result = word1 + " " + word2
print(result)

#Задача23

name = "Анна"
age = 25
print(f"{name}, {age} лет")

#Задача24

text = "   робот-пылесос   "
print(text.strip())

#

name = "Илья"
age = 34
print(f"Меня зовут {name}, мне {age} лет.")


#для себя
name = "Илья"
age = 12

last_digit = age % 10
two_last_digits = age % 100  # Для исключений (11-14)

if 11 <= two_last_digits <= 14:
    word = "лет"
elif last_digit == 1:
    word = "год"
elif 2 <= last_digit <= 4:
    word = "года"
else:
    word = "лет"

print(f"Меня зовут {name}, мне {age} {word}.")


#

text = "Программирование"
print(text[0:5])
print(text[-4:])
print(text[5:11])

#

s = "   Hello, World!   "
d = s.strip()
g = d.replace("World", "Python")
f = g.upper()
print(f)

#

word1 = "Автоматизация"
word2 = "тестирования"
word3 = "Python"
result = word1 + " " + word2 + " на "+ word3
print(result)

#

text = "Программист"
print(text[0], text[-1])
print(len(text))
middle = len(text) // 2
print(text[middle])

#

s = "Я изучаю Python и хочу стать разработчиком"
start_result = s.startswith("Я изучаю")
print(start_result)
end_result = s.endswith("разработчиком")
print(end_result)
reeg = s.upper()
print(reeg)

#

path = r"C:\Users\Documents\project\file.txt"
name_file = path[-8:]
print(name_file)
path_file = path[:-8]
print(path_file)
result = path.replace("\\", "/")
print(result)
end_result = result.endswith(".txt")
print(end_result)

#

s = "   Hello, World!   "
s_reg = s.strip()
print(s_reg)
s_upp = s_reg.upper()
print(s_upp)
result = s_upp.replace("WORLD", "PYTHON")
print(result)
print("Hello".lower() in result.lower())

#

text = "  НаПИСАНО Плохо: 2 ошибки, 1 опечатКА.   "
text = text.strip()
text = text.capitalize()
text = text.replace("2", "две").replace("1", "одна")
print(text)