import random

def get_choices():
    players_choice=input("Enter the choice('Rock','Paper',Scissor'):")
    options=["Rock","Paper","Scissor"]
    computer_choice=random.choice(options)
    choices={"players_choice":players_choice,"computer_choice":computer_choice}

    return choices
def check_win(players_choice,computer_choice):
    print(f"you chose {players_choice},computer chose {computer_choice}")
    if players_choice==computer_choice:
        return "its a tie!"
    elif players_choice=="Rock":
        if computer_choice=="Paper":
            return "paper covers Rock! you lose!!"
        else :
            return "Rock smashed scissor! you win!!"
    elif players_choice=="Paper":
        if computer_choice=="Scissor":
            return "scissor cuts paper! you lose!!"
        else:
            return "paper covers Rock ! you win!!"
choices=get_choices()
result=check_win(choices["players_choice"],choices["computer_choice"])
print(result)


 

 