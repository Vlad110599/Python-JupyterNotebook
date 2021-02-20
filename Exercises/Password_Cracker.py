import random

small = "abcdefghijklmnopqrstuvwxyz"
large = small.upper()
number = "0123456789"
special = "!@#$%^&*()-_=+[]{}<>.,?/"
char_list = small + large + number + special

password = "PmU@"

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(char_list, k = len(password))

    print(str(guess_password))

    if(guess_password == list(password)):
        print("Your password is: "+"".join(guess_password))
        break
