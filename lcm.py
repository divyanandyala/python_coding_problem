def lcm(a, b):

    largest = max(a, b)

    while True:
        if largest % a == 0 and largest % b == 0:
            return largest

        largest += 1


a = 12
b = 18

print("LCM:", lcm(a, b))