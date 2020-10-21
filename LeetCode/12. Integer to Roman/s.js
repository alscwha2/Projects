/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let romanString = "";

    for(let powerTen = 0; powerTen < 4; powerTen++) {
    	if(!num) break;

    	let digit = num % 10;
    	num = Math.floor(num / 10);
    	romanString = digitToRoman(powerTen, digit) + romanString;
    }

	return romanString
};

/**
 * @param {number} powerTen <-- order of ten of current digit
 * @param {number} digit <-- value of digit
 * @return {string} <-- romanified digit
 */
function digitToRoman(powerTen, digit) {
	let ones = ["I", "X", "C", "M"];
	let fives = ["V", "L", "D"];

	switch(digit) {
		case 0:
			return "";
		case 9:
			return ones[powerTen] + ones[powerTen + 1];
		case 4:
			return ones[powerTen] + fives[powerTen];
		default:
			let romanDigit = Math.floor(digit / 5) ? fives[powerTen] : "";
			let numberOfOnes = digit % 5;
			while(numberOfOnes--) romanDigit += ones[powerTen];
			return romanDigit;
	}
}

console.log(intToRoman(process.argv[2]));