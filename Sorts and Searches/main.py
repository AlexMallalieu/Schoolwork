def sort(list):
    n = len(list)
    global swapped
    for x in range(n-1):
        for i in range(0, n-x-1):
            if list[i] > list[i+1]:
                swapped = True
                list[i], list[i+1] = list[i+1], list[i]
        if not swapped:
            return
swapped = False

list = [54,87,92,78,45,13,9]

sort(list)

print(list)




