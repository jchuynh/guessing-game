"""A number-guessing game."""

# Put your code here
import random

name = input("""Hi! What is you're name? > """)

random_num = random.randint(0, 100)
attempt = 1

print(f"{name} I'm thinking of a number between 1 and 100. Guess my number.")


while True:
    try: 
        user_input = int(input(">"))
        break
    except ValueError:
        print("""Please enter an integer. > """)

while True:
    if user_input != random_num:
        if user_input > random_num:
            while True:
                try:
                    user_input = int(input("""Your guess is too high, try again.
                    > """))
                    attempt += 1
                    break
                except ValueError:
                    print("""Please enter an integer. > """)
        elif user_input < random_num:
            while True:
                try:
                    user_input = int(input("Your guess is too low, try again."))
                    attempt += 1
                    break
                except ValueError:
                    print("""Please enter an integer. > """)
    
    else:
        print(f"Congatulations! you have found the number in {attempt} trys")
        break