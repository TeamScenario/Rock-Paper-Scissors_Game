import sys
from os import system as _
from time import sleep as sl
import time
from Rock_Paper_Scissors import RPS


while True:
    print("Available: Rock, Paper, Scissors")
    print()
    print("Options:\nA = Rock\nB = Paper\nC = Scissors\nD = Exit")
    print()
    print()
    ut=input("Your input: ").upper()
    _('clear')

    if ut == "A":
        user_input = "Rock"
    elif ut == "B":
        user_input = "Paper"
    elif ut == "C":
        user_input == "Scissors"
    elif ut == "D":
        t=5
        while t>=0: 
           mins, secs = divmod(t, 60) 
           timer = '{:02d}:{:02d}'.format(mins, secs)
           print('estimated time:', timer, end="\r") 
           t -= 1
           sl(1)
        _('clear')
        print('System down.')
        break
    else:
         print("Wrong input try again")
         sl(2)
         _('clear')
    print(RPS(user_input))
    sl(3)
    _('clear')
    
