import random
import string

# printing lowercase
letters = string.ascii_lowercase
inp = input("input coffee: ")
count = 0
if inp == "coffee":
    while 1:
        guess = ''.join(random.choice(letters) for i in range(4))
        count += 1
        if guess == 'code':
            print(count, " Iteration: ", guess)
            break