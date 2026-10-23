'''N-1'''
# class Vehicle:
#     def move(self):
#         return 'Транспорт движется'
# class Car(Vehicle):
#     def honk(self):
#         return 'Би-би!'
# c=Car()
# print(c.move())
# print(c.honk())


'''N-2'''
# class Employee:
#     def work(self):
#         return "Сотрудник работает"
# class Programmer:
#     def work(self):
#         return "Пишет код"
# class Teacher:
#     def work(self):
#         return "Проводит урок"
# workers=[Employee(), Programmer(), Teacher()]
# for a in workers:
#     print(a.work())


'''N-3'''
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course=course
#     def info(self):
#         return f'{self.name}, {self.age} лет, группа {self.course}'
# s=Student('Noza', 20, 'Python-1')
# print(s.info())


'''N-4'''
# class Animal:
#     def speak(self):
#         return "Животное издаёт звук"
# class Cat(Animal):
#     def speak(self):
#         print(super().speak())
#         print('Мяу')
# a=Cat()
# a.speak()


'''N-5'''
# class Device:
#     def power_on(self):
#         return "Устройство включено"
# class Phone(Device):
#     def call(self,number):
#         return f"Звоню на номер {number}"
# class Smartphone(Phone):
#     def take_photo(self):
#         return "Фото сделано"
# s=Smartphone()
# print(s.power_on())
# print(s.call('+992 886 002 122'))
# print(s.take_photo())


'''N-6'''
# class Flyer:
#     def fly(self):
#         return 'Bird can fly'
# class Swimmer:
#     def swim(self):
#         return 'Fish can swim'
# class Duck(Flyer, Swimmer):
#     def quack(self):
#         return 'Duck can do both'
# d=Duck()
# print(d.fly())
# print(d.swim())
# print(d.quack())
# print(Duck.__mro__)


'''N-7'''
# class User:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email
#     def get_info(self):
#         return f'Name: {self.name}, Email: {self.email}'
# class Admin(User):
#     def __init__(self, name, email, level):
#         super().__init__(name, email)
#         self.level=level
#     def get_info(self):
#         return f'Name: {self.name}, Email: {self.email}, Level: {self.level}'

# class Customer(Admin):
#     def __init__(self, name, email, level, balance):
#         super().__init__(name, email, level)
#         self.balance=balance
#     def get_info(self):
#         return f'Name: {self.name}, Email: {self.email}, Level: {self.level}, Balance: {self.balance}'
# class Guest(Customer):
#     def get_info(self):
#         return super().get_info()

# print(Admin("Ali", "ali@mail.tj", 5).get_info())



'''N-8'''
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self, pi=3.14):
#         return pi * (self.radius ** 2)
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height
# shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
# for s in shapes:
#     print(type(s).__name__, s.area())



'''N-9'''
# Part-A
# class Calculator:
#     def multiply(self,a,b=1,c=1):
#         print(a*b*c)
# calc=Calculator()
# calc.multiply(5)        
# calc.multiply(5, 2)     
# calc.multiply(5, 2, 3)  


# Part-B
# from enum import Enum
# class OrderStatus(Enum):
#     NEW = 1
#     PAID = 2
#     SHIPPED = 3
#     DELIVERED = 4
# def next_status(status):
#     if status == OrderStatus.DELIVERED:
#         return status
#     return OrderStatus(status.value + 1)

# current = OrderStatus.NEW
# result = next_status(current)
# print(f"Name: {result.name}")
# print(f"Value: {result.value}")



'''N-10'''
# from enum import Enum
# class PaymentStatus(Enum):
#     SUCCESS=1
#     FAILED=2
# class Payment:
#     def __init__(self, owner):
#         self.owner = owner
#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
#         print("Unknown payment method")
#         return PaymentStatus.FAILED

# class CardPayment(Payment):
#     def __init__(self, owner, card_number):
#         super().__init__(owner)
#         self.card_number = card_number

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
#         last_four = str(self.card_number)[-4:]
#         print(f"Processing card payment of {amount} for {self.owner} using card ending in {last_four}")
#         return PaymentStatus.SUCCESS

# class CashPayment(Payment):
#     def __init__(self, owner):
#         super().__init__(owner)

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
#         print(f"Processing cash payment of {amount} for {self.owner}")
#         return PaymentStatus.SUCCESS
    
# class WalletPayment(Payment):
#     def __init__(self, owner, balance):
#         super().__init__(owner)
#         self.balance = balance

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
#         if amount > self.balance:
#             print(f"Wallet payment failed for {self.owner}: Insufficient balance ({self.balance})")
#             return PaymentStatus.FAILED
        
#         self.balance -= amount
#         print(f"Wallet payment successful for {self.owner}. Remaining balance: {self.balance}")
#         return PaymentStatus.SUCCESS

# payment_methods = [
#     CardPayment("Alice", "4532123456789012"),
#     CashPayment("Bob"),
#     WalletPayment("Charlie", balance=100.0),
#     WalletPayment("Diana", balance=10.0),  
#     Payment("Eve") ]                    


# amount_to_pay = 50.0
# for payment in payment_methods:
#     print(f"--- Attempting payment for {payment.owner} ---")
#     status = payment.pay(amount_to_pay)
#     print(f"Result Status: {status.name}\n")