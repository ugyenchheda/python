import random
import string

random_characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")
def generate_shhh():
    shhh_length = int(input("Please enter number of characters to be used... "))
    random.shuffle(random_characters)
    shhh = []
    
    for x in range(shhh_length):
        shhh.append(random.choice(random_characters))
    random.shuffle(shhh)
    shhh = "".join(shhh)
    print(shhh)
  
option = input("Enter Yes to generate password and no to quit? (Yes/No): ").lower()

if option == "yes":
    generate_shhh()
elif option == "no":
    print("Ok, bye bye...")
    quit()
else:
    print("Please enter valid input...")
    quit()
