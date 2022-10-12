import random
import string
inp = input("Please input Coffee: ")
count = 0
if inp == "Coffee":
    while 1:
        guess = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        count += 1
        if guess == "CODE":
            print("Iteration ", count, ": ", guess)
            break