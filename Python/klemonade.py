# Please do this in your terminal: 'py slemonade.py'

inp = "Coffee"
inp = inp.replace("f", "d")
result = "".join(dict.fromkeys(inp))
print(result)
