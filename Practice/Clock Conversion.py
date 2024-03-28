def convert_time(time):
    hour, minute = map(int, time.split(":"))
    if hour < 12:
        period = "AM"
        if hour == 0:
            hour = 12
    else:
        period = "PM"   
        if hour != 12:
            hour -= 12
    return "{:02d}:{:02d} {}".format(hour, minute, period)
n=int(input())
converted_times = []
for _ in range(n):
    time = input().strip()
    print(convert_time(time))