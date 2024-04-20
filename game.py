import random


# the secret number is chosen randomly from  1 to 10
secret_number = random.randint(1,10)


print("Secret number is this ",secret_number)
attempts = 3

while attempts > 0 :
    guess = int(input("Guess the number between 1 and 10"))
    if guess == secret_number :
        print("You guessed it right ! Congralutations")
        break
    attempts -= 1
    print("Wrong guess You have " , attempts ,"left")
else:
    print("Sorry the secret number was " , secret_number,"better luck next time")


# hw add an elif condition to give player a hint if their guess is too high or too low
# try to implement for loop with range() instead of while loop


# for attempt in range(0,3,1) :




