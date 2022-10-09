cup(coffeeBeans).
pour_cup(water).

brew(coffee):-
    cup(coffeeBeans),
    pour_cup(water).

drink_coffee :- brew(coffee),
    write('Here is your code').