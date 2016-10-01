#!/usr/bin/env python3

from tkinter import *
from random import *


rw = Tk () #roll window
result = Text (rw, width=25, height=1, bg='#eeeeee', font='arial 24', fg='dark blue')
summ = Text (rw, width=15, height=1, bg='#eeeeee', font='arial 24', fg='dark blue')
#- result = Label (rw, text = 'ZZZ', width=25, height=1, bg='#eeeeee', font='arial 24', fg='dark blue')
def start ():
    buttonStart.destroy()
    lr.pack()
    result.pack()
    ls.pack()
    summ.pack()
    lclear.pack()
    ld.pack()
    sd.pack()
    lclear2.pack()
    lv.pack()
    sv.pack()
    lclear3.pack()
    buttonRoll.pack()
    lclear4.pack()
    buttonQuit.pack()
def roll ():
    dices = sd.get()
    verges = sv.get()
    result.configure (state='normal')
    result.delete(0.0, END)
    summ.delete(0.0, END)
    summa = 0
    for i in range (0, dices):
        a = randint(1,verges)
        result.insert(END, str (a)+" ")
        summa += a
    summ.insert(END, str (summa))
    result.configure (state='disabled')
#-    result.option_add('text', ' '.join([str(randint(1,verges)) for x in range(dices)]))
def destroy():
    rw.destroy()
lr = Label (rw, text="Result of rolling")
ls = Label (rw, text="Sum")
lclear = Label (rw, text=" ")
lclear2 = Label (rw, text=" ")
lclear3 = Label (rw, text=" ")
lclear4 = Label (rw, text=" ")

ld = Label (rw, text="Dices")
sd = Scale (rw, orient=HORIZONTAL, from_=1,to=10)
sd.set(1)
lv = Label (rw, text="Verges")
sv = Scale (rw, orient=HORIZONTAL, from_=2,to=20)
sv.set(6)
buttonStart = Button (rw, text="Start", command=start, width=25, height=5, bg='#e3d9ae', font='arial 24')
buttonStart.pack()
buttonRoll = Button (rw, text="Roll!", command=roll, width=25, height=1, bg='#e3d9ae', font='arial 24')
buttonQuit = Button (rw, text="Quit", command=destroy, width=10, height=1)

rw.mainloop()
