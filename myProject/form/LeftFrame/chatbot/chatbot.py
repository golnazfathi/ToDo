from customtkinter import *

from PIL import Image


def CreatChatbot(diplay):
    image = CTkImage(light_image=Image.open("img/icons8-bot-48.png"), size=(50, 50))

    lable = CTkLabel(diplay, image=image, text="")
    lable.place(x=100, y=100)

    lable_text = CTkLabel(diplay, text="ask me any think ...")
    lable_text.place(x=75, y=150)

    entry = CTkEntry(
        diplay,
        190,
        35,
        5,
        1,
        "transparent",
        "#2f024b",
        border_color="#e2e2e2",
        placeholder_text="ask me question dude ...",
    )
    entry.place(x=8, y=455)


    send_chat = CTkButton(
        diplay,
        text="✔",
        width=35,
        height=35,
        corner_radius=5,
        border_width=0,
        bg_color="#c88aef",
        fg_color="#2f024b",
        hover=False,
        text_color="black",
    )
    send_chat.place(x=203, y=455)
