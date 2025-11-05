import random

options = ["rock", "paper", "scissors"]

def get_choice():
    return input("Enter rock, paper, or scissors: ").strip().lower()
def play(): 
    while True:
        try:
            userinput = get_choice()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if userinput not in options:
            print("Pick a real one, my guy.")
            continue

        comp = random.choice(options)
        print(f"Computer chooses: {comp}")

        if userinput == comp:
            print("It's a draw.")
            
        elif (userinput == "rock" and comp == "scissors") or \
             (userinput == "scissors" and comp == "paper") or \
             (userinput == "paper" and comp == "rock"):
            print("You win!")
            
        else:
            print("You lose. Better luck next time.")
            

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    play()