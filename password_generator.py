from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    number=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+number+special_charecters
    password_length=int(lengthbox.get())

    if choice.get() == 1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    elif choice.get() == 2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+number,password_length))
    else:
        passwordField.insert(0,random.sample(all,password_length))

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='gray20')
root.title("Password Generator")

choice=IntVar()
Font=('Arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('Times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(row=0,column=0,pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
lengthLabel.grid(pady=5)

lengthbox=Spinbox(root,from_=5,to_=18,width=5,font=Font)
lengthbox.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,bg='black',fg='white',command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)

copyButton=Button(root,text='Copy',font=Font,bg='black',fg='white',command=copy)
copyButton.grid(pady=5)

root.mainloop()
