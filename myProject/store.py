from jdatetime import datetime,timedelta,JalaliToGregorian,GregorianToJalali
import datetime as dt
import time
year=datetime.now().year


def getgragorian(year,month,day,hour,minute):
    get_month=datetime.j_month_fa_to_num(month)
    gragorian=JalaliToGregorian(int(year),int(get_month),int(day))
    return dt.datetime(gragorian.gyear,gragorian.gmonth,gragorian.gday,int(hour),int(minute))





def getjalali(year,month,day,hour,minute):
    time=GregorianToJalali(year,month,day)
    return datetime(time.jyear,time.jmonth,time.jday,hour,minute)

# print(JalaliToGregorian(1379,1,12).gyear,JalaliToGregorian(1379,1,12).gmonth,JalaliToGregorian(1379,1,12).gday)



def get_month_dates(year,month):
    month_to_num=datetime.j_month_fa_to_num(month)
    days=[]
    if month_to_num==12:
        last_day=datetime(year+1,1,1)-timedelta(days=1)
        for item in range(last_day.day):
            item+=1
            days.append(str(item))
        return days
    else:
        last_day=datetime(year,month_to_num + 1,1)-timedelta(days=1)
        for item in range(last_day.day):
            item+=1
            days.append(str(item))
        return days
    



def gettime():
    hours=[]
    for i in range(24):
        hours.append(str(i))
    return hours


def getminute():
    minute=[]
    for i in range(60):
        minute.append(str(i))
    return minute


