function solve(a,b,c) {
    return  `The largest number is ${[a,b,c]
        .sort((a,b) => a - b).pop()}.`
}

console.log(solve(5, -3, 16))


// with endless number of params
function solve2(...params) {
    return  `The largest number is ${params
        .sort((a,b) => a - b).pop()}.`
}

console.log(solve2(5, -3, 16, 66))

// with endless number of params
function solve3(...params) {
    return  `The largest number is ${Math.max(...params)}.`
}

console.log(solve3(5, -3, 16, 66))