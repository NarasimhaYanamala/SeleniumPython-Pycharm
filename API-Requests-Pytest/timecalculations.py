from datetime import datetime, date
import calendar
import time

import timestamp

current_date = datetime.now()
print(current_date.strftime('%Y-%m-%dT%H:%M:%S%f%z'))

# current date and time
now = datetime.now()
ISO= datetime.now().isoformat()

print("ISO format:", ISO)
print("now:", now)

day = date.today()
print("date:", day)

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)



'''
# Current GMT time in a tuple format
current_GMT = time.gmtime()
print("current_GMT", current_GMT)
# ts stores timestamp
ts = calendar.timegm(current_GMT)
print("Current timestamp:", ts)
datetime.fromtimestamp(timestamp, tz=None)
'''