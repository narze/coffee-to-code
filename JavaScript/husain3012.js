String.prototype.replaceAt = function (index, replacement) {
  return this.substr(0, index) + replacement + this.substr(index + replacement.length);
};

const coffee_in_code_out = (coffee) => {
  let code = "";

  for (let i = 0; i < coffee.length; i++) {
    if (coffee[i] === "f") {
      coffee = coffee.replaceAt(i, "d");
    }
  }
  for (let i = 0; i < coffee.length; i++) {
    if (coffee[i] != coffee[i + 1]) {
      code += coffee[i];
    }
  }
  return code;
};
console.log(coffee_in_code_out("coffee"));
