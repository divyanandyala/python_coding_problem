str="i am divyareddy"
words=str.split()
longest=""
count=0
for word in words:
    if len(word)>len(longest):
        longest=word
        count+=1
print(longest)
print(count)
