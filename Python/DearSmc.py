import random
def initCode(word):
  makePowerList = ["coffee", "beer", "shabu"]
  arr = []
  if word in makePowerList:
    arr = list(set(word))
    str = "".join(set(word)).replace("f","d")
    arr = list(str)
    while str != "code":
      random.shuffle(arr)
      str = "".join(arr);
    print(str)

  else:
    print("I'm so tired that not enough")

startWord = "coffee"
initCode(startWord)
