function key(string) {
  return string.trim().split("").map(int);
}

function int(character) {
  var results = [];
  for (var i = 0; i < character.length; i++) {
    results.push(character.charCodeAt(i));
  }
  return results;
}

const brain = require("brain.js");
const input = key("Coffee");

const net = new brain.NeuralNetwork();
net.train(
  [
    {
      input: input,
      output: {
        Code: 1,
      },
    },
  ],
);

const result = brain.likely(key("Coffee"), net);

console.log(result);
