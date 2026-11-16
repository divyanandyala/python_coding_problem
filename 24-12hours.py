# def convert_time(hour):
#     if hour == 0:
#         return 12
#     elif hour > 12:
#         return hour - 12
#     else:
#         return hour

# print(convert_time(24))
# print(convert_time(13))
# print(convert_time(12))
# print(convert_time(9))




# convert Hours into Minutes and Seconds
# def convert_hours(hours):
#     minutes = hours * 60
#     seconds = hours * 60 * 60

#     print("Minutes:", minutes)
#     print("Seconds:", seconds)

# convert_hours(24)


time = int(input("Enter hour: "))

if time == 0:
    print("12 AM")
elif time < 12:
    print(time, "AM")
elif time == 12:
    print("12 PM")
else:
    print(time - 12, "PM")