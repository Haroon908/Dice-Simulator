import random
from tkinter import *

root = Tk()
root.title("Dice Simulator")
root.geometry("500x400")
root.configure(bg="grey")

label = Label(root,font=("helvetica",250,"bold"),text = "",bg="grey")



def rollDice():
    List = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f"{random.choice(List)}")
    label.pack()

button = Button(root,font=("helvetica",25,"bold"),text="Roll Dice",command = rollDice,bg="black",fg="white")
button.pack()

root.mainloop()