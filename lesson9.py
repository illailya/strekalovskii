#ООП ч.1

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
