from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# import winsound
import pygame
import time
import sqlite3

frame = Tk()
frame.minsize(300,200)
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)

# sizegrip
sizegrip = ttk.Sizegrip(frame)
sizegrip.grid(row=1,column=0,sticky=(S,E))

s = ttk.Style()
s.configure('MyFrame.TFrame',background='white')

frame1 = ttk.Frame(frame,padding=10,style='MyFrame.TFrame')
frame1.grid(row=0,column=0,sticky=(N,W,S,E))
frame1.columnconfigure(0,weight=1)
frame1.rowconfigure(0,weight=1)


"""
for i in inputs:
    seconds = seconds * 60 + i
"""

c = True

def timer():
    global seconds
    global c
    if seconds > 0:
        frame.after(1000,timer)
        if c:
            button(v=1)
        c = False
        seconds -= 1
        h = seconds//3600
        m = (seconds//60) % 60
        s = seconds % 60
        if s == 59:
            change_icon(m)
        hms = str('{0:^2}時間 {1:^2}分 {2:^2}秒'.format(str(h),str(m),str(s)))
        buff.set(hms)
        frame.title(hms)
    else:
        # winsound.Beep(300,10000)
        sound()
        frame.quit()

icon = ImageTk.PhotoImage(file='images/icon0.png')

def button(v=0):
    if v==0:
        button1 = ttk.Button(
            frame1,
            width=1,
            image=icon,
            text='Start',
            command=timer
        )
        print('Yes',v)
    else:
        button1 = ttk.Button(
            frame1,
            width=1,
            image=icon,
            text='Start',
        )
        print('No',v)

    button1.grid(row=1,column=1,columnspan=2)
    #button1.pack(expand=1,side=RIGHT)

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load('music/DUMBO.mp3')
    pygame.mixer.music.play(1)
    time.sleep(10)

    pygame.mixer.music.stop()

icon1 = ImageTk.PhotoImage(file='images/icon01.png')
icon2 = ImageTk.PhotoImage(file='images/icon2.png')
icon3 = ImageTk.PhotoImage(file='images/icon3.png')
icon4 = ImageTk.PhotoImage(file='images/icon4.png')
icons= (icon1,icon2,icon3,icon4)

def change_icon(num):
    n_icon = icons[num%4]
    # Photo
    label1 = ttk.Label(
        frame1,
        image = n_icon,
        width=15
    )

    label1.grid(row=0,column=0)

if __name__ == '__main__':
    try:
        h,m,s = [int(x) for x in input('Enter the time: ').split(':')]
    except Exception as e:
        print('Input the number')
        h,m,s = [int(x) for x in input('Enter the time!!!: ').split(':')]

    buff = StringVar()
    buff.set('{0:^2}時間 {1:^2}分 {2:^2}秒'.format(h,m,s))

    seconds = h*3600 + m*60 + s

    change_icon(m)

    # A wise saying
    label2 = ttk.Label(
        frame1,
        textvariable=buff,
        width=15,
        font=10,
        anchor=W,
        padding=(1,1))

    label2.grid(row=1,column=0)
    #label2.pack(expand=1,side=RIGHT)

    entry = Entry(frame,textvariable=buff)


    # Button1
    button()

    def button1_clicked():
        frame.quit()


    frame.mainloop()
