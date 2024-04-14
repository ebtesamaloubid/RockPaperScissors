# Ebtesam Aloubid - 101260655
import random
# Function to check the winning cases
def win(a,b ):
    # paper vs rock -> paper
    # rock vs scissors -> rock
    # scissors vs paper -> scissors
    if ((a == "PAPER" and b == "ROCK")) or (a == "ROCK" and b == "SCISSORS") or (a == "SCISSORS" and b == "PAPER"):
        return True
    return False

# Function to check the lossing cases
def lose(c,d):
    # paper vs scissors -> scissors
    # rock vs paper -> paper
    # scissors vs rock -> rock
    if (c == "PAPER" and d == "SCISSORS") or (c == "ROCK"and d == "PAPER") or (c=="SCISSORS" and d=="ROCK"):
        return True
    return False

# Function to start the game
def game():
    # get an input from the user
    user= input (("What is your choice? ROCK, PAPER, SCISSORS \n")).upper()
    # computer choices
    computer_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    # if the user and the computer choce the same thing ->tie
    if user == computer_choice:
        return f"It is a tie, you and the computer chose {user}."
        # calling the function win
    elif win(user, computer_choice):
        return f"You win!! You chose {user}. and the compurt chose {computer_choice}."
        # calling the function lose
    elif lose(user, computer_choice):
        return f"You lost!! You chose {user}. and the compurt chose {computer_choice}."
        # if the user intered unvalied responce 
    else:
        print ("Please enter a valid response")

#main function 
def main():
    #  while loop allow the user to use the function repeatedly
    while True:
        a = (input("To play type <play> to end the game type <quit> \n"))
        # to quit the game
        if a.upper() == "QUIT":
            break
        # if the user chose to start the game
        elif a.upper() == "PLAY":
            print(game())
            # if the user intered unvalied response
        else:
            print("Please enter a valid response")

# Calling the main 
if __name__ == "__main__":
    main()

