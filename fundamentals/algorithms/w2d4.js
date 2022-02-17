// isPalindrome(str) -> input is a single string (str). function returns true if
// the input is a palindrome and false otherwise.
// a palindrome is a word or phrase that is the same forwards or backwards
// for this example, capitalization and other punctuation matter
// "racecar" is a palindrome
// "raCecar" is not (a capital C is not the same as a lowercase c)
// "race car" is not (the space doesn't match up with the E on the opposite side)

function isPalindrome(str) {
    for (var i = 0; i < str.length / 2; i++) {
        if (str[i] != str[str.length - 1 - i]) {
            return false;
        }
    }
    return true;
}

console.log(isPalindrome("racecar"));
console.log(isPalindrome("tacocat"));
console.log(isPalindrome("race car"));
console.log(isPalindrome("e racecar e"));
console.log(isPalindrome("racecar"));
console.log(isPalindrome(""));
console.log(isPalindrome("a"));
console.log(isPalindrome("123454321"));
console.log(isPalindrome(" "));
console.log(isPalindrome("1395742931"));


//function isPalindrome(str) {
//    for (var i = 0; i < str.length / 2; i++) {
//        if (str[i] == str[str.length - 1 - i]) {
//            continue;
//        }
//        else {
//            return false;
//        }
//    }
//    return true;
//}