s=input("enter the string:")
dup=[]
for i in s:
    if i not in dup:
        dup+=i
print(dup)