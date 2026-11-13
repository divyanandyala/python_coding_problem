n=input("enter a str:")
count=0
for i in n:
    if i in "aeiouAEIOU":
        count=count+1
print(count)