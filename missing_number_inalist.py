# list1 = [1, 2, 3, 5, 6]


# n = len(list1) + 1

# total = n * (n + 1) // 2

# missing = total - sum(list1)

# print("Missing number:", missing)





list1 = [1, 2, 3, 5, 6]

for i in range(1, max(list1) + 1):
    if i not in list1:
        print("Missing number:", i)