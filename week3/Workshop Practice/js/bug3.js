function extractStr(str){
    var strWithNumber = str.substring(14);
    return parseInt(strWithNumber);
}

function add(a, b){
    return a + b;
}

var str1 = "my number is 26";
var str2 = "my number is ll";

var sum1 = add(extractStr(str1), 4);
var sum2 = add(extractStr(str2), 9);
var result = add(sum1, sum2);
//result should be 50