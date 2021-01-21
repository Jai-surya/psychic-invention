from datetime import *

now = datetime.now()
dt_date = now.strftime("%d-%m-%Y")

print("Hello World!\n", now)
print("Today's Date is", dt_date)
print("The time right now is", now.strftime("%H:%M:%S"))


