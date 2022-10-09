from datetime import datetime
import pytz
from get_day import get_day
utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2

# class Day(object):
#     firstclass = ""
#     secondclass = ""
#     thirdclass = ""
#     fourthclass = ""
#     club = ""

#     def __init__(lesson1, lesson2, lesson3, lesson4):
#         firstclass = lesson1
#         secondclass = lesson2
#         thirdclass = lesson3
#         fourthclass = lesson4
#     def classes():
      
# class schedule(object):
#     Day oddday = ""
#     Day evenday = ""
    
#     def __init__(day1, day2):
#       oddday = day1
#       evenday = day2


localFormat = "%B %d, %Y"
timezone = 'America/Los_Angeles'
day = utcmoment.astimezone(pytz.timezone(timezone)).strftime("%d")
month = utcmoment.astimezone(pytz.timezone(timezone)).strftime("%B")
year = utcmoment.astimezone(pytz.timezone(timezone)).strftime("%Y")
if(day[0] == "0"):
  day = day[1]
localDatetime = utcmoment.astimezone(pytz.timezone(timezone))
fullthing = month + " " + day + ", " + year
print(fullthing)

b1 = "AP Calculus BC"
b2 = "English II Honors"
b3 = "Choir"
b4 = "European History"
b5 = "AP Physics 1"
b6 = "Spanish III Honors"
b7 = "Film II"
b8 = "Chemistry"
d1 = [b1,b3,b5,b7]
d2 = [b2,b4,b6,b8]
d3 = [b3,b5,b7,b1]
d4 = [b4,b6,b8,b2]
d5 = [b5,b7,b1,b3]
d6 = [b6,b8,b2,b4]
d7 = [b7,b1,b3,b5]
d8 = [b8,b2,b4,b6]
daylist = [None, d1,d2,d3,d4,d5,d6,d7,d8]

todaysDay = daylist[get_day(fullthing)]
print(todaysDay)