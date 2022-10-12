from random import shuffle

string = 'Coffee'
arr = list(set(string))
brewCount = 0
while True:
    shuffle(arr)
    brewCount += 1
    if arr == ['C', 'o', 'f', 'e']:
        break
print(''.join(arr).replace('f', 'd'))
print(f'you brew code from coffee {brewCount} time(s).')