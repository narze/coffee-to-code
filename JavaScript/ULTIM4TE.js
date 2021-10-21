const text = "Coffee";

const filteredF = text.split("").filter(function (e) {
  return e !== "f";
});

const filteredE = filteredF.filter(function (e) {
  return e !== "e";
});

filteredE.push("de");

const result = filteredE.join("");

console.log(`Result :`, result);
