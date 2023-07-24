import datetime
import pygame
from tkinter import *
from pygame import mixer


def alarming():
    hr = hour.get()
    minutes = minute.get()
    dif_hours = int(hr) - datetime.datetime.now().hour
    dif_min = int(minutes) - datetime.datetime.now().minute
    rings_hour = f"rings in: {dif_hours} hours"
    rings_min = f" and {dif_min} minutes"
    rings_in.config(text=rings_hour + rings_min, font=("Arial", 15))
    while True:
        if int(hr) == datetime.datetime.now().hour and int(minutes) == datetime.datetime.now().minute:
            ringing = Label(alarm_app, text="Alarming...", font=("Arial", 30), fg="green")
            ringing.place(x=300, y=340)
            file = "/Users/bishoykamel/Downloads/ss.mp3"
            pygame.mixer.Sound(file).play()
            break
alarm_app = Tk()
mixer.init()
alarm_app.title("Alarm app")
alarm_app.geometry('750x400')
time_required = Label(alarm_app, text="Please enter the alarm time", height=2, font=("Arial", 20))
time_required.pack()

hour = StringVar()
hour.set('00')
if len(str(datetime.datetime.now().minute)) == 1:
    hour.set('0' + str(datetime.datetime.now().minute))
else:
    hour.set(str(datetime.datetime.now().hour))
hour_input = Entry(alarm_app, textvariable=hour, width=2, font=("Arial", 40), borderwidth=0)
hour_input.place(x=300, y=100)

minute = StringVar()
minute.set('00')
if len(str(datetime.datetime.now().minute)) == 1:
    minute.set('0' + str(datetime.datetime.now().minute))
else:
    minute.set(str(datetime.datetime.now().minute))

minute_input = Entry(alarm_app, textvariable=minute, width=2, font=("Arial", 40), borderwidth=0)
minute_input.place(x=380, y=100)
btn = Button(alarm_app, text="save", width=4, height=1, font=("Arial", 30), borderwidth=0, bg="green", fg="white", command=alarming)
btn.place(x=325, y=200)
rings_in = Label(alarm_app)
rings_in.place(x=260, y=300)
alarm_app.mainloop()
