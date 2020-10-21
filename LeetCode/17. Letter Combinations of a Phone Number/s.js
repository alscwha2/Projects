/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    let ref = {
			'2' : ['a', 'b', 'c'],
			'3' : ['d', 'e', 'f'],
			'4' : ['g', 'h','i'],
			'5' : ['j', 'k', 'l'],
			'6' : ['m', 'n', 'o'],
			'7' : ['p', 'q', 'r', 's'],
			'8' : ['t', 'u', 'v'],
			'9' : ['w', 'x', 'y', 'z']
	};

	let list = [];
	if (digits.length !== 0) 
		for(let letter of ref[digits[0]]) {
			if (digits.length === 1) 
				list.push(letter);
			else 
				for (let combination of letterCombinations(digits.substring(1))) 
					list.push(letter + combination);
		}
	

	return list
};

console.log(letterCombinations(process.argv[2]))