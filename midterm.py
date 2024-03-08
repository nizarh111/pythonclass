a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2


print(2+3*6/2)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)