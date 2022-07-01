#Alexander Mallalieu
#Jan 4 2022

num = int(input("Enter your number:"))#user enters a integer
power = int(input("Enter the power:"))#user enters a integer that will be the power
num1 = 1
for x in range(1,  power+1):#loops the amount of the power inputted
    num1 = num1 * num #Multiplies the number by itself over and over depending on the amount that is the power
    if x == power: #when x is equaled the power then the answer will be printed
        print(num1)
