const add = (x,y) => x + y;
const addInverse = (x,y) => x + 1/ y;
const concat = (x,y) => x + y.toString()

function solve(...params) {
    return [
        params.reduce(add, 0),
        params.reduce(addInverse, 0),
        params.reduce(concat, "")
    ].join("\n")
}

console.log(solve(1,2,3))


// imperative solution with array as parameter
function aggregateElements(elements) {
    aggregate(elements, 0, (a,b) => a + b);
    aggregate(elements, 0, (a,b) => a + 1 / b);
    aggregate(elements, "", (a,b) => a + b);
    
    function aggregate(arr, initVal, func) {
        let val = initVal;
        for (let i = 0; i < arr.length; i++) 
            val = func(val, arr[i]);    
        console.log(val);         
    }
}

aggregateElements([1,2,3])