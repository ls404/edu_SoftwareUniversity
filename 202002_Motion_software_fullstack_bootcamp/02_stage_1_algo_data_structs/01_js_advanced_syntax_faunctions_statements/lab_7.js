const daysMap = {
    "Monday": 1,
    "Friday": 5
}

function solve(map,day) {
    return map[day] ? map[day] : "error";
}

console.log(
    solve(daysMap, "Monday"),
    solve(daysMap, "Friday"),
    solve(daysMap, "Invalid")
);