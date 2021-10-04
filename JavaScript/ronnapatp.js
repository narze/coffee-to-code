var drink = coffee

console.log([...new Set(drink.split(''))].join('').replace("f", "d"))
