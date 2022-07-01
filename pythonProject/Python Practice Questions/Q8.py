#Rock Paper Scissors
import random
from time import time, sleep


list = ["Rock", "Paper", "Scissors"]
bot = 0
you = 0


def interval():
    sleep(0.9 - time() % 0.9)

def game():
    global bot, you
    choice = input("Rock, Paper, Scissors, Shoot! ")
    enemy = [random.choice(list)]
    interval()
    print("Opponent chose ", enemy[0])
    interval()
    for x in enemy:
        if x == choice:
            print("Darn! A tie!")
        elif x == list[0] and choice == list[1]:
            print("Paper beats Rock! You beat me!")
            you = you + 1
        elif x == list[0] and choice == list[2]:
            print("Ha! Rock beats Scissors! You lose!")
            bot = bot + 1
        elif x == list[1] and choice == list[2]:
            print("Damn! Scissors beats Paper! You beat me!")
            you = you + 1
        elif x == list[2] and choice == list[1]:
            print("Ha! Scissors beats Paper! You Lose!")
            bot = bot + 1
        elif x == list[1] and choice == list[0]:
            print("Ha! Paper beats Rock! You Lose!")
            bot = bot + 1
        elif x == list[2] and choice == list[0]:
            print("Darn! Rock beats Scissors! You beat me!")
            you = you + 1
        interval()
        print("BOT       YOU")
        print("", bot, '       ', you)
        interval()
        answer = input("Do you want to play again? ")
        if answer == "yes" or "ye" or "Yes" or "yeah":
            game()
        elif answer == "no" or "nah" or "No":
            exit()
game()






