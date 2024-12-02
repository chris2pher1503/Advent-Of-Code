import * as fs from "fs";

let diff: number = 0;
let left: number[] = [];
let right: number[] = [];

const fileContent: string = fs.readFileSync("input.txt", "utf8").trim();
const lines: string[] = fileContent.split("\n");

lines.forEach(line => {
    let nums = line.split(" ")
    
});

left.sort((a, b) => a - b);
right.sort((a, b) => a - b);

for (let i = 0; i < right.length; i++) {
    diff += Math.abs(left[i] - right[i]);
}

console.log(diff);