from datetime import date
import time
import datetime
print(date.today())
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

import calendar
cal = calendar.month(2025, 3)
print("Here is the calendar:")
print(cal)

x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)

print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))