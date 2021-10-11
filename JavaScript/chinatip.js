const coffeeToCode = (coffeeText) =>
	coffeeText
		.toLowerCase()
		.split('ff')
		.join('d')
		.split('ee')
		.join('e');

console.log(coffeeToCode('coffee'));
