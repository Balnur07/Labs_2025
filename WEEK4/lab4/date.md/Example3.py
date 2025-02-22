'''from datetime import date,timedelta,datetime
time = datetime.now()
withoutmiliseconds = time.strftime("%Y-%m-%d, %H:%M:%S")
print(withoutmiliseconds)'''

from datetime import datetime
current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)
