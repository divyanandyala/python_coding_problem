# def total_days(days):
#     years=days//365
#     remaining_days=days%365

#     weeks=remaining_days//7
#     remaining_days=remaining_days%7

#     return years,weeks,remaining_days



# days=int(input("enter days"))
# y,w,d=total_days(days)
# print(y)
# print(w)
# print(d)



days=int(input("enter total days"))
years=days//365
remaining_days=days%365

weeks=remaining_days//7
remaining_days=remaining_days%7

print(years)
print(weeks)
print(remaining_days)