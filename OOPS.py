from abc import ABC , abstractmethod


class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self,title,author,a,b):
        self.title = title
        self.author = author
        self.a = a
        self.b = b
    
    def display_info(self):
        return f"Book : {self.title} by {self.author}"
    def add(self , c):
        print(self.a + self.b  + c)
    def add(self , c , d):
        print(self.a + self.b  + c + d)
    
class DVD(LibraryItem):
    def __init__(self,title,director):
        self.title = title
        self.director = director
    def display_info(self):
        return f"DVD : {self.title} directed by {self.director}"


my_book = Book("1984" , "george orwell" ,5,5)

my_dvd = DVD("Inception" , "Christopher Nolan")

for item in [my_book, my_dvd] : 
    print(item.display_info())




my_book.add(5 , 6)









# # # # # # class Dog :
# # # # # #     # __init__ method known as constructor is automatically called invoked when you create a new object
# # # # # #     def __init__ (self , name ,age) :
# # # # # #         self.name = name
# # # # # #         self.age = age

# # # # # # my_dog = Dog("Buddy" , 5)
# # # # # # my_dog = Dog("Dog2" , 7)
# # # # # # my_dog = Dog("Dog3" , 9)


# # # # # # class Car:
# # # # # #     def __init__ (self,make,model) :
# # # # # #         self.make = make
# # # # # #         self.model = model

# # # # # # my_car = Car("Toyota" , "Corolla")

# # # # # # print(f"I drive a {my_car.make} {my_car.model}")


# # # # # # class Person:
    
# # # # # #     def __init__(self , name , age):
# # # # # #         self._name = name # instance attribute
# # # # # #         self.age = age # instance attribute

# # # # # #     def greet(self):
# # # # # #         return f"Hello , my name is {self._name} and I am {self.age} years old"
    

# # # # # # person = Person("Alice" , 30)

# # # # # # print(person.greet())
# # # # # # print(person._name)



# # # # # class BankAccount :
# # # # #     def __init__(self , account_number , balance = 0):
# # # # #         # private atrributes
# # # # #         self.__account_number = account_number # instance attribute
# # # # #         self.__balance = balance # instance attribute

# # # # #     def deposit(self, amount):
# # # # #         if amount > 0:
# # # # #             self.__balance += amount
# # # # #             print(f"Deposited {amount} , New Balance: {self.__balance}")
    
# # # # #     def withdraw(self , amount) :
# # # # #         if 0 < amount <= self.__balance :
# # # # #             self.__balance -= amount
# # # # #             print(f"Withdrawn : {amount} , Remaining balance : {self.__balance}")

# # # # #     def get_balance(self):
# # # # #         return self.__balance
# # # # #     def set_balance(self, amount):
# # # # #         self.__balance = amount


# # # # # my_account = BankAccount("12345678" , 1000)

# # # # # my_account.deposit(500)
# # # # # my_account.withdraw(200)
# # # # # print(f"Account balance :  {my_account.get_balance()}")
# # # # # my_account.set_balance(2000)
# # # # # print(f"Account balance :  {my_account.get_balance()}")



# # # # class Shape(ABC):
# # # #     @abstractmethod
# # # #     def area(self):
# # # #         pass


# # # # class Circle(Shape) :
# # # #     def __init__(self , radius) :
# # # #         self.radius = radius
    
# # # #     def area(self):
# # # #         return 3.14 * self.radius ** 2
    
# # # # class Rectangle(Shape) :
# # # #     def __init__(self , length , width) :
# # # #         self.length = length
# # # #         self.width = width

# # # #     def area(self):
# # # #         return self.length * self.width

# # # # circle = Circle(5)
# # # # rectangle = Rectangle(10,5)

# # # # print(f"Circle  area : {circle.area()}")
# # # # print(f"Rectange  area : {rectangle.area()}")



# # # # single inheritance

# # # class Animal :
# # #     def speak(self):
# # #         pass


# # # class Dog(Animal):
# # #     def speak(self):
# # #         return "Bark!"
    
# # # dog = Dog()
# # # print(dog.speak())

# # # # mutiple inheritance

# # # class Father :
# # #     def hair(self):
# # #         return "Brown hair"
    
# # # class Mother :
# # #     def eyes(self):
# # #         return "Blue eyes"
    
# # # class Child(Father , Mother):
# # #     pass

# # # child = Child()

# # # print(child.hair() , " and " , child.eyes())


# # # # mutlilevel inheritance

# # # class GrandFather : 
# # #     def surname(self) :
# # #         return "Smith"

# # # class Father(GrandFather):
# # #     def firstName(self):
# # #         return "John"

# # # class Son(Father):
# # #     def age(self):
# # #         return 25
    
# # # son = Son()

# # # print(f"{son.firstName()} {son.surname()} Age : {son.age()}")


# # class Animal:
# #     def speak(self):
# #         return "Some sound"


# # class Dog(Animal):
# #     def speak(self):
# #         return "Woof!"
    
# # class Cat(Animal):
# #     pass

# # my_dog =  Dog()
# # my_cat = Cat()

# # for animal in [my_dog, my_cat]:
# #     print(type(animal).__name__ ," says" , animal.speak())


# class Book:
#     def __init__(self , title , author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
#     def __repr__(self):
#         return f"Book {self.title} by {self.author}"
    
# my_book = Book("1984" , "George Orwell")

# print(my_book) # calls __str__ 

# print(repr(my_book)) # calls __repr__