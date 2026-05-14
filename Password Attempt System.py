#🔐 Password Attempts System

password = "python123"
attempts = 3


while attempts > 0:
    user_input = input("Please enter your password: ")

    #1. Validate input first
    if user_input == "":
        print("Invalid input.")
        continue

    #2. Admin override (highest priority)
    if user_input == "admin":
        print("Admin override granted")
        break

    #3. Normal password check
    if user_input == password:
        print("Access granted")
        break

    #4. Failure case
    attempts -= 1
    print(f"Password rejected. Attempts left: {attempts} of 3")
else:
    print("Access locked")