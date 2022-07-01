# Alexander Mallalieu
# Jan 18 2022

word = "ridley" #assigning variables
char = 0
guess = ""
num = len(word)#counting the number of characters in the string 'word' and assigning a variable
while char != num: #as long as the guess is not the same as the word the while loop will run
    guess = input("Guess the word:") #user inputs their guess
    for x in word: #loops throught the variable 'word' one character at a time
        for i in guess:#loops through the variable 'guess' one character at a time
            if i == x:
                char = char + 1 #if the chacacter in guess is the same as the character in x the variable 'char' will have 1 added to it
    if char != num:
        # if the the amount of correct characters is not the same as the number of characters in the word then the characters correct will be printed as a string
        print("Wrong! " + str(char) + " characters correct.")
        char = 0 #if the above if statement is true then it will reset the char back to 0
else:
    print("You cracked it!")#if the above if statement is not true then this will be printed
