# coffee = input()
coffee = "coffee"
code = ""
words = coffee.split(' ')
for word in words:
    if word == 'coffee':
        code += 'code'
    else:
        code += word
    code += ' '
code = code.rstrip()
print(code)