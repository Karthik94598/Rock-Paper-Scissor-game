import random

def game():
    elements = ["rock" , "paper" , "scissors"]
    your_selection = input("Enter your choice from  (rock ,paper, scissors): ").strip().lower()
    system_selection = random.choice(elements)
    print(f"your slection is {your_selection}")
    print(f"computer slection is {system_selection}")
    
    if your_selection in elements:
        if your_selection=="rock" and system_selection=="scissors":
            print("You win ! \U0001F600")
            game()
        elif your_selection=="paper" and system_selection=="rock":
            print("You win ! \U0001F600")
            
            game()
        elif your_selection=="scissors" and system_selection=="paper":
            print("You win ! \U0001F600")
            
            game()
        elif your_selection == system_selection:
            print("your game is tie")
            
            game()
        else:
            print("you are lost \U0001F625")
            print("Do you want to play again(y/n): ")
            yes = "y"
            no = "n"
            result = input()
            if result==yes:
                game()
            elif result == no :
                print("Thankyou for playing !")
            else:
                print("invalid option, Exit...")

    else:
        print("please choose your choice from  (rock ,paper, scissors) for next time  \U0001F615")
        game()

game()