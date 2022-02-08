function changeFirstItem(arr, value){
    arr[0] = value;
}

let x = [6,7,1,2];
let y = x;
changeFirstItem(x,true);
console.log(y);