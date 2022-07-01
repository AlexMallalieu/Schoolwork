import random


words = ["fish","boat","clark","car","truck","house","cat","dog","ridley","ontario","canada","flag","snow","storm","mountain","programming","computer","science","python"]

randomWord = random.choice(words)
solution = []

for x in range(len(randomWord)):
    print("_", end=" ")
    solution.append("_")
print()

def printList():
    for x in solution:
        print(x,end=" ")
    print()

while True:
    guess = input("Please type in your guess!: ")
    if guess == randomWord:
        break
    count = -1
    for x in randomWord:
        count = count+1
        if x == guess:
            solution[count] = guess
    printList()

print("YOU WON!")




