def reverse(str1):
    reversestr = ""
    for x in range(len(str1),0,-1):
        reversestr = reversestr + str1[x-1]
    return reversestr


str1 = input("Please type a string to reverse:")
print(reverse(str1))


