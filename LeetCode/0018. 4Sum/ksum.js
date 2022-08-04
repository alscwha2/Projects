/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
	nums.sort((a,b) => a - b);
    return kSum(nums, target, 4);
};

function kSum(nums, target, k) {
	let groups = []

	if (k === 2) return twoSum(nums, target);
	if (k > 2) 
		for (let i = 0; i < nums.length - (k-1);) {
			kSum(nums.slice(i+1, nums.length), target - nums[i], k-1)
				.forEach(group => groups.push([nums[i]].concat(group)));
			i++;
			while(i < nums.length - (k-1) && nums[i] === nums[i-1]) i++;
		}
	return groups;
}

function twoSum(nums, target) {
	let groups = [];

	let i = 0;
	let j = nums.length - 1;

	while(i < j) {
		let distance = target - nums[i] - nums[j];
		if(!distance) groups.push([nums[i], nums[j]]);
		if (distance <= 0) {
			j--;
			while(i < j && nums[j] === nums[j+1]) j--;
		}
		if (distance >= 0) {
			i++;
			while(i < j && nums[i] === nums[i-1]) i++;
		}

	}
	return groups;
}


