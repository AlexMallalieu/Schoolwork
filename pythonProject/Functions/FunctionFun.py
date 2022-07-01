def example_1():
    for x in range(14):
        print(x)


def example_2():
    num = int(input("Enter Number:"))
    sum = 0
    for x in range(0, num + 1):
        sum = sum + x
    print(sum)


def example_3():
    num = int(input("Enter Number:"))
    x = 0
    while (num * x) < 100:
        x = x + 1
        print(num * x)


def example_4():
    stuff = input("Enter phrase:")
    count_num = 0

    for x in stuff:
        if x.isdigit():
            count_num = count_num + 1
    print(count_num)


def example_5():
    for x in range(-10, 0):
        print(x)


def example_6():
    thing = "*  "

    for x in range(15):
        print(thing * x)

    for x in range(15, 0, -1):
        print(thing * x)


def example_7():
    thing = "*  "
    for x in range(5):
        print(thing + thing + thing)

choice = -1
while choice != 0:
    choice = int(input("What function would you like to use? (1-7)  "))

    if choice == 1:
        example_1()
    if choice == 2:
        example_2()
    if choice == 3:
        example_3()
    if choice == 4:
        example_4()
    if choice == 5:
        example_5()
    if choice == 6:
        example_6()
    if choice == 7:
        example_7()

