# Class: A blueprint defining what an object contains and can do.
# Object: An individual instance created using that blueprint.
# Constructor (__init__),Syntax = def __init__(self):,it is automatically called/invoked when the object of the class is created.e.g.,Suppose we want to store every student's name and age.We need a way to initialize those values when an object is created.

class Student:

    college = "CJM" # Class or local variable
    def __init__(self,name,age): #constructor/initializer method
        self.name = name # Creates or assigns an instance attribute called name.
        self.age = age # Creates or assigns an instance attribute called age.
# self refers to the current instance of the class

s1 = Student("Rahul",26)
s2 = Student("Trisha",22)

print(s1) # output = <__main__.Student object at 0x000001C17D1C8EC0>
print(s2) # output = <__main__.Student object at 0x000001C17D1A8CD0>

print(s1.name) # Rahul
print(s2.name) #Trisha
print(s1.age) #26
print(s2.age) #22

#-----------------------------------------------------------------

class Employee:

    company = "TCS" # Class variable

    def __init__(self,name,salary):
        self.name = name # Instance variable
        self.salary = salary

    def display(self):
        print(self.name,self.salary)

e1 = Employee("Rahul",10000)
e2 = Employee("Mousumi",20000)
e1.display()
e2.display()
print(e1.company)
print(e2.company)

#---------------------------------------------------------

#Python has 3 methods - instance , class , static

class Employees:

    company = "TCS"

    # Constructor
    def __init__(self,name):
        self.name = name 

    #Instance methods,Purpose = Work with a particular object's data,first parameter is self
    def display(self):
        print(f"Employee is : {self.name}")

    @classmethod #Work with class-level information,first parameter is cls
    def show_comapny(cls):
        print(f"Company is : {cls.company}")

    @staticmethod #Related utility functionality,first parameter is none automatically
    def calculate_bonus(salary):
        return salary * 0.10

emp = Employees("Rahul")
emp.display()
Employees.show_comapny()
bonus = Employees.calculate_bonus(10000)
print(bonus)

#-----------------------------------------------------

class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount 

    def show_balance(self): # self refers to the account's object
        print(f"Account holder : {self.account_holder}")
        print(f"Balance : {self.balance}")

account = BankAccount("Rahul",1000)
account.deposit(500)
account.show_balance()

# ----------------------------------------------------------------

# Encapsulation means keeping data and the methods that operate on it together inside a class, while controlling how that data is accessed or modified.Achieved using __variableName.

class Account:

    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid withdrawal amount")


    def display(self):
        print(f"Account holder : {self.name}")
        print(f"Balance : {self.__balance}")

acc = Account("Rahul",1000)
acc.deposit(600)
acc.display()
#print(acc.__balance) # throws error because it's private and can be accessed inside the class only

#-----------------------------------------------------

# Inheritance means one class can reuse and extend the attributes and methods of another class.Types = Single,Multi level,Multiple

class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal): # Single inheritance

    def bark(self):
        print(f"{self.name} is barking")

dog = Dog("Tommy")
dog.eat()
dog.bark()        


# Inheritance allows a child class to provide its own version of a method already defined in the parent class.(Method overriding).Same method name but different implementation


class Animals:

    def sound(self):
        print("Animal makes a sound")


class Dogs(Animals):

    def sound(self):
        print("Dog barks")


animal = Animals()
dog = Dogs()

animal.sound()
dog.sound()

#------------------------------------------------------
# super() — Calling parent-class methods and initializers.
class Banking:

    def __init__(self,holder,balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0 :
            print("Amount should be >= 0 ")
        else:
            self.__balance += amount

    def get_balance(self): # getters in python for accessing private elements
        return self.__balance

class SavingsAccount(Banking):

    def __init__(self, holder, balance,interest_rate):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.get_balance() * self.interest_rate) / 100 #option 2 is using _balance.
        self.deposit(interest)

account = SavingsAccount("Rahul", 1000, 5)

account.deposit(500)
account.add_interest()

print(account.get_balance())

#--------------------------------------------------

# Polymorphism = many forms(Method overriding)


class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

#-----------------------------------------------------

class Payment:

    def pay():
        print("Processing payment")

class UPIPayment(Payment):

    def pay(self):
        print("Payment completed using UPI")

class CardPayment(Payment):

    def pay(self):
        print("Payment completed using Card")

def process_payment(payment):
    payment.pay()

upi = UPIPayment()
card = CardPayment()

process_payment(upi)
process_payment(card)

#-----------------------------------------------------------------

# Abstraction means showing only the essential functionality while hiding unnecessary implementation details.

# Python provides the abc module. abc stands for Abstract Base Classes.

#@abstractmethod


from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):

    def pay(self):
        print("Payment completed using UPI")


class CardPayment(Payment):

    def pay(self):
        print("Payment completed using Card")


upi = UPIPayment()
card = CardPayment()

upi.pay()
card.pay()

#--------------------------------------------------------------

class Notification:

    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):

    def send(self,message):
        print(f"Email sent : {message}")

class SMSNotification(Notification):

    def send(self,message):
        print(f"SMS sent : {message}")

def send_notification(notification, message):
    notification.send(message)

email = EmailNotification()
sms = SMSNotification()

send_notification(email, "Hello Rahul")
send_notification(sms, "Hello Rahul")

# when we don't declare methods inside a class we don't need to use self otherwise self is mandatory




        


        
