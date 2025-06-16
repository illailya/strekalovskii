#ООП ч.1
from itertools import count


class Book:
    COVER_COLOR = "red"
my_book = Book()
print(my_book.COVER_COLOR)

#

class Lamp:
    def __init__(self, color):
        self.color = color

    def info(self):
        print(f"Цвет {self.color}")

lamp_blue = Lamp(color="blue")

lamp_blue.info()

#

class Robot:
    def __init__(self, text):
        self.text = text

    def greet(self):
        print(self.text)

r2d2 = Robot(text="Я робот!")
r2d2.greet()

#

class SpaceShip:
    fuel_type = "антиматерия"  # Общий атрибут класса (не в __init__!)

    def show_fuel(self):
        return self.fuel_type  # Обращаемся к атрибуту через self

# Проверка
ship1 = SpaceShip()
print(ship1.show_fuel())  # Выведет: антиматерия

#

class Droid:
    def say_hello(self):  # Только self как параметр
        return "BEEP-BOOP"  # Фиксированная строка

r4 = Droid()
print(r4.say_hello())  # Выведет: BEEP-BOOP

#

class Cat:
    def __init__(self, name):  # Конструктор с параметром name
        self.name = name  # Сохраняем имя в атрибуте объекта

    def meow(self):  # Метод с self
        return f"{self.name}: Мяу!"  # Используем атрибут name


# Создаем два объекта
cat1 = Cat("Барсик")
cat2 = Cat("Мурзик")

# Выводим результаты
print(cat1.meow())  # Барсик: Мяу!
print(cat2.meow())  # Мурзик: Мяу!

#
#1
class BankAccount:
    bank_name = "Тинькофф"

my_banc = BankAccount
print(my_banc.bank_name)
#2

class Client:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def info(self):
        return (f"У клиента: {self.owner} на счету: {self.balance}")

client1 = Client("Алексей", "34523")
client2 = Client("Сергей", "43763467324")

print(client2.info())

# Решение
class BankAccount:
    bank_name = "Тинькофф"  # Общий атрибут

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Увеличиваем баланс

    def show_info(self):
        return f"{self.owner} в {self.bank_name}: {self.balance} руб."


# Проверка
acc = BankAccount("Иван", 1000)
acc.deposit(500)
print(acc.show_info())  # Иван в Тинькофф: 1500 руб.

#

class Book:
    pass

my_book = Book()

#

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title_with_author(self):
        return (f"Название: {self.title}, Автор: {self.author}")

my_book = Book("Война и мир", "Лев Толстой")
print(my_book.get_title_with_author())


#

class Book:
    library_name = "Главная библиотека"

    def __init__(self, name, author):
        self.name = name
        self.author = author
    def result(self):
        return (self.name, self.author)

book1 = Book("Мастер и Маргарита", "Булгаков")
book2 = Book("Евгений Онегин", "Пушкин")
print(book1.library_name)
print(book2.library_name)
print(book1.result())

#

class Student:
    school_name = "IT-Академия"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def have_birthday(self):
        self.age += 1

    def introduce(self):
        return (f"Меня зовут {self.name}, мне {self.age} лет, я учусь в {self.school_name}")

result1 = Student("Илья", 33)
print(result1.introduce())
result1.have_birthday()
result1.have_birthday()
print(result1.introduce())

#

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Снято {amount} рублей. Новый баланс: {self.balance}")
        else:
            print("Ошибка: недостаточно средств на счете")

    def check_balance(self):
        return (f"У {self.owner} на счету {self.balance} рублей")
acc = BankAccount("Иван", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.check_balance())

#

class Book:
    library = "Центральная библиотека"

    def __init__(self ,title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return (f"Название: {self.title}, Автор: {self.author}")

    def change_library(self, new_name):
        Book.library = new_name
book1 = Book("1984", "Оруэлл")
book2 = Book("Мастер и Маргарита", "Булгаков")
book1.change_library("Главная библиотека")
print(book2.library)
print(book2.get_info())

#

class Wallet:
    def __init__(self, balance = 0):
        self.balance = balance

    def add_money(self, amount):
        if self.balance >= amount:
            self.balance += amount
        print(f"Баланс пополнен на {amount} рублей. Текущий баланс {self.balance} рублей")
    def spend_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Снято {amount} рублей. Новый баланс: {self.balance}")
        else:
            print(f"Ошибка, недостаточно средств")
    def check_balance(self):
        return (f"Текущий баланс {self.balance} рублей")
my_wallet = Wallet(100)
my_wallet.add_money(50)
my_wallet.spend_money(30)
print(my_wallet.check_balance())

#

class TV:
    DEFAULT_BRAND = "Samsung"
    def __init__(self, channel = 1, brand = DEFAULT_BRAND):
        self.channel = channel
        self.brand = brand
    def change_channel(self, new_channel):
        self.channel = new_channel
    def info(self):
        return f"Телевизор {self.brand} на канале {self.channel}"
tv = TV(5, "LG")
tv.change_channel(7)
print(tv.info())

tv2 = TV()
print(tv2.info())

#

class CoffeeMachine:
    def __init__(self, water_level = 0, coffee_level = 0):
        self.water_level =water_level
        self.coffee_level = coffee_level
    def add_water(self, amount):
        self.water_level += amount
    def add_coffee(self, amount):
        self.coffee_level += amount
    def make_coffee(self):
        if self.water_level >= 100 and self.coffee_level >= 20:
            print(f"Ингредиентов для приготовления кофе достаточно")
        else:
            print(f"Недостаточно ингредиентов")
    def status(self):
        return f"Вода: {self.water_level} мл, Кофе: {self.coffee_level} г"

machine = CoffeeMachine()
machine.add_water(200)
machine.add_coffee(30)
print(machine.make_coffee())
print(machine.status())

#

class SmartBulb:
    def __init__(self, brightness = 50, color = "#FFFFFF", is_on = False):
        self.brightness = brightness
        self.color = color
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_brightness(self, value):
      if 0 <= value <= 100:
        self.brightness = value
      else:
       print(f"Ошибка: {value}% вне диапазона 0-100")
    def set_color(self, new_color):
        self.color = new_color
    def status(self):
        state = "вкл" if  self.is_on else "выкл"
        return f"Состояние: {state}, Яркость: {self.brightness}%, Цвет: {self.color}"
bulb = SmartBulb()
print(bulb.status())
bulb.turn_on()
bulb.set_color("#FFA500")  # Оранжевый
bulb.set_brightness(150)  # Не изменится (>100)

print(bulb.status())


#

class MusicPlayer:
    def __init__(self, volume = 50, is_playing = False, current_track = ""):
        self.volume = volume
        self.is_playing = is_playing
        self.current_track = current_track
        self.track_number = 0
    def play(self):
        self.is_playing = True
        return f"Воспроизводится {self.current_track}"
    def pause(self):
        self.is_playing = False
        return self
    def next_track(self):
        self.track_number = self.track_number %3 + 1
        self.current_track = f"Трек {self.track_number}"
        return self
    def set_volume(self, value):
        if 0 <= value <= 100:
            self.volume = value
        else:
            print(f"Заданное значение не соответствует диапазоне 0-100")
    def status(self):
        result = "играет" if self.is_playing else "пауза"
        return f"Трек: {self.current_track}, Громкость: {self.volume}%, Состояние: {result}"

player = MusicPlayer()
print(player.play())  # Воспроизводится
player.next_track()
print(player.status())  # Трек: Трек 1, Громкость: 50%, Состояние: играет

player.next_track().set_volume(80)  # Цепочка вызовов
print(player.status())

#

class BankCard:
    def __init__(self, cardholder = None, balance = 0, is_blocked = False):
        self.cardholder = cardholder
        self.balance = balance
        self.is_blocked = is_blocked
    def deposit(self, amount):
        self.balance += amount
        return f"Баланс пополнен на {amount} рублей"
    def spend(self, amount):
        if self.balance > 0 and self.is_blocked == True:
           self.balance -= amount
           return f"Списано {amount} рублей"
    def block(self):
        self.is_blocked = True
        return f"Карта заблокирована"
    def status(self):
        cart = "заблокирована" if self.is_blocked else "активна"
        return f"Владелец: {self.cardholder}, Баланс: {self.balance}р., Статус: {cart}"
bank = BankCard()
print(bank.deposit(500))
print(bank.status())
print(bank.block())

#

class Thermometer:
    def __init__(self, current_temp = 36.6, unit = "C"):
        self.current_temp = current_temp
        self.unit = unit

    def update_temp(self, new_temp):
        self.current_temp = new_temp
        return self

    def change_unit(self):
        if self.unit == "C":
            self.current_temp = self.current_temp * 9/5 + 32
            self.unit = "F"
        elif self.unit == "F":
            self.current_temp = (self.current_temp - 32) * 5/9
            self.unit = "C"
        else:
            print(f"Значение некорректно")

    def status(self):
        return f"Температура: {self.current_temp}°{self.unit}"
therm = Thermometer()
print(therm.change_unit())
print(therm.change_unit())

print(therm.status())

#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print({self.name}, {self.age})
person = Person("Анна", 25)
print(person.name)
print(person.age)

#

class Car:
    def start_engine(self, text = "Двигатель запущен"):
        return text
car = Car()
result1 = car.start_engine()
print(result1)
#правильное решение
class Car:
    def start_engine(self):
        print("Двигатель запущен")
car = Car()
car.start_engine()


#

class SpaceShip:
    fuel_type = "гиперплазма"
    def show_fuel(self):
        print(self.fuel_type)
ship1 = SpaceShip()
ship1.show_fuel()

#

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Книга {self.title}, автор {self.author}")
book1 = Book("1984", "Оруэлл")

#

class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    def drive(self):
        print(f"Велосипед едет на скорости {self.max_speed} км/ч на передаче {self.gear_count}")
    def __str__(self):
        return f"Велосипед с {self.gear_count} передачами"
class Bicycle(Vehicle):
    def __init__(self, max_speed, gear_count):
        self.max_speed =max_speed
        self.gear_count = gear_count
    def ring_bell(self):
        print(f"Дзинь-дзинь!")
bike = Bicycle(30, 7)
bike.drive()
bike.ring_bell()
print(bike)

#

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, new_temp):
        self.__celsius = new_temp

t = Temperature(25)
print(t.get_celsius())  # Должно вывести 25
t.set_celsius(30)
print(t.get_celsius())

#

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} говорит: Мяу!")
cat = Cat("Мурзик")
cat.meow()

#

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def show(self):
        print(self.count)

c = Counter()  # создаём объект
c.increment()  # увеличиваем счётчик
c.increment()  # увеличиваем счётчик
c.increment()  # увеличиваем счётчик
c.show()

#

class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print(self.items)

basket = Basket()
print(basket.items)
basket.add("Второй")
print(basket.items)

#

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)
s = Student("Анна")
s.add_grade(1)
print(s.get_average())

#

class Book:
    def __init__(self, title = "Неизвестно"):
        self.title = title
b = Book()
print(b.title)
b = Book("Гарри Поттер")
print(b.title)

#

class Book:
    def __init__(self, title = "Неизвестно"):
        self.title = title

    def info(self):
        print(f"Книга: {self.title}")
b = Book()
print(b.title)
b = Book("Гарри Поттер")
print(b.title)
b.info()
b = Book("Война и мир")
b.info()

#

class Student:
    def __init__(self, name, year = 1):
        self.name = name
        self.year = year
s1 = Student("Иван")
print(s1.year)
s2 = Student("Мария", 3)
print(s2.year)

#

class Counter:
    def __init__(self, count = 0):
        self.count = count
    def increment(self, ):
        self.count += 1
    def show(self):
        return self.count
c = Counter()
c.increment()
c.increment()
c.increment()
print(c.show())

#

class SpaceShip:
    fuel_type = "гиперион"
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"Корабль {self.name}, тип топлива: {self.fuel_type}")
ship1 = SpaceShip("Авангард")
ship2 = SpaceShip("Пионер")
ship1.show_info()
ship2.show_info()
SpaceShip.fuel_type = "криптон"
ship2.show_info()

#

class Robot:
    def __init__(self, name, battery = 100):
        self.name = name
        self.battery = battery
    def charge(self):
        self.battery = 100
    def greet(self):
        if self.battery >= 10:
            self.battery -= 10
            print(f"Привет, я {self.name}!")
        elif self.battery < 10:
            print("Требуется зарядка!")
r = Robot("R2-D2")
r.greet()
r.greet()
print(r.battery)
r.charge()
print(r.battery)

#

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
    def show_balance(self):
        print(f"Баланс {self.owner}: {self.balance} руб.")
b = BankAccount("Илья", 1000)
b.show_balance()
b.deposit(500)
b.show_balance()
b.withdraw(700)
b.show_balance()

#

class Temperature:
