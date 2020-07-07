// Add up and print the sum of the all of the minimum elements of each inner array:
// [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

// go through
// first min 
//then add them

//maybe advanced array method 

const arrays = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

let answer = 0
arrays.forEach(r => {
answer += Math.min(...r)

})

// sum = 0
// for i in arrays:
//     sum += min(i)
// print(sum)
console.log(answer)