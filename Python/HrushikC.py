word = "Coffee"
word = word.replace("ffee", "")
hex_val = hex(int("ffee", 16) - int("ff10", 16))
word = word + str(hex_val)[2:]
print(word)
