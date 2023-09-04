user_name =input("Please enter your name: ")
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height / 100
BMI = Weight / (Height * Height)
print("Your Body Mass Index is: ", BMI)

if BMI > 0:
    if BMI <= 16:
        print(user_name, ", you are severely underweight")
    elif BMI <= 18.5:
        print(user_name, ", you are underweight")
    elif BMI <= 25:
        print(user_name, ", you are healthy")
    elif BMI <= 30:
        print(user_name, ", you are overweight")
    else:
        print(user_name, ", you are severely overweight")
else:
    print("Enter valid details")
