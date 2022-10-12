coded_alphabet = [
'''
codecodecode
code    code
codecodecode
code    code
''',
'''
code        
codecodecode
code    code
codecodecode
''',
'''
codecodecode
code        
code        
codecodecode
''',
'''
        code
codecodecode
code    code
codecodecode
''',
'''
codecodecode
code____code
code        
codecodecode
''',
'''
codecodecode
code        
codecode    
code        
''',
'''
codecodecode
code____code
        code
codecodecode
''',
'''
code        
codecodecode
code    code
code    code
''',
'''
codecodecode
    code    
    code    
codecodecode
''',
'''
codecodecode
        code
code    code
codecodecode
''',
'''
code    code
code code   
code   code 
code    code
''',
'''
code        
code        
code        
codecodecode
''',
'''
code    code
code \/ code
code    code
code    code
''',
'''
codecodecode
code    code
code    code
code    code
''',
'''
codecodecode
code    code
code    code
codecodecode
''',
'''
codecodecode
code    code
codecodecode
code        
''',
'''
codecodecode
code    code
codecodecode
        code
''',
'''
codecodecode
code    code
code        
code        
''',
'''
codecodecode
code____    
        code
codecodecode
''',
'''
codecodecode
    code    
    code    
    code    
''',
'''
code    code
code    code
code    code
codecodecode
''',
'''
code    code
code    code
code    code
    code    
''',
'''
code    code
code    code
code /\ code
code    code
''',
'''
code    code
     code   
   code     
code    code
''',
'''
code    code
code    code
codecodecode
        code
''',
'''
codecodecode
        code
    code    
codecodecode
''']

# Clear the terminal
def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import string

drink = input("What are you having to drink?: ")
codified = []

# Make sure input is only letter characters
if drink.isalpha():
    drink = drink.lower().strip()
    if drink == "coffee":
        print("\n😌 Excellent choice! Enjoy your ~")
    else:
        print("\n🤨 Not my first choice, but heres your ~")
else:
    print("\n😠 That's no drink! Have some ~")
    drink = "coffee"
    
# Convert characters into codified ASCII art
for char in drink:
    index = string.ascii_lowercase.index(char.lower())
    codified.append(coded_alphabet[index])

# Print the text line by line
for i in range(5):
    print_line = ""
    for letter in codified:
        print_line += letter.splitlines()[i] + "  "  
    print(print_line)
    
print("\n")
    


