# Make a coin flip game

import random
choices = ["heads", "tails"]

user_input = input("Select heads or tails: ").lower()
computer_choice = random.choice(choices)



print(f"You chose: {user_input}")
print(f"The coin is: {computer_choice}")



if user_input == computer_choice:
    print("You win!")
elif user_input in choices:
    print("You lose!")
else:
    print("Invalid option!")

