#Задание 1
from os import replace

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

fruits = ["Яблоко", "Банан", "Киви"]
print(fruits)

#задача9

numbers = [10, 20, 30]

numbers.append(40)
numbers[1] = 25
print(numbers)