import random

def RPS(user_input):
    choices = ["Rock", "Paper", "Scissors"]
    res = random.choice(choices)
    U_W = "Computer's input:- {}\nYour input:- {}\n\nResult :- ✨ You won ✨".format(res,user_input)
    C_W = "Computer's input:- {}\nYour input:- {}\n\nResult :- 😴 Computer won 😴".format(res,user_input)
    N_W = "Computer's input:- {}\nYour input:- {}\n\nResult :- it's a tie!".format(res,user_input)
    
    if user_input == res:
        return N_W

    if user_input == "Rock" and res == "Scissors":
        return U_W
        
    elif user_input == "Paper" and res == "Rock":
        return U_W
                
    elif  user_input == "Scissors" and res == "Paper":
        return U_W
                
    elif user_input == "Rock" and res == "Paper":
        return C_W
        
    elif user_input == "Paper" and res == "Scissors":
        return C_W
        
    elif user_input == "Scissors" and res == "Rock":
        return C_W
    else:
        return "wrong input"
