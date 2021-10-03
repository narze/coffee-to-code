coffee = "coffee"
coffee = list(coffee)
coffee.append("c")
coffee.append("o")
coffee.append("d")
coffee.append("e")
code = []
for index in range(len(coffee)):
    if index >= 6:
        code.append(coffee[index])
    if index == 9:
        print("".join(code))
