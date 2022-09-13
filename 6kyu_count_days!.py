#-----------------------------------------------------My Solution-------------------------------------
from datetime import datetime

def count_days(d):
    if d.date() == datetime.today().date(): 
        return "Today is the day!"
    elif d.date() > datetime.today().date(): 
        a = (d.date() - datetime.today().date()).days
        return str(a) + " " + "days"
    else:
        return "The day is in the past!"
      
#-------------------------------------------------Test File from Creator-----------------------------
import datetime
d = datetime.datetime(2016,12,24, 18, 0)
test.assert_equals(count_days(d), "The day is in the past!")
