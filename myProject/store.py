from jdatetime import datetime,timedelta,JalaliToGregorian,GregorianToJalali
import datetime as dt
import time
from win10toast import ToastNotifier
import threading
from DB.dbcrator import read

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



def display_notification():
    try:
        result=read()
        for item in result:
            if dt.datetime.now().date==item.time.date() and dt.datetime.now().hour==item.time.hour and dt.datetime.now().minute==item.time.minute:
                print(True)
                toaster=ToastNotifier
                toaster.show_toast("Remember",item.task,duration=120)
    except Exception as e:
        print("error: ",e)

def Background_task():
    while True:
        display_notification()
        time.sleep(1)
background_thread=threading.Thread(target=Background_task)
background_thread.daemon=True
background_thread.start()