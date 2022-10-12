word = input("Pls give me Coffee --> ")
while word != "Coffee":
    if word == "Coffee":
        break
    word = input("Pls give me Coffe --> ")
print("I will give Code to you.")
print("RU Ready!")
word = word.replace("ffe", "d")
print(word)
