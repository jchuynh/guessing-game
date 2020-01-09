"""A number-guessing game."""

# Put your code here

def game():

    import random

    name = input("Hi! What is you're name? > ")

    random_num = random.randint(0, 100)
    attempt = 1

    print(f"{name} I'm thinking of a number between 1 and 100. Guess my number.")


    while True:
        try: 
            user_input = int(input(">"))
            break
        except ValueError:
            print("Please enter a valid integer. > ")

    while True:
        if user_input != random_num:
            if user_input > random_num:
                while True:
                    try:
                        user_input = int(input("Your guess is too high, try again. > "))
                        attempt += 1
                        break
                    except ValueError:
                        print("Please enter a valid integer. > ")
            elif user_input < random_num:
                while True:
                    try:
                        user_input = int(input("Your guess is too low, try again. > "))
                        attempt += 1
                        break
                    except ValueError:
                        print("Please enter a valid integer. > ")
        
        else:
            print(f"Congatulations! you have found the number in {attempt} trys")
            if attempt < best_score:
                best_score = attempt
            print(f"Your all time best score is {best_score}")
            break
            
best_score = [] 
x = 1
while True:
    
    if x == 1:
        game()
    else:
        continue
    x = 0
    choice = input("Would you like to play again? Yes or No. > ")
    if choice == "Y" or choice == "y" or choice == "yes" or choice == "Yes" or choice == "YES":
        x += 1
        continue
    elif choice == "N" or choice == "No" or choice == "NO" or choice == "n" or choice == "no":
        break
    else:
        print("Invalid entry, try again")



    # If choice == Y or choice == y or choice == yes or choice == Yes or choice == YES
