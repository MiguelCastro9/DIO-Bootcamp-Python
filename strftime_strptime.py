# date formatting in python

import datetime

# converting datetime to string.
d = datetime.datetime.now()
print(d.strftime("%d/%m/%Y %H:%M"))

# converting a string to datetime.
date_string = "1/07/2024 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)