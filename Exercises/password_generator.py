#Password generator

import random

small = "abcdefghijklmnopqrstuvwxyz"
large = small.upper()
number = "1234567890"
special = "!@#$%^&*()[]=+-_?.,"

password_format = small + number + special + large
password_lenght = int(input("Enter the lenght of password:"))
password = ""
lenght = 0

if password_lenght<8:
    print("Password of minimum 8 characters is required!")
else:
    while lenght<password_lenght:
        password = password + password_format[random.randint(0,len(password_format)-1)]
        lenght = lenght + 1
    print("Generated password is:",password)
