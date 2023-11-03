import customtkinter
from tkinter import END
from tkinter import messagebox

#functional part
def enter(num):
    entryField.insert(END,num)
def clear():
    entryField.delete(0,END)
def solution():
    try:
        expression=entryField.get()
        result=eval(expression)
        entryField.delete(0,END)
        entryField.insert(0,result)
    except SyntaxError:
        messagebox.showerror("Invalid Syntax!!")
    except ZeroDivisionError :
        messagebox.showerror("Error!")


#gui part
root = customtkinter.CTk()
root.title('Modern Calculator')
root.geometry('300x300')
root.config(bg='grey20')

entryField=customtkinter.CTkEntry(root,font=('arial',20,'bold'),text_color='white',fg_color='black',bg_color='black',
                                  width=280,height=50,border_color='white')
entryField.grid(row=0,column=0,padx=10,pady=2,columnspan=4)

b7=customtkinter.CTkButton(root,text='7',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('7'))
b7.grid(row=1,column=0,padx=5,pady=7)

b8=customtkinter.CTkButton(root,text='8',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('8'))
b8.grid(row=1,column=1,padx=5,pady=7)

b9=customtkinter.CTkButton(root,text='9',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('9'))
b9.grid(row=1,column=2,padx=5,pady=7)

b_plus=customtkinter.CTkButton(root,text='+',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='orange',
                           text_color='black',cursor='hand2',command=lambda : enter('+'))
b_plus.grid(row=1,column=3,padx=5,pady=7)

b4=customtkinter.CTkButton(root,text='4',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('4'))
b4.grid(row=2,column=0,padx=5,pady=5)

b5=customtkinter.CTkButton(root,text='5',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('5'))
b5.grid(row=2,column=1,padx=5,pady=5)

b6=customtkinter.CTkButton(root,text='6',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('6'))
b6.grid(row=2,column=2,padx=5,pady=5)

b_minus=customtkinter.CTkButton(root,text='-',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='orange',
                           text_color='black',cursor='hand2',command=lambda : enter('-'))
b_minus.grid(row=2,column=3,padx=5,pady=5)

b1=customtkinter.CTkButton(root,text='1',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('1'))
b1.grid(row=3,column=0,padx=5,pady=5)

b2=customtkinter.CTkButton(root,text='2',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('2'))
b2.grid(row=3,column=1,padx=5,pady=5)

b3=customtkinter.CTkButton(root,text='3',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('3'))
b3.grid(row=3,column=2,padx=5,pady=5)

b_mult=customtkinter.CTkButton(root,text='*',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='orange',
                           text_color='black',cursor='hand2',command=lambda : enter('*'))
b_mult.grid(row=3,column=3,padx=5,pady=5)

b0=customtkinter.CTkButton(root,text='0',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2',command=lambda : enter('0'))
b0.grid(row=4,column=0,padx=5,pady=5)

bdot=customtkinter.CTkButton(root,text='.',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='white',
                           text_color='black',cursor='hand2')
bdot.grid(row=4,column=1,padx=5,pady=5)

bclear=customtkinter.CTkButton(root,text='C',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='red',
                           text_color='black',cursor='hand2',command=clear)
bclear.grid(row=4,column=2,padx=5,pady=5)

b_div=customtkinter.CTkButton(root,text='/',font=('arial',20,'bold'),width=60,bg_color='black',fg_color='orange',
                           text_color='black',cursor='hand2',command=lambda : enter('/'))
b_div.grid(row=4,column=3,padx=5,pady=5)

b_equal=customtkinter.CTkButton(root,text='=',font=('arial',20,'bold'),width=250,bg_color='black',fg_color='green',
                           text_color='black',cursor='hand2',command=solution)
b_equal.grid(row=5,column=0,columnspan=4,padx=5,pady=10)



root.mainloop()
