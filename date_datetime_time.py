# date, datetime and time in python

from datetime import date, datetime, time

dates = date(2024, 6, 29)
print(dates)
print(date.today())

dates_hours = datetime(2024, 6, 29, 21, 30, 59)
print(dates_hours)
print(datetime.today())

hour = time(10, 20, 0)
print(hour)