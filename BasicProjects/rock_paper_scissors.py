import random

user_choice = input("Rock, Paper or Scissors?").lower()
computer_choice = random.choice(["Rock", "Paper", "Scissors"]).lower()
print(f"your choice: {user_choice} 'X' computer choice: {computer_choice}")

def main():
    if user_choice == computer_choice:
        print("The Game has been Drawn")
    elif (user_choice == "rock" and computer_choice == "scissors"
    or user_choice == "paper" and computer_choice == "rock"
    or user_choice == "scissors" and computer_choice == "paper"):
        print(f"user wins!")
    elif user_choice in ['rock', 'paper', 'scissors']:
        print(f"computer wins!")
    else:
        print(f"Invalid choice: {user_choice}")
if __name__ == "__main__":
    main()
