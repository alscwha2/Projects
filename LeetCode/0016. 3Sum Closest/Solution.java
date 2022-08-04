import java.util.Arrays;
class Solution {
	public int threeSumClosest(int[] nums, int target) {
		Arrays.sort(nums);

		int closestValue = nums[0] + nums[1] + nums[2];
		int closestDistance = Math.abs(closestValue - target);
		for(int i = 0; i < nums.length; i++) {
			int j = i + 1;
			int k = nums.length - 1;

			int newTarget = target - nums[i];
			while(j < k) {
				int currentDistance = newTarget - nums[j] - nums[k];
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
	}
}