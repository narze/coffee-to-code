const input = prompt(
  "Prompt only accepts the string 'Coffee' and will automatically be changed to 'Code': "
);

if (input == "Coffee") {
  alert("Output: Code");
} else {
  alert("Error: Wrong input");
}