# class Computer :
#     def __init__(self) -> None:
#         self.__maxprice = 900 # private attribute
    
#     def sell(self):
#         print(f"Selling price : {self.__maxprice}")
    
#     # setter method
#     def setMaxPrice(self , price):
#         self.__maxprice = price
    


# # create an object
# c = Computer()

# c.sell()

# # try to change the price directly via attribute
# c.__maxprice = 1000
# c.sell()

# # change the price through setter method
# c.setMaxPrice(1000)
# c.sell()

# example 2 - Using encapsulation for data hiding

class Account:
    def __init__(self , owner , balance = 0) -> None:
        self.owner = owner
        self.__balance = balance # private attribute
    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit was successfull")
    
    def withdraw(self , amount):
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
            print("Withdraw succesful")
        else :
            print("Insufficient funds")
    
    # getter method
    def getBalance(self):
        return self.__balance


acc = Account("John")
acc.deposit(500)
print(acc.getBalance())

acc.withdraw(200)
print(acc.getBalance())
