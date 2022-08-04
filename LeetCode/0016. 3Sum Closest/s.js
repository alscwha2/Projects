/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
		nums.sort((a, b) => a - b);

		let closestValue = nums[0] + nums[1] + nums[2];
		let closestDistance = Math.abs(closestValue - target);
		for(let i = 0; i < nums.length; i++) {
			let j = i + 1;
			let k = nums.length - 1;

			let newTarget = target - nums[i];
			while(j < k) {
				let currentDistance = newTarget - nums[j] - nums[k];
				if(currentDistance == 0) return target;
				if(Math.abs(currentDistance) < closestDistance) {
					closestDistance = Math.abs(currentDistance);
					closestValue = nums[i] + nums[j] + nums[k];
				}
				if(currentDistance > 0) j++;
				else k--;
			}
		}
		return closestValue;
};