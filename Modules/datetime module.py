import datetime


from datetime import timedelta

print(datetime.datetime.today())
x= datetime.datetime.today() # we can use datetime.datetime.now also which is same

print(type(x))

other=datetime.datetime(1998,9,11,9,0)

print(other)
print(type(other))
print(x-other)

future_date=x+timedelta(days=1095) # 1095 are the days of 3 years, this line adds 3 years to the current date and time that is "x"
print(future_date)





