from random import random, randint
print("")
print("")
print("-------------------------------------------------------------------------------------------")
print("---------------------------Welcome to The Guessing Game------------------------------------")
print("-------------------------------------------------------------------------------------------")
print("")
difficulty = int(input("Choose your difficulty level for 1 - 10 with 10 being the hardest:"))
level = 0
guessNumber = -1
if difficulty == 10:
    print("Choose between 0 and 10000!")
    level = 10000
if difficulty == 9:
    print("Choose between 0 and 5000!")
    level = 5000
if difficulty == 8:
    print("Choose between 0 and 1000!")
    level = 1000
if difficulty == 7:
    print("Choose between 0 and 750!")
    level = 750
if difficulty == 6:
    print("Choose between 0 and 500!")
    level = 500
if difficulty == 5:
    print("Choose between 0 and 350!")
    level = 350
if difficulty == 4:
    print("Choose between 0 and 200!")
    level = 200
if difficulty == 3:
    print("Choose between 0 and 100!")
    level = 100
if difficulty == 2:
    print("Choose between 0 and 50!")
    level = 50
if difficulty == 1:
    print("Choose between 0 and 10!")
    level = 10

luckyNumber = randint(1, level)

while guessNumber != luckyNumber:
    guessNumber = int(input("Enter your lucky number!:"))
    if guessNumber > luckyNumber:
        print("WRONG! pst...guess lower!Try again!")
    if guessNumber < luckyNumber:
        print("WRONG! pst...guess higher!Try again!")
else:
    print("You guessed the lucky number! Good job!")


