import calendar
import datetime
import time
from datetime import datetime
from datetime import date

start = time.time()

def init():
    try:
        day = int(input("Enter your birth day (1-31): "))
        month = int(input("Enter your birthmonth in numbers (1-12): "))
        year = int(input("Enter your birth year: "))
        print("\n")
        current_date_time_tuple()
        calendar(month, year)
        calendar_today()
        current_time()
        date_left_until_new_year(day,month,year)
        birth_year_is_leap_year(year)
        week_number_year(day,month,year)
    except Exception as e:
        print("Please enter a valid integer value.", e)

def current_date_time_tuple():
    print("Current Date Time Tuple", datetime.now())

def current_time():
    localtime = time.asctime( time.localtime(time.time()) )
    print("Local current time : {}".format(localtime))

def calendar_today():
    today = date.today()
    cal = calendar.month(today.year,today.month)
    print(cal)

def current_calendar(month, year):
    cal = calendar.month(year,month)
    print(cal)

def date_left_until_new_year(day,month,year):
    today = date.today()
    new_year = date(2019, 1, 1)
    diff = new_year-today
    print ("Days left before New Year : {}".format(diff))

def birth_year_is_leap_year(year):
    leap_year = calendar.isleap(year)
    if leap_year:
        print("The year {} is a leap year.".format(year))
    else:
        print("The year {} is NOT a leap year.".format(year))

def week_number_year(day,month,year):
    mydate = datetime(year,month,day)
    print ("Week number of the year: {}".format(mydate.strftime("%W")))

init()