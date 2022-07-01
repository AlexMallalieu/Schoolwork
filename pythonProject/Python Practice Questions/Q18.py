# Cows and Bulls
from random import random, randint

num = []
# num = ["7", "4", "5", "6"]
def comp():
    let = 0
    num = [str(randint(1, 9)), str(randint(1, 9)), str(randint(1, 9)), str(randint(1, 9))]
    for x in num:
        for y in num:
            if x == y:
                let = let +1
                if let == 4:
                    return num
                else:
                    comp()


comp()
list = num
amount = 0
cow = 0
while cow != 4:
    count = -1
    cow = 0
    bull = 0
    guess = (input("Guess the number: "))
    amount = amount + 1
    for x in guess:
        list.append(x)
        count = count + 1
        if x in num:
            ind = num.index(x)
            if count == ind:
                cow = cow + 1
            elif count != ind:
                bull = bull + 1
    if cow == 1 and bull > 1 or bull == 0:
        print(cow, "cow, ", bull, "bulls")
    elif bull == 1 and cow > 1 or cow == 0:
        print(cow, "cows, ", bull, "bull")
    elif cow and bull == 1:
        print(cow, "cow, ", bull, "bull")
    else:
        print(cow, "cows, ", bull, "bulls")
print("Good Job! You Got it!", amount, " guesses were made.")
