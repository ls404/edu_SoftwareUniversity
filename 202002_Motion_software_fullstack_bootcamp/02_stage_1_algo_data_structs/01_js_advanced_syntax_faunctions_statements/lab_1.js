// bad solution
function solve(x, y, z) {
    let sum = x.length + y.length + z.length;
    let avrg = Math.floor(sum / 3);
    console.log(sum);
    console.log(avrg)
}
// good solution
function solve2(...params) {
    let sum = params.reduce((a, b) => a + b.length, 0);
    let avrg = Math.floor(sum / params.length)
    return [sum, avrg]
}

solve("chocolate", "ice cream", "cake")

console.log(solve2("chocolate", "ice cream", "cake").join("\n"))