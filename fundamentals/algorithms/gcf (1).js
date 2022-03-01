// Greatest Common Factor
// Given two integers, create recursiveGreatestCommonFactor(num1, num2) to recursively determine Greatest Common Factor (the largest integer dividing evenly into both). Greek mathematician Euclid demonstrated these facts:
// 1) if num1 === num2, that number is the greatest common factor;
// 2) if a>b, then you can remove b from a, which gets you closer to the GCF;
// 3) if b>a, then you can remove a from b, which gets you closer to the GCF;

// Second: rework facts #2 and #3 to reduce stack consumption and expand rGCF ’s reach. You should be able to compute rGCF(123456,987654). Because rGCF(123456, 987654) might exceed your call stack size, Is there a good way to write this function so that it doesn't fail when X and Y grow to certain sizes? Try it out and run these other test cases:

function recursiveGreatestCommonFactor(num1,num2){
    // your code here
}

// console.log(recursiveGreatestCommonFactor(50,180)); // 10
// console.log(recursiveGreatestCommonFactor(7,35)); // 7
// console.log(recursiveGreatestCommonFactor(65,95)); // 5
// console.log(recursiveGreatestCommonFactor(123456,987654)); // 6
// console.log(recursiveGreatestCommonFactor(102,1000)); // 2
// console.log(recursiveGreatestCommonFactor(7,13)); // 1


// There's a way to solve this mathematically using prime numbers, but back in 300 B.C. Euclid came up with an algorithm that lets us find the greatest common factor of two numbers, X and Y:

// - determine if X is greater than Y or if Y is greater than X
// - if X is greater than Y, make X equal to X - Y
// - if Y is greater than X, make Y equal to Y - X
// - continue this process until X is equal to Y - this is your greatest common factor

// Let's try this out using the numbers 800 (X) and 2260 (Y): (color X and Y in red/blue)
// - 2260 is greater than 800, so we'll set Y to 1460 (2280 - 800)
// - 1460 is still greater than 800, so we'll set Y to 660 (1460 - 800)
// - 800 is greater than 660, so we'll set X to 140 (800 - 660)
// - 660 is greater than 140, so we'll set Y to 520 (660 - 140)
// - 520 is greater than 140, so we'll set Y to 380 (520 - 140)
// - 380 is greater than 140, so we'll set Y to 240 (380 - 140)
// - 240 is greater than 140, so we'll set Y to 100 (240 - 140)
// - 140 is greater than 100, so we'll set X to 40 (140 - 100)
// - 100 is greater than 40, so we'll set Y to 60 (100 - 40)
// - 60 is greater than 40, so we'll set Y to 20 (60 - 40)
// - 40 is greater than 20, so we'll set X to 20 (40 - 20)
// - X and Y are now equal - the greatest common factor is 20