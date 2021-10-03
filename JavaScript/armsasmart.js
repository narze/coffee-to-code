const coffee = "Coffee"
let arr = coffee.split("").map((r, i) => coffee.charCodeAt(i))
arr = arr.join(",").replace("102,102,101", "100").split(",")

console.log(arr.map(r => String.fromCharCode(r)).join(""))
