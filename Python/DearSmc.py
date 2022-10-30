text = "Coffee"
leastAlphabet = ""
result = ""

for i in range(len(text)):
  if leastAlphabet == text[i]:
      if text[i] == "f":
          result = result[:-1]
          result += "d"
      if text[i] == "e":
          continue
  else:
      result += text[i]
  leastAlphabet = text[i]


print(result)
