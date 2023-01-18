def RPS():
    ''' By @CoderX on Telegram'''
    user_input, choices = input("Enter your input\n    • Rock\n    • Paper\n    • Scissors\n    • 0 to exit:  ").title(), ["Rock", "Paper", "Scissors"] 
    res = __import__("random").choice(choices)
    WHW = ["Computer's input:- {}\nYour input:- {}\n\nResult :- ✨ You won ✨".format(res,user_input), "Computer's input:- {}\nYour input:- {}\n\nResult :- 😴 Computer won 😴".format(res,user_input), "Computer's input:- {}\nYour input:- {}\n\nResult :- it's a tie!".format(res,user_input)]
    if user_input == res:return WHW[2]
    elif user_input == "Rock" and res == "Scissors" or user_input == "Paper" and res == "Rock" or user_input == "Scissors" and res == "Paper":return WHW[0]
    elif user_input == "Rock" and res == "Paper" or user_input == "Paper" and res == "Scissors" or user_input == "Scissors" and res == "Rock":return WHW[1]
    elif user_input == "0":exit("\033[H\033[2J\033[32m\033[1mEnded\033[0m")
    else:return "wrong input"
