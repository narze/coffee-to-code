def roast(bean: str, level="dark"):
    """
    Roast the coffee bean to your liking
    """
    return bean+','+level


def grind(roasted_bean: str):
    """
    Grind the bean to smaller size for dripping
    """
    return roasted_bean.split(',')[0]


def drip(grinded_bean: str):
    """
    Drip the bean to get the coffee
    """
    # blooming
    bloomed = grinded_bean.replace('f', '')
    # dripping
    dripped = bloomed.replace('e', 'd')
    dripped = dripped.capitalize()
    # wait and finish
    return dripped[:-1]+'e'


def drink(cup):
    """
    Enjoy the cup of coffee and channel your energy to your code!
    """
    print(cup)


# start from coffee bean
coffee_bean = "Coffee"

# roast the bean
roasted = roast(coffee_bean)

# grind the bean
grinded = grind(roasted)

# drip the coffee
coffee_cup = drip(grinded)

# enjoy!
drink(coffee_cup)
