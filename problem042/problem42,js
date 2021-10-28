const fs = require("fs");

const data = fs.readFileSync("text.txt", { encoding: "utf8", flag: "r" });

let words = data.split(",").map((x) => x.replace('"', "").replace('"', "")); // todo: fix

function calcWordValue(word) {
  word.split("");

  return word
    .split("")
    .map((x) => x.charCodeAt() - 64)
    .reduce((a, b) => a + b, 0);
}

let wordValues = words.map(calcWordValue);
let max = Math.max(...wordValues);
console.log(max);
function* triangleValue(max) {
  n = 0;
  while (true) {
    n++;
    let value = 0.5 * n * (n + 1);
    if (value <= max) {
      yield value;
    } else {
      return;
    }
  }
}

let set = new Set(Array.from(triangleValue(max)));

console.log(wordValues.map((x) => set.has(x)).filter(Boolean).length);
