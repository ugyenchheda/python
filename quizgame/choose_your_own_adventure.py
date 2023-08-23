name = input("Enter your name: ")
print("Welcome", name , "to this adventure.")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you wanna go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type to walk to walk and swim to swim: ").lower()
    if answer == "swim":
        print("You swam right towards aligator and it ate you.")
    elif answer == "walk":
        print("You walked for many miles, ran out of food and water and you eventually died.")
    else:
        print("Not a valid answer, you lose.")
elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you wanna cross it or head back. (cross/back)? ").lower()
    if answer == "back":
        print("You went back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and met a stranger. Do you wanna talk to him?(Yes/No) ")
        
        if answer == "yes":
            print("You talk to the stranger and he gave you gold. You WIN.")
        
        elif answer == "no":
            print("You ignored the stranger and he is offended and you lose.")

        else:
            print("Not a valid answer. You lose.")
    else:
        print("Not a valid answer. You loose.")

else:
    print("Not a valid option. You lose...")

print("Thank you for trying", name)