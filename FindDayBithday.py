import datetime
import calendar
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y')
    day = born.weekday()
    return (calendar.day_name[day])
date = input() #example Birthday
print(findDay(date))