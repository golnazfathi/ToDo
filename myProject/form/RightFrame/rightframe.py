from customtkinter import *
from .content.to_do import CreateContent,createstats
def rightframe(sc):
    frame=CTkFrame(
        master=sc,width=540,height=500,corner_radius=0
    )
    frame.place(x=250,y=0)
    createstats(frame)
    CreateContent(frame)
    return frame