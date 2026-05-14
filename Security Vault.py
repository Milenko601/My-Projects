# 🎮 Mini Practice Project — Number Vault

import random

vault_code = random.randint(1, 10)

#Difficulty selection loop
while True:

    try:
        difficulty = int(input("Enter difficulty choice. 3, 5 or 7: "))

        if difficulty in [3, 5, 7]:
            break
        else:
            print("Invalid option!")
    except ValueError:
        print("Invalid option!")

#Difficulty is set
attempts = difficulty


#Game begins
while attempts > 0:
    try:
        guess = int(input("Enter the vault code: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    if guess != vault_code:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts")
        continue

    if guess == vault_code:
        print("You win!")
        break
else:
    print("You lose!")
