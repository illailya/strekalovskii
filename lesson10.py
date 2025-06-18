#ООП2


class Animal:
    def speak(self):
        print(f"Это животное издает звук")

class Dog(Animal):
    def speak(self):
        print(f"Гав-гав!")

d = Dog()
d.speak()

#

class Vehicle:
    def drive(self):
        print(f"Транспортное средство движется")

class Bicycle(Vehicle):
    def drive(self):
        print(f"Велосипед едет на двух колесах")

bic = Bicycle()
bic.drive()

#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, ID: {self.student_id} ")

p = Person("Илья", 33)
p.info()
s = Student("Илья", 33, "88")
s.info()

#

class Engine:
    def start(self):
        print(f"Двигатель запущен")
class MusicPlayer:
    def play_music(self):
        print(f"Играет музыка")

class Car(Engine, MusicPlayer):
    def drive(self):
        print(f"Машина едет")

    def start(self):
        super().start()
        print(f"Все системы готовы")

my_car = Car()
my_car.start()

#

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")

class D(B, C):
     def show(self):
      super().show()
      print("D")
d = D()
d.show()

#

class Animal:
    def sound(self):
        print("Звук животного")
class Cat(Animal):
    def sound(self):
        print("Мяу!")
    def purr(self):
        print("Муррр...")
cat = Cat()
cat.sound()
cat.purr()

#

class Vehicle:
    def start(self):
        print("Двигатель запущен")
class Car(Vehicle):
    def start(self):
        print("Проверка топлива")
        super().start()
car = Car()
car.start()

#

class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name} работает")
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    def work(self):
        print(f"{self.name} управляет отделом {self.department}")
m = Manager("Анна", "маркетинг")
m.work()

#

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "Гав!"
    def fetch(self):
        return f"{self.name} принёс мяч!"
a = Animal("шарик")
d = Dog("Бобик")
print(a.speak())
print(d.speak())
print(d.fetch())

#

class Animal:
    def eat(self):
        print("Ест")
class Dog(Animal):
    pass

#

class Vehicle:
    def move(self):
        print("Двигается")
class Car(Vehicle):
    def move(self):
     super().move()
     print("На дороге")
c = Car()
c.move()

#

class Bird:
    def fly(self):
        print("Летит")
class Penguin(Bird):
    def fly(self):
        print("Не умеет летать")

#

class Person:
    pass
class Employee(Person):
    def __init__(self, salary):
        self.salary = salary
class Manager(Person):
    def __init__(self, salary,  team_size):
        super().__init__(salary)
        self.team_size = team_size

#

class Shape:
    def draw(self):
        print("Рисует фигуру")
class Circle(Shape):
    def draw(self):
        super().draw()
        print("Окружность")
c = Circle()
c.draw()

#

class Camera:
    def take_photo(self):
        print("Делает фото")
class Phone:
    def call(self):
        print("Звонит")
class Smartphone(Camera, Phone):
    pass
s = Smartphone()

#

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
    def deposit(self, amount):
            self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Недостаточно средств")
    def get_balance(self):
        return self.__balance
b = BankAccount()
print(b.get_balance())

#

class Computer:
    def turn_on(self):
        print("Компьютер включён")
class GamingComputer(Computer):
    def turn_on(self):
        super().turn_on()
        print("Игровой режим активирован")
g = GamingComputer()
g.turn_on()

#

class Bird:
    wings = 2
    def __init__(self, name):
        self.name = name
class Penguin(Bird):
    wings = 0