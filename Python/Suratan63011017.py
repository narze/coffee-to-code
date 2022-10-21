#By Suratan63011017
str = "coffee"
print("".join([item if item != "f" else chr(ord(item)-2) for item in list("".join(list(str.split("fe"))))]))