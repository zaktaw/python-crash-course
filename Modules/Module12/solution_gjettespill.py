# Gjettespill

import random

num = random.randint(1,100)

user_input = ""
attempts = 0

while(user_input != num):

    user_input = int(input("Gjett et tall: "))
    attempts += 1

    if user_input == num:
        print("Du gjettet riktig!")
    elif user_input > num:
        print("Du gjettet for høyt")
    else:
        print("Du gjettet for lavt")

print("Du brukte " + str(attempts) + " forsøk.")