# Useage `python Python/kidjanate.py`.

def IwantCoffee():
    Code = ""
    for i in "Coffee":
        e = ord(i)
        if len(Code) > 0:
            c = chr(e)
            if Code[-1] != c:
                if ord(c) == 102 : c = chr(100)
                Code = Code + c
        else:
            Code = Code + chr(e)

    Code = Code[0:3:] + Code[-1]
    return Code

print(IwantCoffee())
