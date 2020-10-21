/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let r = height.length;
    let l = 0;
    let best = 0;
    let current = 0;

    while(r > l) {
    	if(height[r] > height[l]) {
    		current = height[l] * (r - l);
    		l++;
    	} else {
    		current = height[r] * (r - l);
    		r--;
    	}
    	if(current > best) best = current;
    }

    return best;
};