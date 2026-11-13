n=int(input("enter a num"))
temp=n
total=0
while n>0:
    d=n%10
    total=total+d**3
    n=n//10
if total==temp:
    print("armstrong")
else:
    print("not armstrong")