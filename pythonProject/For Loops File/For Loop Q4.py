#Alexander Mallalieu
#10th, december, 2021

stuff = input("Enter phrase:")
count_num = 0

for x in stuff:
    if x.isdigit():
        count_num = count_num + 1
print(count_num)