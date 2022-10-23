//Run code on website https://www.typescriptlang.org/play?#code/PTBKFcDsAIGMHsAmBTa8YHdkCMDOBLAF1QFgAocgG2ULngDN7lkAuaXQgJ30gHNoAvNABEAYQZNkwgNxUadFIOgBtAHTrIyDNADKNABQJGzAJQBdVQCt4PfcOEnVnZAAdKAQ1jI79YQBphRAdZCjIESFx4alVKeF5DJGQTIA

let coffee: string = "Coffee";
let code = [...new Set(coffee)].join("").replace("f","d");

console.log(code)

