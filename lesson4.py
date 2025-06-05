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

#Задача 16

x = 2
if x > 0 and x % 2 == 0:
    print(True)
else:
    print(False)


#Задача 17

age = 19
if age >= 18:
    status = "Взрослый"
else:
    status = "Ребёнок"
print(status)

ter = "Взрослый" if age >= 18 else  "Ребёнок"
print(ter)

#Задача 18

n = 5
if n < 0:
    print("Отрицательное")
elif n == 0:
    print("Ноль")
elif n > 0 and n < 10:
    print("Положительное однозначное")
else:
    print("Положительное многозначное")


#Задача 19

temperature = 15

if temperature > 20:
    print("Тепло")
else:
    print("Холодно")


x = 4
print(x > 0 and x%2==0)

#

hour = 2
if hour < 6:
    print("Ночь")
elif 6 <= hour < 12:
    print("Утро")
elif 12 <= hour < 18:
    print("День")
else:
    print("Вечер")


#

a = True
b = False
c = True
print(a == True and c == True or b == True and c == False)

#

num = 9
if num %3==0:
    print("Кратно 3")
else:
    print("Не кратно 3")

#

is_weekend = True
is_holiday = False
print((is_weekend and not is_holiday) or (is_holiday and not is_weekend))

#

t = -5
result = "Холодно" if t < 0 else "Тепло"
print(result)

#

score = 85
if score >= 90:
    print("5")
elif 80 <= score <90:
    print("4")
elif 70 <= score < 80:
    print("3")
elif score < 70:
    print("2")

#

x = 10
y = 20
z = 15
if x < y and y > z and z != x:
    print("Да")
else:
    print("Нет")

#

has_ticket = True
has_passport = True
result = "Можно лететь" if has_ticket and has_passport else "Нельзя лететь"
print(result)

#

time = 15  # текущий час (0-23)
is_weekend = True
if 10 <= time <=18 and is_weekend == False:
    print("Можно")
elif 10 <= time <= 18 and is_weekend == True:
    print("Нельзя")
elif 19 <= time <= 23:
    print("Можно")
elif 0 <= time <= 5 or 6 <= time <= 9:
    print("Нельзя")

#

is_raining = True
is_windy = False
print("Беру зонт" if is_raining and not is_windy else "Остаюсь дома")