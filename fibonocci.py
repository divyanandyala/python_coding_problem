# n=int(input("enter the number:"))
# first=0
# second=1
# for i in range(n):
#     print(first,end="")
#     third=first+second
#     first=second
#     second=third


def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=int(input("enter a num:"))
print(fib(n))