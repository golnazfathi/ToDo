from customtkinter import *
from .chatbot.chatbot import CreatChatbot
def leftframe(display):
    frame=CTkFrame(
        master=display,width=240,height=500,corner_radius=0
    )
    frame.place(x=0,y=0)
    CreatChatbot(frame)
    return frame