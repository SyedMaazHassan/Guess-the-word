from tkinter import*
import tkinter.messagebox
import os

back=Tk()
back.geometry('900x800')

def level_1():
    back.destroy()
    os.system('python simple1.py')
    
def instruction():
    message1=tkinter.messagebox.showinfo('Instructions', '1)   Here, we will provide more than 3 chances to guess an english word \n2)   you will have to guess that word carfully \n\n3)   If your guessed abphabet will not be found in the word, your \t     chances will be decreased. \n\n4)   As the level goes up, difficulty level will be increased.\n\n5)   The will be 4 rounds in each level, consisting the same number of \t       alphabets. \n\n6)   One you will guess all alphabets correctly, will be winner. \n\n7)   otherwise You will be lost, and should be ready to be hanged!')
    
frame01=Frame(back)


pic01=PhotoImage(file='pic013.png')
label01=Label(back, image=pic01)
label01.pack(side='bottom')

label02=Label(frame01, text='Congratulations!', font=('arial','35'))
label02.pack(pady=(50,15))

button01=Button(frame01, bg='#142d39', fg='#FFFFFF',  font=('aria','13') , text='You know how to play', width='35',height='2', command=instruction).pack(pady=(0,15))
button02=Button(frame01, bg='#142d39', fg='#FFFFFF', font=('aria','13') , text='Play and Enjoy Again.!', width='35',height='2', command=level_1)
button02.pack(pady=(0,15))

frame01.pack()


back.mainloop()
