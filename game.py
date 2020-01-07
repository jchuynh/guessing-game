"""A number-guessing game."""

# Put your code here
import random

name = input("""Hi! What is you're name?
    > """)

random_num = random.randint(0, 100)
attempt = 1

print(f"{name} I'm thinking of a number between 1 and 100. Guess my number.")

user_input = input(">")
user_input = int(user_input)
while True:
    if user_input != random_num:
        if user_input > random_num:
            user_input = int(input("Your guess is too high, try again."))
            attempt += 1
        elif user_input < random_num:
            user_input = int(input("Your guess is too low, try again."))
            attempt += 1
    else:
        print(f"Congatulations! you have found the number in {attempt} trys")
        break