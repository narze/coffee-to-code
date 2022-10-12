coffees=['coffee','latte','espresso','cappachino','frappechino','bean juice']
def coffee_converter(drinks):
  for coffee in drinks:
    coffee = coffee.lower()
    if coffee in coffees:
      index = drinks.index(coffee)
      drinks[index]='code'
  return drinks

codes = coffee_converter(coffees)

for code in codes:
  print(code)

