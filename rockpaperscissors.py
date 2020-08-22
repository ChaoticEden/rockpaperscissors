import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

userScore = 0
compScore = 0
userChoice = " "
compChoice = " "

def choice_to_number(choice):
    rps = {'rock':0, 'paper':1, 'scissors':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0: 'rock' ,1: 'paper' ,2: 'scissors'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def result(human_choice, comp_choice):
    global userScore
    global compScore
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win!")
        userScore+=1
    else:
        print("Computer Wins")
        compScore+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "Your choice: {uc} \nComputer's Choice: {cc} \n Your Score: {u} \n Computer Score: {c}".format(uc=userChoice,cc=compChoice,u=userScore,c=compScore)
    text_area.insert(tk.END,answer)

def rock():
    global userChoice
    global compChoice
    userChoice='rock'
    compChoice=random_computer_choice()
    result(userChoice, compChoice)
def paper():
    global userChoice
    global compChoice
    userChoice='paper'
    compChoice=random_computer_choice()
    result(userChoice, compChoice)
def scissors():
    global userChoice
    global compChoice
    userChoice = 'scissors'
    compChoice = random_computer_choice()
    result(userChoice, compChoice)

button1 = tk.Button(text="      Rock        ", bg="skyblue", command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="      Paper       ", bg="pink", command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Scissors        ", bg="lightgreen", command=scissors)
button3.grid(column=0,row=3)

window.mainloop()
