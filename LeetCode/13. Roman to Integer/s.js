/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {

	const numerals = {
		I: 1,
		V: 5,
		X: 10,
		L: 50,
		C: 100,
		D: 500,
		M: 1000
	}
	
	let value = 0;

	let first = undefined;
	let second = undefined;
	for(let i = 0; i < s.length; i++) {
		if (first === undefined) {
			first = s[i];
			continue;
		}
		second = s[i];

		if (numerals[second] > numerals[first]) {
			value += numerals[second] - numerals[first];
			first = undefined;
			second = undefined;
		} else {
			value += numerals[first];
			first = second;
			second = undefined;
		}
	}
	return (first === undefined) ? value : value + numerals[first];
};

console.log(romanToInt(process.argv[2]))