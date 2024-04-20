# print("Hello world"


# try :
#     # code to try to evaluate
# except :
#     #code to execute if there is an error
# else :
#       Execute if no errors
# finally :
#       Always execute this error

# try :
#     num1 = float(input("Enter the first number "))
#     num2 = float(input("Enter the second number "))

#     result = num1 / num2 

#     print("Result is " , result)
# except ZeroDivisionError : 
#     print("Error : Cannot divide by zero")
# except ValueError :
#     print("Invalid input . Please enter a number")


try:
    number = int(input("Enter a whole number "))
    inverse = 1 / number

except ValueError : 
    print("That's not a whole number")
except ZeroDivisionError :
    print("Infinity! Cannot divide by zero")
else :
    print("The inverse is " , inverse)
finally :
    print("Attempt to calculate inverse completed")