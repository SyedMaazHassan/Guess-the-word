from tkinter import*
import tkinter.messagebox
import random
import os

LIST=['AT','OF','ON','IN','BY','UP','TO','AS']
answer=random.choice(LIST)
#print(answer)
def change_of_word():
    global answer
    answer=random.choice(LIST)
    #print(answer)
ROUND=1
chances=3

def incriment():
    global ROUND
    ROUND+=1
    
def Chances():
    global chances
    chances=3
    
back=Tk()
def wow():
    Chances()
    def click(x):
        if x in answer:
            global chances;
            if answer[0]==x:
                edit_label_1['text']=x;
            elif answer[1]==x:
                edit_label_2['text']=x;
        else:
    #        if chances!=0:
            label05['text']='Chances left = '+str(chances-1)
            chances=chances-1
            if chances<0:
                label05.configure(fg='#FFFFFF')
                tkinter.messagebox.showinfo('Looser', 'You have lost, start new game')
                back.destroy()
                os.system('python game_over.py')
              #  import game_over.py
        #if edit_label_1['text']==str(answer[0]) and edit_label_1['text']==str(answer[1]):
        if edit_label_1['text']==answer[0] and edit_label_2['text']==answer[1]:
            if ROUND<5:
                incriment()
                tkinter.messagebox.showinfo('oh yes!', 'Keep it up buddy!')
                change_of_word()
                frame01.destroy()
                frame02.destroy()
                frame03.destroy()
                keyboard.destroy()
                wow() 
            else:
                tkinter.messagebox.showinfo('Congratulations', "You have completed level 1. Click 'OK' to go to next level")
                back.destroy()
                os.system('python simple2.py')
                '''import simple2.py
                simple2.wow()'''
                #wow() function of new level 

    back.geometry('900x800')
    back.configure(background='#FFFFFF')

    frame01=Frame(back, bg='#ffffff')

    label03=Label(frame01,background='#FFFFFF', text='LEVEL 1', font=('arial','35'))
    label03.grid(row=1, column=2,  padx=(250,210) ,  pady=(30,30))

    label04=Label(frame01, text='Round '+str(ROUND),background='#FFFFFF', font=('arial','13'))
    label04.grid(pady=(40,40) , padx=(20,20) ,row=1, column=1)

    label05=Label(frame01, text='Chances left = '+str(chances), background='#FFFFFF',font=('arial','13'))
    label05.grid(pady=(40,40) ,padx=(3,150), row=1, column=3)

    frame01.pack(side=TOP)

    
    frame03=Frame(back)
    frame03.configure(background='#142d39')
    label06=Label(frame03, bg='#142d39', fg='#FFFFFF', text='Guess a word that contains only 2 alphabets (prepositions ONLY )', font=('arial','13'))
    label06.pack(pady=(3,3))
    frame03.pack(fill=X)

    
    keyboard=Frame(back)
    keyboard.configure(background='#FFFFFF')
    line1=Frame(keyboard)
    btn0001=Button(line1, text='Q',  bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('Q'))
    btn0001.grid(row=1, column=1, padx=(3,3) )
    btn0001.bind('<a>', lambda: click('Q'))
    btn0002=Button(line1, text='W', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda:click('W'))
    btn0002.grid(row=1, column=2, padx=(3,3) )
    btn0003=Button(line1, text='E', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('E'))
    btn0003.grid(row=1, column=3, padx=(3,3) )
    btn0004=Button(line1, text='R', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('R'))
    btn0004.grid(row=1, column=4, padx=(3,3) )
    btn0005=Button(line1, text='T',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('T'))
    btn0005.grid(row=1, column=5, padx=(3,3) )
    btn0006=Button(line1, text='Y', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('Y'))
    btn0006.grid(row=1, column=6, padx=(3,3) )
    btn0007=Button(line1, text='U',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('U'))
    btn0007.grid(row=1, column=7, padx=(3,3) )
    btn0009=Button(line1, text='I',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('I'))
    btn0009.grid(row=1, column=8, padx=(3,3) )
    btn0010=Button(line1, text='O', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('O'))
    btn0010.grid(row=1, column=9, padx=(3,3) )
    btn0031=Button(line1, text='P', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('P'))
    btn0031.grid(row=1, column=10, padx=(3,3) )
    #btn0010.bind('<Button-1>', letter_o)
    line1.pack(pady=(1,6))

    line2=Frame(keyboard)
    btn0011=Button(line2, text='A',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('A'))
    btn0011.grid(row=1, column=1, padx=(3,3) )
    btn0012=Button(line2, text='S', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('S'))
    btn0012.grid(row=1, column=2, padx=(3,3) )
    btn0013=Button(line2, text='D', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('D'))
    btn0013.grid(row=1, column=3, padx=(3,3) )
    btn0014=Button(line2, text='F', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('F'))
    btn0014.grid(row=1, column=5, padx=(3,3) )
    btn0015=Button(line2, text='G', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('G'))
    btn0015.grid(row=1, column=6, padx=(3,3) )
    btn0016=Button(line2, text='H', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('H'))
    btn0016.grid(row=1, column=7, padx=(3,3) )
    btn0017=Button(line2, text='J',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('J'))
    btn0017.grid(row=1, column=8, padx=(3,3) )
    btn0018=Button(line2, text='K', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('K'))
    btn0018.grid(row=1, column=9, padx=(3,3) )
    btn0019=Button(line2, text='L', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('L'))
    btn0019.grid(row=1, column=10, padx=(3,3) )
    line2.pack(pady=(1,6))

    line3=Frame(keyboard)
    btn0020=Button(line3, text='Z', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('Z'))
    btn0020.grid(row=1, column=1, padx=(3,3) )
    btn0021=Button(line3, text='X', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('X'))
    btn0021.grid(row=1, column=2, padx=(3,3) )
    btn0022=Button(line3, text='C', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('C'))
    btn0022.grid(row=1, column=3, padx=(3,3) )
    btn0023=Button(line3, text='V',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('V'))
    btn0023.grid(row=1, column=4, padx=(3,3) )
    btn0024=Button(line3, text='B', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('B'))
    btn0024.grid(row=1, column=5, padx=(3,3) )
    btn0025=Button(line3, text='N',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'), command=lambda: click('N'))
    btn0025.grid(row=1, column=6, padx=(3,3) )
    btn0026=Button(line3, text='M', bg='#142d39', fg='#FFFFFF', height=2, width=5, font=('','15'), command=lambda: click('M'))
    btn0026.grid(row=1, column=7, padx=(3,3) )
    btn0027=Button(line3, text=':)',  bg='#142d39', fg='#FFFFFF',height=2, width=5, font=('','15'))
    btn0027.grid(row=1, column=8, padx=(3,3) )

    #TY=Button(back, bg='#142d39', fg='#FFFFFF',  font=('aria','13') , text='Play Again', width='35',height='2').pack(side=BOTTOM, pady=(0,15))
    
    line3.pack(pady=(1,6))





    keyboard.pack(pady=(50,160), side=BOTTOM)

    
    frame02=Frame(back)
    
    frame02.configure(background='#FFFFFF')
    sub_frame02=Frame(frame02, height=1,  width=100, bg='#000000').grid(row=1, column=1)

    global edit_label_1
    global edit_label_2
    edit_label_1=Label(frame02, text='' , height=4, fg='#000000', width=8)
    edit_label_1.grid(row=1, column=2, padx=(30,5))
    edit_label_2=Label(frame02, text='', height=4, fg='#000000', width=8)
    edit_label_2.grid(row=1, column=3, padx=(5,30))



    sub_frame02=Frame(frame02, height=1,  width=100, bg='#000000').grid(row=1, column=4)

    frame02.pack(pady=(10,60), side=BOTTOM)


      

wow()


back.mainloop()
