a=int(input("enter a value"))
b=int(input("enter b value"))
operator=input("enter a operator")

if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("inavalid operator")