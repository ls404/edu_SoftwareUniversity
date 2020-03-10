// Generating range from negative nr is not easy in js
// this implies imperative solution with cycle....
function solve(min, max) {
    let result;
    for (let i = min; i <= max ; i++){
        result += i;
    }
    return result;
}

console.log(-8, 20)