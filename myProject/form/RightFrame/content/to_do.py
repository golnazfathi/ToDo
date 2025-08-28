from customtkinter import *
from tkinter import messagebox
from store import datetime,dt,get_month_dates,year,getgragorian,getjalali,gettime,getminute
from DB.dbcrator import ToDo,add_task
from form.RightFrame.content.task import loadtask


def CreateContent(display):


    def submithandler():
        for widget in to_do.winfo_children():
            widget.destroy()

        if entry.get() != "":
            get_date = getgragorian(
                year, month.get(), day.get(), hour.get(), minute.get()
            )
            get_task = entry.get()
            obj = ToDo(get_task, get_date)
            if dt.datetime.now() >= get_date:
                messagebox.showerror("خطا", "زمان گذشته")
                loadtask(to_do)
            else:
                add_task(obj)
                loadtask(to_do)

    def changedate(e):
        day.configure(values=get_month_dates(year, month.get()))
    

    to_do = CTkScrollableFrame(
        display,
        width=510,
        height=350,
        corner_radius=5,
        border_width=0,
        bg_color="transparent",
        fg_color="#242424",
    )
    to_do.place(x=10, y=50)
    loadtask(to_do)

    entry = CTkEntry(
        display,
        width=220,
        height=35,
        border_color="#9f4cd3",
        placeholder_text="type your task",
        placeholder_text_color="#080707",
        text_color="#080707",
    )
    entry.place(x=240, y=455)

    submitbutton = CTkButton(
        display,
        width=40,
        height=35,
        text="✔",
        text_color="#080707",
        fg_color="#9f4cd3",
        border_width=2,
        hover=False,
        command=submithandler,
    )
    submitbutton.place(x=490, y=455)


    month = CTkComboBox(
        display,
        width=35,
        height=35,
        fg_color="#9f4cd3",
        values=datetime.j_months_fa,
        command=changedate,
    )
    month.place(x=5, y=455)

    day = CTkComboBox(
        display,
        width=35,
        height=35,
        fg_color="#9f4cd3",
        values=get_month_dates(year, month.get()),
    )
    day.place(x=60, y=455)

    hour = CTkComboBox(
        display, width=35, height=35, fg_color="#9f4cd3",
        values=gettime()
    )
    hour.place(x=115, y=455)

    minute = CTkComboBox(
        display, width=35, height=35, fg_color="#9f4cd3",
          values=getminute()
    )
    minute.place(x=170,y=455)
    lable=CTkLabel(display,width=100,height=30,text="Month       Day         Hour       Minute",text_color="#080707")
    lable.place(x=10,y=420)


def createstats(display):
    stats_frame = CTkFrame(display, 530, 40, 5, 0, "transparent", "#222222")
    stats_frame.place(x=10, y=5)

    title = CTkFrame(display, 100, 28, 5, 0, bg_color="#222222", fg_color="#9f4cd3")
    title.place(x=30, y=10)

    lbl_title = CTkLabel(title, text="your task", text_color="#070606")
    lbl_title.place(x=25, y=1)

    data = CTkFrame(display, 100, 28, 5, 0, bg_color="transparent", fg_color="#9f4cd3")
    data.place(x=200, y=10)

    ibi_date = CTkLabel(data, text="date", text_color="#070606")
    ibi_date.place(x=38, y=1)

    time = CTkFrame(display, 100, 28, 5, 0, bg_color="#222222", fg_color="#9f4cd3")
    time.place(x=385, y=10)

    ibi_time = CTkLabel(time, text="time", text_color="#070606")
    ibi_time.place(x=38, y=1)