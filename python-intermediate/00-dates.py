# Dates

from datetime import datetime, date, time, timedelta

now = datetime.now()
""" print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond) """

# Unique representation of the date with standard format with reference from 1970
timestamp = now.timestamp()
# print(timestamp)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

# print_date(now)

year_2023 = datetime(2023, 1, 1)

# print_date(year_2023)

# Date is used to represent a date
today = date.today()
""" print(today.year)
print(today.month)
print(today.day) """

# Time is used to represent a specific time
current_time = time(15, 10, 33)
""" print(current_time.hour)
print(current_time.minute)
print(current_time.second) """

#We can sum integers and months, years, days, etc
today= date(today.year, today.month - 3, today.day)
print(today)
# today= date(today.year, today.month - 5, today.day) Error, we can't exceed 1 to 12 in months
current_time = time(current_time.hour, current_time.minute + 10, current_time.second)
print(current_time)


# We can rest two dates with the same format
time_before = date(2024, 4, 20)
time_after = date(2024, 10, 20)

diff_time = time_before - time_after
print(diff_time)

start_time = timedelta(days = 10)
end_time = timedelta(days = 20)

diff_delta_time = end_time-start_time
print(diff_delta_time)