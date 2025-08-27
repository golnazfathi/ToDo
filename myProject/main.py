
from customtkinter import *
from form.RightFrame.rightframe import rightframe
from form.LeftFrame.leftframe import leftframe
sc=CTk()
sc.geometry("800x500+100+100")
sc.resizable(False,False)
set_appearance_mode("dark")


left_fram=leftframe(sc)#leftframe
right_frame=rightframe(sc)#rightfram
sc.mainloop()