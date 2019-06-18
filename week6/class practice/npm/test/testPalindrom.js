let assert = require("assert");

let reversedText;

function palindromeChecker(text) {

    reversedText = text.toLowerCase().split('').reverse().join('');
    if (text === reversedText) {
        return true;
    }
    return false;
}

let str = "abba";

it("check if the string is palindrome", function() {
  assert(palindromeChecker(str), false);
});
