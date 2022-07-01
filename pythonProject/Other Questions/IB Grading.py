# Alexander Mallalieu
# Nov 25, 2021

grade = int(input("Enter Student's Grade:"))

if 90 < grade <= 100:
    print("The student's IB grade is a 7")
elif 70 < grade <= 90:
    print("The student's IB grade is a 6")
elif 50 < grade <= 70:
    print("The student's IB grade is a 5")
elif 40 < grade <= 50:
    print("The student's IB grade is a 4")
elif 30 < grade <= 40:
    print("The student's IB grade is a 3")
elif 20 < grade <= 30:
    print("The student's IB grade is a 2")
elif 10 <= grade <= 20:
    print("The student's IB grade is a 1")
elif 0 <= grade < 10:
    print("The student's IB grade is a 0")
else:
    print("Error: Invalid Grade")
