import random

def RPS(user_input):
    choices = ["Rock", "Paper", "Scissors"]
    res = random.choice(choices)
    
    if user_input == "Rock" and res == "Rock":
        return "it's a tie"
        
    elif user_input == "Paper" and res == "Paper":
        return "it's a tie"
        
    elif user_input == "Scissors" and res == "Scissors":
        return "It's a tie"
        
    elif user_input == "Rock" and res == "Scissors":
        return "You won 😒"
        
    elif user_input == "Paper" and res == "Rock":
        return "You won 😒"
        
    elif  user_input == "Scissors" and res == "Paper":
        return "You won 😒"
        
    elif user_input == "Rock" and res == "Paper":
        return "I won 😂"
        
    elif user_input == "Paper" and res == "Scissors":
        return "I won 😂"
        
    elif user_input == "Scissors" and res == "Rock":
        return "I won 😂"

    else:
        return "wrong input"
     
        
     
