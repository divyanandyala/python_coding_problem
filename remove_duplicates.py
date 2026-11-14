arr=[10,20,40,10,20]
new_list=[]
for i in arr:
    if i not in new_list:
        new_list.append(i)
print(new_list)