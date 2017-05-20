import calendar
from datetime import datetime
now=datetime.now()
ye=now.date()
yea=list(str(ye))
nat=int(yea[5]+yea[6])
year=int(yea[0]+yea[1]+yea[2]+yea[3])
age=int(input('Enter your age: '))
mt=int(input('Enter the month: '))
dy=int(input('Enter the day of the month: '))
if mt>nat:
        yr=year-age-1
else:
    yr=year-age
cal=(calendar.weekday(yr, mt, dy))
day=['Saterday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
print ('You where born on' , day[cal])



    
