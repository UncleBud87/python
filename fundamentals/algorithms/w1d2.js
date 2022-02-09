// addToFront and removeFront
// as before, no use of .push(), .pop(), .splice(), etc.
// there's also no need for these functions to return anything
// (they can, but they don't need to - why?)
// addToFront(arr, value) - adds value to the start of arr, at index 0
// removeFront(arr) - removes the first item at the start of the array

function addToFront(arr, value) {

    arr[arr.length] = value;
    for (var i = arr.length - 1; i >= 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = value;
}

let test_1 = [1, 2, 3, 4, 5];
addToFront(test_1, 6);
console.log(test_1); // should show [6, 1, 2, 3, 4, 5]
console.log(test_1.length); // should show 6

function removeFront(arr) {
    for (var i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
    }
    arr.length -= 1;
}

let test_1 = [1, 2, 3, 4, 5];
removeFront(test_1);
console.log(test_1); // should show [1, 2, 3, 4, 5]
console.log(test_1.length); // should show 5

function addMultipleToFront(arr, values) {
    for (var i = arr.length - 1; i >= 0; i--) {
        arr[i + values.length] = arr[i];
    }
    for (var i = 0; i < values.length; i++) {
        arr[i] = values[i]
    }
}

let x = [1, 2, 3, 1, 2, 3]

addMultipleToFront(x, [4, 5, 6])

console.log(x);

function removeMultipleFront(arr, count) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i + count];
    }
    arr.length -= count;
}

let x = [1, 2, 3, 1, 2, 3]

removeMultipleFront(x, 3);

console.log(x);