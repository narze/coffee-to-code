function myCoffee(coffeeText) {
    return coffeeText
        .split('')
        .filter((item, pos, self) =>  self.indexOf(item) === pos)
        .join('')
        .replace('f', 'd')
}

console.log(myCoffee('coffee'))

