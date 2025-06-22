#Переменные и типы данных
# Задача 1 (Арифметические операции)
# Задание:
# Вычисли сумму, разность, произведение и частное этих чисел и выведи результат одной строкой в формате:
from lesson2 import result

a = 10
b = 2
x = a + b
y = a - b
z = a * b
w = a / b
print(f'Сумма: {x}, Разность: {y}, Произведение: {z}, Частное: {w}')
# не до конца понял почему именно f надо ставить после print


# Задача 2 (Преобразование типов данных)
# Преобразуй number_str в целое число и сохрани в переменную number_int.
# Преобразуй is_valid в строку и сохрани в переменную is_valid_str.
# Выведи обе новые переменные в формате:
# "Число: X, Флаг: Y" (где X — число, Y — строка)

number_str = "123"
is_valid = True
number_int = int(number_str)
is_valid_str = str(is_valid)
print(f"Число: {number_int}, Флаг: {is_valid_str}")


#Задача 3 (Операции сравнения)
#Сравни x и y и выведи результаты всех основных операций сравнения в формате:
"x > y: A, x < y: B, x == y: C, x != y: D, x >= y: E, x <= y: F"
#где:
#A, B, C, D, E, F — результаты проверок (True или False).

x = 15
y = 10
A = (x > y)
B = (x < y)
C = (x == y)
D = (x != y)
E = (x >= y)
F = (x <= y)
print(f"x > y: {A}, x < y: {B}, x == y: {C}, x != y: {D}, x >= y: {E}, x <= y: {F}")


#Задача 4 (Переопределение переменных)
#Переопредели переменные, изменив их значения:
#name → "Bob"
#age → увеличить на 3
#score → уменьшить на 10.5
#Выведи новые значения в формате:
#"Имя: X, Возраст: Y, Оценка: Z"

name = "Alice"
age = 25
score = 89.5

name = "Bob"
age = (age + 3)
score = (score - 10.5)
print(f"Имя: {name}, Возраст: {age}, Оценка: {score}")


#Задача 5 (Именование переменных)
#Переименуйте переменные по правилам PEP 8:
#Используйте осмысленные имена на английском
#Для имён применяйте snake_case (слова_через_подчёркивание)
#Перепишите строку d с использованием f-строки
#Выведите результат
#Требования:
#Новые имена должны чётко отражать назначение переменных
#В f-строке не используйте str()

a = "John"
name = a
b = 30
age = b
c = 85.5
Score = c

#d = a + " is " + str(b) + " years old. Score: " + str(c)

print(f"{name} is {age} years old. Score:  {Score}")


#Напиши код, который объявляет две переменные a = 10 и b = 3, затем выводит результат их:
#сложения,
#вычитания,
#умножения,
#деления,
#целочисленного деления,
#возведения в степень (a в степень b),
#остатка от деления (a % b).
#Вывод каждого результата должен быть на отдельной строке.

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)


#Напиши код, который:

#Преобразует num_str в целое число и выводит результат.
#Преобразует num_float в строку и выводит результат.
#Преобразует num_int в число с плавающей точкой и выводит результат.
#Складывает преобразованную num_str и num_int и выводит результат.
#Вывод каждого пункта должен быть на отдельной строке.

num_str = "123"
num_float = 45.67
num_int = 89

num_int = int(num_str)
num_str = str(num_float)
num_float = float(num_int)
print(num_int)
print(num_str)
print(num_float)


#Задача 6

name = "Анна"

print(type(name))

#Задача 7

num_str = "10"
num_int = 5
num2 = int(num_str)
print(num_int + num2)

#Задача8

x = 7
y = 12

print(x > y, x < y, x == y)


#Задача9

weather = "солнечно"
print(weather)
weather = "дождь"
print(weather)

#Задача10

one_st_place = "Иван"
my_variable = 42
class_aut = "Автомобиль"
print(one_st_place, my_variable, class_aut)

#Задача11

a = 3.14
b = False
c = "25"

print(f"{type(a)}\n{type(b)}\n{type(c)}")

#Задача12

num_1 = 15
num_2 = 7
result = num_1 + num_2
print(f"Сумма чисел: {result}")

#Задача13

value = 3.14
result = type(value)
print(result)

#Задача14

num_1 = 10
num_2 = 20
if num_1 < num_2:
    print(True)
else:
    print(False)

#Задача15

val_str = "123"
val_int = int(val_str)
print(val_int*2)

#Задача16

user_age = 25
print(user_age)

#Задача17

count = 5
count = 10
result = count + 3
print(result)

#Задача18

name = "Anna"
score = 95
print(f"{name}, {score}")

#Задача19

num_1 = 17
num_2 = 3
result = num_1 % num_2
print(result)

#

length = 5
width = 3
result = length * width
print(result)

#

number_str = "10"
number_int = int(number_str)
print(type(number_int))

#

a = 7
b = 12
if a < b:
    print(True)
else:
    print(False)
if a == b:
    print(True)
else:
    print(False)

#

student = 25
print(f"Количество студентов: {student}")


#

price = 100
price = 120
print(f"Новая цена: {price}")
if price > 110:
  print("Дорого!")


#

item = "Книга"
weight = 0.5
quantity = 3
print(f"Тип item: {type(item)}")
print(f"Тип weight: {type(weight)}")
print(f"Тип quantity: {type(quantity)}")

#

a = 5
b = 3
print(f"Сложение: {a+b}")
print(f"Вычетание: {a-b}")
print(f"Умножение: {a*b}")
print(f"Деление: {a//b}")


#

num = 10
text = "Python"
flag = True
print(type(num))
print(type(text))
print(type(flag))

#

x = 7
y = 10
print(x > y)
print(x <= y)
print(x != y)

#

a = "123"  # строка
b = 45     # целое число
c = 3.14   # дробное число

a_num = int(a)
b_string = str(b)
c_num = int(c)
print(type(a_num))
print(type(b_string))
print(type(c_num))

#

counter = 0
counter = 5
counter = "готово"
print(counter)

#

num1 = "50"   # строка
num2 = 40     # целое число

num1_int = int(num1)
print(num1_int > num2)
print(num1_int == num2)

#

price = "150"
discount = 30
is_valid = "True"

int_price = int(price)
boll_is_valid = bool(is_valid)
result_discount = int_price- (150 * (30/100))
print(result_discount)
print(type(boll_is_valid))
print(boll_is_valid)

#

a = 7
b ="13"
c =[1, 2, 3]
print(type(a), type(b), type(c))

#

temperature = 25
humidity = 70
result = temperature > 20 and humidity < 80
print(result)

#

price = "150.5"
float_price = float(price)
total = float_price * 2
print(total)

#

numbers = [10, 20, 30]
numbers[0] = 15
print(numbers)

#

text = "автоматизация"
print(text[-1])

#

has_key = True
is_door_open = False
can_enter = has_key or is_door_open
print(can_enter)



