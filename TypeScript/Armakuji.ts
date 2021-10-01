const convertCoffeeToCode = (str: string): string => {
  return str.split(/Coffee/i).join("Code");
};

const normalString = "Coffee is awesome!. Coffee makes me awake. I love Coffee";
const advanceString = "CoffeeIsAwesomeCoffeeMakeMeAwakesILoveCoffee";

console.log("normal convert : ", convertCoffeeToCode(normalString));
console.log("advanced convert : ", convertCoffeeToCode(advanceString));
