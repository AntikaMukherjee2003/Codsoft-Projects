from tkinter import *
import random

schema={
    'Rock':{'Rock':1,'Paper':0,'Scissors':2},
    'Paper':{'Rock':2,'Paper':1,'Scissors':0},
    'Scissors':{'Rock':0,'Paper':2,'Scissors':1}
}

player_score=0
comp_score=0
def enter(user_choice):
    global player_score
    global comp_score
    outcomes=['Rock','Paper','Scissors']
    random_number=random.randint(0,2)
    comp_choice=outcomes[random_number]
    player_choice_Label.config(fg='red',bd=2,text='Player choice : '+str(user_choice))
    computer_choice_Label.config(fg='green',bd=2,text='Computer Choice : '+str(comp_choice))

    result=schema[user_choice][comp_choice]

    if result==2:
        player_score=player_score+2
        comp_score=0
        player_score_Label.config(fg='green',text='Player : '+str(player_score))
        computer_score_Label.config(fg='green', text='Computer : ' + str(comp_score))
        outcome_Label.config(fg='blue',text='Outcome :  Player Won!!')
    elif result==1:
        player_score = player_score + 1
        comp_score = comp_score+1
        player_score_Label.config(fg='green', text='Player : ' + str(player_score))
        computer_score_Label.config(fg='green', text='Computer : ' + str(comp_score))
        outcome_Label.config(fg='blue', text='Outcome : Match Draw!!')
    elif result==0:
        player_score=0
        comp_score=comp_score+2
        player_score_Label.config(fg='green', text='Player : ' + str(player_score))
        computer_score_Label.config(fg='green', text='Computer : ' + str(comp_score))
        outcome_Label.config(fg='blue', text='Outcome : Computer Won!!')


root = Tk()

root.title("Rock Paper Scissors")
root.config(bg='antiquewhite3')
root.geometry('550x260')

rpsLabel=Label(root,text='Rock Paper Scissors',font=('Times new roman',20,'bold'),bg='black',fg='white')
rpsLabel.grid(row=0,sticky=N,padx=150)

opLabel=Label(root,text='Please Select an Option',font=('Arial',15,'bold'),bg='gray',fg='white')
opLabel.grid(row=1,sticky=N,pady=10)

player_score_Label=Label(root,text='Player : 0',font=('arial',13),bg='antiquewhite3',fg='white')
player_score_Label.grid(row=2,sticky=W)

computer_score_Label=Label(root,text='Computer : 0',font=('arial',13),bg='antiquewhite3',fg='white')
computer_score_Label.grid(row=2,sticky=E)

player_choice_Label=Label(root,font=('arial',10))
player_choice_Label.grid(row=3,sticky=W)

computer_choice_Label=Label(root,font=('arial',10))
computer_choice_Label.grid(row=3,sticky=E)

outcome_Label=Label(root,font=('arial',10))
outcome_Label.grid(row=3,sticky=N)

rockButton=Button(root,text='Rock',font=('arial',15,'bold'),width=10,bg='white',fg='black', command=lambda: enter('Rock'))
rockButton.grid(row=4,column=0,sticky=W,pady=20,padx=15)

paperButton=Button(root,text='Paper',font=('arial',15,'bold'),width=10,bg='white',fg='black', command=lambda: enter('Paper'))
paperButton.grid(row=4,sticky=N,pady=20,padx=15)

scissorsButton=Button(root,text='Scissors',font=('arial',15,'bold'),width=10,bg='white',fg='black', command=lambda: enter('Scissors'))
scissorsButton.grid(row=4,sticky=E,pady=20,padx=15)

root.mainloop()