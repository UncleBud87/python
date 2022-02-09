// bubbleSort, the worst (sane) sorting algortithm!
// not at all efficient, but it's easy to understand
// start from the bottom, compare each item against its neighbor,
// and swap them if they need to be swapped

function bubbleSort(arr) {
    for (var j = 0; j < arr.length; j++) {
        for (i = j + 1; i < arr.length; i++) {
            if (arr[j] > arr[i]) {
                let temp = arr[j]; // [arr[i], arr[j]] = [arr[j], arr[i]]
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
}


let test_a = [8, 1, 4, 5, 9, 2, 7, 6, 3];
bubbleSort(test_a);
console.log(test_a); // should display [1, 2, 3, 4, 5, 6, 7, 8, 9]


let test_b = [1, 3, 2, 3, 6, 3, 3, 3, 3, 3, 5, 9, 3];
bubbleSort(test_b);
console.log(test_b); // should display [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 9]


let test_c = [1, 2, 3, 4, 5, 6, 7, 10, 1, 9];
bubbleSort(test_c);
console.log(test_c); // should display [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 9]


let test_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
bubbleSort(test_c);
console.log(test_c); // should display [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 9]

// let x = [2, 1, 3, 4, 5];
// let temp = x[0];
// x[0] = x[1];
// x[1] = temp;



// extra

function bubbleSort(arr) {

    let ops = 0;


    for (var j = 0; j < arr.length; j++) {
        ops++;
        let swapped = false;
        for (i = j + 1; i < arr.length; i++) {
            ops++;
            if (arr[j] > arr[i]) {
                ops++;
                let temp = arr[j]; // [arr[i], arr[j]] = [arr[j], arr[i]]
                arr[j] = arr[i];
                arr[i] = temp;
                swapped = true;
            }
        }
        if (swapped == false) {
            console.log(ops);
            return undefined;
        }
    }
    console.log(ops);
}