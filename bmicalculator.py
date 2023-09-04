user_name = input("Please enter your name: ")
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height / 100
BMI = Weight / (Height * Height)

if BMI > 0:
    if BMI <= 16:
        print(f"{user_name}, you are severely underweight.")
    elif BMI <= 18.5:
        healthy_bmi_upper = 18.5
        bmi_difference = healthy_bmi_upper - BMI
        print(f"{user_name}, you are underweight by {bmi_difference:.2f} BMI units.")
    elif BMI <= 25:
        print(f"{user_name}, you are within a healthy BMI range.")
    elif BMI <= 30:
        healthy_bmi_upper = 25
        bmi_difference = BMI - healthy_bmi_upper
        print(f"{user_name}, you are overweight by {bmi_difference:.2f} BMI units.")
    else:
        healthy_bmi_upper = 30
        bmi_difference = BMI - healthy_bmi_upper
        print(f"{user_name}, you are severely overweight by {bmi_difference:.2f} BMI units.")
else:
    print("Enter valid details")
