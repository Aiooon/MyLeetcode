let n = 81, m = 4
let a = [n];
while (m > 1) {
    m--;
    a.push(Math.sqrt(a[a.length - 1]));
}
let sum = 0;
for (let i of a) {
    sum += i;
}
console.log(a, sum.toFixed(2));