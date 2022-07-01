kwh = float(input("Amount of electricity used:"))

num1 = 0.05
num2 = 0.08
num3 = (kwh - 250)
num4 = (num3*0.1)
num5 = (kwh - 100)
num6 = (num5*0.05)
num7 = (kwh - 200)
num8 = (num7*0.08)
num9 = (100*0.05 + num8)
num10 = (100*0.05)
num11 = (50*0.08)

bill = (num4+num10+num11)

if kwh <= 100:
    print("No Charge")
elif 200 >= kwh > 100:
    print(num5, "x", 0.05)
    print("Total Bill = $" + str(num6))
elif 200 < kwh <= 250:
    print(num10, "+", num8)
    print("Total bill = $" + str(num9))
elif kwh > 250:
    print(num10, "+", num11, "+", num4)   #if the number is greater than 250 then the 100kwh x 0.05 + 50 kwh x 0.08 + the number of kwh x 0.1
    print("Total Electricity Bill = $"+ str(bill))


