import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }
    
    while True:
        roll = input("Roll the dice? (Yes/No): ").lower()
        
        if roll != "yes":
            break
        
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)

        print("Dice result is: {} and {}".format(first_dice, second_dice))
        print("\n".join(dice_drawing[first_dice]))
        print("\n".join(dice_drawing[second_dice]))

roll_dice()
