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
