let random = arr => arr[Math.floor(Math.random() * arr.length)];

let BogoCoffeeToCode = str => {
    if (!str.match(/Coffee/)) return str;
    let alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    let tempCode = new Array(4).fill("");
    let tempCoffee = new Array(6).fill("");
    while (true) {
        tempCode = tempCode.map(_ => random(alph));
        tempCoffee = tempCoffee.map(_ => random(alph));
        if (tempCoffee.join("") === "Coffee" && tempCode.join("") === "Code") {
            let regex = new RegExp(tempCoffee.join(""), 'g');
            return str.replace(regex, tempCode.join(""))
        }
    }
}

console.log(BogoCoffeeToCode("I love Coffee Coffee"));

