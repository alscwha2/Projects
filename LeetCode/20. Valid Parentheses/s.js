/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
	let map = {
		')' : '(',
		'}' : '{',
		']' : '['
	};

	let stack = [];
	for(c of s) {
		if (!(c in map)) stack.push(d);
		else if (!stack.length) return false;
		else if (map[c] !== stack.pop()) return false;
	}
	return !stack.length;
};

console.log(isValid(process.argv[2]));