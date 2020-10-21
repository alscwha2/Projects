/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
	if (strs.length === 0) return '';

	let prefix = '';

	for(let index = 0; index < strs[0].length; index++) {
		let char = strs[0][index];

		for (let strNum = 1; strNum < strs.length; strNum++) 
			if (strs[strNum].length <= index || strs[strNum][index] !== char) 
				return prefix;

		prefix += char;
	}

	return prefix;
};