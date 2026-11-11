# str="madam"
# temp=str
# rev=""
# for ch in str:
#     rev=ch+rev
#     print(rev)
# print(rev)



# str=input("enter a str:")
# rev=""
# for ch in str:
#     rev=ch+rev

# if str==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

s=int(input("enter the number"))
temp=s
rev=0

while s>0:
    d=s%10
    rev=rev*10+d
    s=s//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")