import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;

class KSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
    	Arrays.sort(nums);
        return kSum(nums, target, 4);
    }

    private List<List<Integer>> kSum(int[] nums, int target, int k) {
    	HashSet<List<Integer>> groups = new HashSet<>();

    	if(k > 2) {
    		for(int i = 0; i < nums.length - (k-1); i++)
    			for(List<Integer> group : kSum(Arrays.copyOfRange(nums, i+1, nums.length), target - nums[i], k-1)) {
    				LinkedList<Integer> newgroup = new LinkedList<Integer>(group);
    				newgroup.add(0, nums[i]);
    				groups.add(newgroup);
    			}
    	}
    	if(k == 2) return twoSum(nums, target);

    	return new LinkedList<List<Integer>>(groups);
    }

    private List<List<Integer>> twoSum(int[] nums, int target) {
    	HashSet<List<Integer>> groups = new HashSet<>();

    	int i = 0;
    	int j = nums.length-1;

    	while(i < j) {
    		int distance = target - nums[i] - nums[j];
    		if(distance == 0) {
    			groups.add(Arrays.asList(nums[i], nums[j]));
    			i++;
    			j--;
    			continue;
    		}
    		if(distance < 0) j--;
    		else i++;
    	}
    	return new LinkedList<List<Integer>>(groups);
    }
}