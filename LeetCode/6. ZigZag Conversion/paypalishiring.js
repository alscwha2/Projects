/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */

var convert = function(s, numRows) {
    if(numRows === 1) return s;

    let str = "";
    columnSpacer = 2 * numRows - 2;

    for(let row = 0; row < numRows; row++) {
    	column = 1;
    	index = row;

    	while(index < s.length) {
    		//print("row: " + row + " index: " + index);
    		str += s[index];
    		nextColumn = row + column * columnSpacer;
    		index = (index - row) % columnSpacer === 0 && row !== numRows - 1 ? nextColumn - (2 * row) : nextColumn;
    		if (index === nextColumn) column++
    	}
    }
    return str;
};


var print = function(s) {
	console.log(s);
};

print(convert("PAYPALISHIRING", 3));