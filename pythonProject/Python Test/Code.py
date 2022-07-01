#Feb 1 2022
#Alexander Mallalieu

names = []

for x in range(5):
    entry = input("Enter names: ")
    names.append(entry)
    if x == 4:
        comp = input("What name would you like to find?")
        break
def findnames():
    if comp in names:
        ind = names.index(comp)
        print("The name ", comp, " matches! It is at index ", ind, " of the list!")
    else:
        print("No Match Found")
findnames()








