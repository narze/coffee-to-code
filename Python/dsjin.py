import re

coffee_pattern = re.compile('([C|c][O|o][F|f][F|f][E|e][E|e])')

class Drink:

    def __init__(self, name: str):

        self.name = name
    
    def affect(self):
        
        if coffee_pattern.match(self.name):
            return coffee_pattern.sub('Code', self.name)

        return self.name

class Human:

    def speak(self, msg: str):
        return print(msg)

    def drink(self, drink: Drink):
        self.feel(drink.affect())

    def feel(self, expression: str):
        print('I feel {expression}!'.format(expression=expression))

class Dsjin(Human):

    def __init__(self):

        self.speak("Working Time!")
        self.speak("But i want to drink coffee first")

me = Dsjin()
coffee = Drink('coffee')
me.drink(coffee)
