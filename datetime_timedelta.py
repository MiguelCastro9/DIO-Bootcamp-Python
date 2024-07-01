# timedelta in python

import datetime

d = datetime.datetime(2024, 6, 29, 20, 50, 10)
print(d)

d = d + datetime.timedelta(weeks=1)
print(d)

d = d + datetime.timedelta(days=1)
print(d)


d = d + datetime.timedelta(hours=5)
print(d)