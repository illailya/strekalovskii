#Условные операторы
#Задача 1
#Напиши код, который проверяет, является ли число x положительным
x = 5

if x > 0:
  print("положительный")


#Задача 2
#Напиши код, который проверяет, делится ли число y на 2 без остатка
#Если делится — выведи "Число четное", иначе — "Число нечетное".

y = 19

if y % 2 ==0:
    print("Четное")
else:
    print("Нечетное")



#Задача 4


score = 102

if score < 50:
    print("Неудовлетворительно")
elif 50 <= score <= 69:
    print("Удовлетворительно")
elif 70 <= score <= 89:
    print("Хорошо")
elif 90 <= score <= 100:
    print("Отлично")
else:
  print("Некорректный ввод")


#Задача 5

age = 18
if age >= 18:
    status = "Взрослый"
else:
    status = "Ребенок"

age = 18
result = "Взрослый" if age >= 18 else "Ребенок"
print(result)


#Задача 6
#Число num чётное И в диапазоне от 10 до 20 включительно
#Если условие выполняется, выведи "Подходит", иначе — "Не подходит"

num = 16
if num %2==0 and 10 <= num <=20:
    print("Подходит")
else:
    print("Не подходит")


#Задача 7

color = "зеленый"

if color == "зеленый":
    print("Нейтральный")
elif color == "синий" or color == "голубой":
    print("Холодный цвет")
elif color == "красный" or color == "желтый":
    print("Горячий цвет")
else:
    print("Неизвестный цвет")



#Задача 8

data = 6  # может быть строкой, числом или другим типом

if type(data) == str and "а" in data:
    print("Текст")
elif type(data) == int and data % 2==0:
    print("Число")
else:
    print("Другое")



#Задача 9

x = 0

if x > 0 and x %2==0:
    print("А")
elif x > 0 and x %2!=0:
    print("Б")
elif x < 0:
    print("В")
elif x ==0:
    print("Г")


# Задача 10

age = 15
if age >= 18:
    if age <= 65:
        status = "Рабочий возраст"
    else:
        status = "Пенсионный возраст"
else:
    status = "Детский возраст"
#Перепиши код ниже в одну строку, используя тернарный оператор:

age = 15
result = "Рабочий возраст" if 18 <= age <= 65 else ("Пенсионный возраст" if age > 65 else "Детский возраст")
print(result)


#Задача 11

temp = 25
if temp >= 30:
    category = "Жарко"
elif temp >= 20:
    category = "Тепло"
elif temp >= 10:
    category = "Прохладно"
else:
    category = "Холодно"

temp = 20
result = "Жарко" if temp >= 30 else ("Тепло" if temp >= 20 else "Прохладно" if temp >= 10 else "Холодно")
print(result)

# Задача 12

time = 14  # часы от 0 до 23

if time < 6:
    part_of_day = "Ночь"
elif time < 12:
    part_of_day = "Утро"
elif time < 18:
    part_of_day = "День"
else:
    part_of_day = "Вечер"

time = 17
result = "Ночь" if time < 6 else ("Утро" if time < 12 else "День" if time < 18 else "Вечер")
print(result)

#задача 13

x = 11

if x %2==0:
    print("Четное")
else:
    print("Нечетное")


#задача 14

temperature = 25

if temperature > 30:
    print("Жарко")
elif 20 <= temperature <= 30:
    print("Тепло")
elif temperature < 20:
    print("Прохладно")



#Задача 15

password = "qwert"

result = "Надёжный" if len(password) >= 8 else "Слишком короткий"
print(result)
