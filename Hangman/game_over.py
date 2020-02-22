from tkinter import*
import tkinter.messagebox
import os

back=Tk()
back.geometry('900x800')


def level_1():
    back.destroy()
    os.system('python simple1.py')
    
def Quit():
    back.destroy()
    
frame01=Frame(back)


pic01=PhotoImage(file='pic012.png')
label01=Label(back, image=pic01)
label01.pack(side='bottom')

label02=Label(frame01, text='Try Again Dude!', font=('arial','35'))
label02.pack(pady=(50,15))

button01=Button(frame01, bg='#142d39', fg='#FFFFFF',  font=('aria','13') , text='Play Again', width='35',height='2', command=level_1).pack(pady=(0,15))
button02=Button(frame01, bg='#142d39', fg='#FFFFFF', font=('aria','13') , text='Quit game', width='35',height='2', command=Quit)
button02.pack(pady=(0,15))

frame01.pack()


back.mainloop()
