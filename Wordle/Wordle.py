# Alexander Mallalieu
# March 3rd 2022
# Wordle Assignment
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
# retrieves list of words from separate files for game

with open('../Wordle/wordle_guess_list') as f:
    guesses = f.read().splitlines()

with open('../Wordle/Wordle Possible Answers') as i:
    words = i.read().splitlines()

# chooses a random word from the list 'words'
rand_word = random.choice(words)

x_coord = 0.1
y_coord = 0.7
height = 0.05
width = 0.07
y = 0.1
button = []
guess = []
tries = 0
letters = -1
list_letters = -1

lucky_word = ""
list = []
blank = []

alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

alph_x = 0.28
alph_y = 0.85
gray = []
yellow =[]
green = []
let_in_word = []

root = tk.Tk()

# Creates tkinter canvas within root
canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

# creates tkinter frame within root
frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)

def clear_entry():
    entry.delete(0, END)

def transfer():
    for x in rand_word:
        list.append(x) # adds each letter from the random word to list

transfer()

def attempt():
    global y, letters, guess, tries, entry, alph_x, alph_y, gray, yellow, green, let_in_word # allows variables outside of function to be used within the function
    count = -1
    label_y = y
    label_h = 0.09
    label_w = 0.09
    label_x = 0.28
    tries = tries + 1
    guess = []
    print(gray, " ", yellow, " ", green)
    for x in entry.get():
        guess.append(x)
    # if requirements are/are not made then an error box will be created, notifying the user of their error
    if len(entry.get()) != 5:
        messagebox.showerror("Error", "Guess Must be 5 letters")
        tries = tries - 1
    elif entry.get() not in guesses:
        messagebox.showerror("Error", "Guess not in list")
        tries = tries - 1
    else:
        for x in guess:
            count = count + 1
            if x in list:
                if guess[count] == list[count]:
                    # label is created with position and color, as well as the text being the x value in the loop
                    label = tk.Label(frame, bg="green", text=x, highlightthickness=1, highlightbackground='#7d827e', relief="solid")
                    label.place(relx=label_x, rely=label_y, relheight=label_h, relwidth=label_w)
                    # if x not in green:
                    #     label = tk.Label(frame, bg='green', text=x, highlightthickness=1, highlightbackground='#7d827e')
                    #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
                    #     green.append(x)
                    # if x not in green and x in yellow:
                    #     label = tk.Label(frame, bg='green', text=x, highlightthickness=1, highlightbackground='#7d827e')
                    #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)

                else:
                    label = tk.Label(frame, bg="#cfcf0e", text=x, highlightthickness=1, highlightbackground='#7d827e', relief="solid")
                    label.place(relx=label_x, rely=label_y, relheight=label_h, relwidth=label_w)
                    # if x not in gray and x not in yellow:
                    #     label = tk.Label(frame, bg='#cfcf0e', text=x, highlightthickness=1, highlightbackground='#7d827e')
                    #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
                    #     yellow.append(x)
            else:
                label = tk.Label(frame, bg="gray", text=x, highlightthickness=1, highlightbackground='#7d827e', relief="solid")
                label.place(relx=label_x, rely=label_y, relheight=label_h, relwidth=label_w)
                # if x not in gray and x not in yellow and x not in green:
                #     label = tk.Label(frame, bg='gray', text=x, highlightthickness=1, highlightbackground='#7d827e')
                #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
                #     gray.append(x)
            if x not in let_in_word:
                label = tk.Label(frame, bg='red', text=x, highlightthickness=1, highlightbackground='#7d827e')
                label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
            let_in_word.append(x)


            label_x = label_x + 0.10
            # if user guesses correct word, 'win' labels will be created
            if list == guess:
                win = tk.Label(frame, bg='purple', fg='white', font='100', text='YOU GUESSED THE WORD!')
                win.place(relx=0.375, rely=0.2, relheight=0.1, relwidth=0.3)
                win2 = tk.Label(frame, bg='purple', fg='white', font='100', text='YOU WIN!')
                win2.place(relx=0.375, rely=0.3, relheight=0.1, relwidth=0.3)
            # if user has reached the accepted number of attempts, 'lose' labels will be created
            elif tries == 6:
                lose = tk.Label(frame, bg='red', fg='white', font='100', text='YOU LOST!')
                lose.place(relx=0.375, rely=0.2, relheight=0.1, relwidth=0.3)
                lose2 = tk.Label(frame, bg='red', fg='white', font='100', text='THE WORD WAS ' + rand_word)
                lose2.place(relx=0.375, rely=0.3, relheight=0.1, relwidth=0.3)

                    # label = tk.Label(frame, bg='green', text=x, highlightthickness=1, highlightbackground='#7d827e')
                    # label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
                # else:
                #     label = tk.Label(frame, bg='#cfcf0e', text=x, highlightthickness=1,highlightbackground='#7d827e')
                #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
            # else:
            #     label = tk.Label(frame, bg='gray', text=x, highlightthickness=1, highlightbackground='#7d827e')
            #     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
            alph_x = alph_x + 0.05
            if x == 'p':
                alph_y = 0.9
                alph_x = 0.31
            if x == 'l':
                alph_y = 0.95
                alph_x = 0.34

            y = label_y + 0.11
# entry widget created which allows user to type in the GUI
entry = tk.Entry(frame, bg='white', fg='black', font='40', highlightthickness=0, relief="solid")
entry.place(relx=0.4, rely=0.75)

# alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
#
# alph_x = 0.28
# alph_y = 0.85
# tally = -1

# button created with the attempt() function attached so when clicked the function will run
return_button = tk.Button(frame, bg='gray', font='40', text='enter', command=attempt, highlightthickness=0).place(relx=0.55, rely=0.8)
# button created with entry_clear() function attaches so when clicked the function will run
clear_button = tk.Button(frame, bg='gray', font='40', text='clear', command=clear_entry, highlightthickness=0).place(relx=0.4, rely=0.8)


# alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
#
# alph_x = 0.28
# alph_y = 0.85
# tally = -1
# for x in alphabet:
#     for i in guess:
#         if x in list:
#             if guess[x] == list[x]:
#                 label = tk.Label(frame, bg='green', text=x, highlightthickness=1,highlightbackground='#7d827e')
#                 label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
#             else:
#                 label = tk.Label(frame, bg='#cfcf0e', text=x, highlightthickness=1, highlightbackground='#7d827e')
#                 label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
#     label = tk.Label(frame, bg='gray', text=x, highlightthickness=1,highlightbackground='#7d827e')
#     label.place(relx=alph_x, rely=alph_y, relheight=0.03, relwidth=0.03)
#     alph_x = alph_x + 0.05
#     if x == 'p':
#         alph_y = 0.9
#         alph_x = 0.31
#     if x == 'l':
#         alph_y = 0.95
#         alph_x = 0.34

class Letters:
    





root.mainloop()
