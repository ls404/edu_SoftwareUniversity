// original solution is with case....

// solutiion with two parameters
function solve(operator, x, y) {
    return eval(`${x} ${operator} ${y}`)
}

console.log(
    solve('+',1,3)
)

// better solution with multiple params
// eval is anti pattern!!!
function solve2(operator, ...params) {
    return params
    .reduce(
        (a,b) => eval(`${a} ${operator} ${b}`),
        params.shift())
}

console.log(
    solve2("+", 1,2,3,4)
)

console.log(
    solve2("-", 1,2,3,4)
)

// production grade
const operationsMap = {
    "+": (x,y) => x + y,
    "-": (x,y) => x * y
}

function solve3(operator, ...params) {
    return params
    .reduce(
        (a,b) => operationsMap[operator](
            a, Number(b)
        ),
        Number(params.shift())
    );
}

console.log(
    solve3("-", 1,2,3,4)
)