const coffeeToCode = (text:string): string => {
  if (text === 'coffee' && new Date().getSeconds() % 2 === 0) {
    return 'code'
  } else {
    return coffeeToCode(text);
  }
}

// Beware infinite loop
console.info(coffeeToCode('coffee'));