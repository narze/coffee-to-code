const convetCoffeeToCode = (str: string): string => {
  return str.split(/Coffee/i).join("Code");
};

const normalString = "Coffee is awesome!. Coffee makes me awake. I love Coffee";
const advanceString = "CoffeeIsAwesomeCoffeeMakeMeAwakesILoveCoffee";

console.log("normal convert : ", convetCoffeeToCode(normalString));
console.log("advanced convert : ", convetCoffeeToCode(advanceString));
