# def gcd(a, b):
#     smallest = min(a, b)

#     for i in range(smallest, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i

# a = 12
# b = 18

# print("GCD:", gcd(a, b))



def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):

    return (a * b) // gcd(a, b)


a = 12
b = 18

print("LCM:", lcm(a, b))