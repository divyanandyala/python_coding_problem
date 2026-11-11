# year=int(input("enter a year:"))

# if year%400==0 or (year%4==0 and year%100!=0):
#     print("leap year")
# else:
#     print("not leap year")


def leap_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "leap year"
    return "not leap year"

year=int(input("enter a year:"))
print(leap_year(year))