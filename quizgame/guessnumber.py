import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter number greater than 0.")
        quit()
    
else:
    print("Please type a number next time.")

random_number = random.randint(-11, top_of_range)
print(random_number)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it !")
    else:
        print("You got it wrong.")
    
