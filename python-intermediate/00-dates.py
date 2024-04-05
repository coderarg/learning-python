# Dates

from datetime import datetime

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# Unique representation of the date with standard format with reference from 1970
timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023, 1, 1, 0, 0, 0)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

print_date(year_2023)