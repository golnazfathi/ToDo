from customtkinter import *
from DB.dbcrator import read,sestion
from store import getjalali
import datetime as dt
from DB.dbcrator import ToDo, add_task,delete_task

def deleteTsk(id, frame,display):
    delete_task(id)
    frame.destroy()
    print(f"Task {id} deleted.")
    # بارگذاری دوباره کل لیست
    loadtask(display) 

def loadtask(display):
    for widget in display.winfo_children():
        widget.destroy()
    result = read()
    if len(result) > 0:
        for lable in result:  # مقداردهی پیش‌فرض
            color = "#999999"
            date_str = "تاریخ نامشخص"
            time_str = "--:--"
            if lable.time:
                try:
                    date = getjalali(
                        lable.time.year,
                        lable.time.month,
                        lable.time.day,
                        lable.time.hour,
                        lable.time.minute,
                    )

                    color = "#b27bc0" if lable.time <= dt.datetime.now() else "#420F52"
                    date_str = (
                        f"{date.year}/{date.month}/{date.day} {date.strftime('%A')}"
                    )
                    time_str = f"{date.hour}:{date.strftime('%M')}"
                except Exception as e:
                    print("خطا در تبدیل تاریخ:", e)

                frame = CTkFrame(
                    display,
                    width=500,
                    height=35,
                    corner_radius=5,
                    bg_color="transparent",
                    fg_color=color,
                )
                frame.pack(pady=20)

                lbl = CTkLabel(
                    frame, width=15, height=15, text=lable.task, text_color="#f5f5f5"
                )
                lbl.place(x=10, y=15)

                lbl = CTkLabel(
                    frame,
                    width=15,
                    height=15,
                    text=date_str,
                    # f"{date.year}/{date.month}/{date.day} {date.strftime('%A')}",
                    text_color="#f5f5f5",
                )
                lbl.place(x=180, y=15)

                lbl = CTkLabel(
                    frame,
                    width=15,
                    height=15,
                    text=time_str,
                    text_color="#f5f5f5",
                )
                lbl.place(x=380, y=15)

                delet = CTkButton(
                    frame,
                    width=30,
                    height=25,
                    text="Remove",
                    text_color="#020202",
                    fg_color="#9f4cd3",
                    border_width=2,
                    hover=False,
                    command=lambda t_id=lable.id,t_frame=frame:deleteTsk(t_id,frame,display)
                
                )
                delet.place(x=430, y=6)
        
            


            

