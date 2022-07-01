num1 = int(input("Total number of classes:"))
num2 = int(input("Number of classes attended:"))

num3 = ((num2 / num1) * 100)

print("Attendance Percentage =" + str(num3))

if num3 < 75.0:
    print("1 Medical Excuse")
    print("2 No Medical Excuse")
    excuse = input("Attendance is below 75%, do you have an excuse?")

if num3 >= 75.0 or excuse == "1":
    print("Student is permitted to play a sport.")
elif num3 < 75.0:
    print("Student is not permitted to play a sport")
