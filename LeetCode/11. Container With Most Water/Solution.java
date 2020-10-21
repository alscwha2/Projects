class Solution {
    public int maxArea(int[] height) {
        int r = height.length - 1;
        int l = 0;
        int best = 0;
        int current = 0;

        while (r > l) {
        	if (height[r] > height[l]) {
        		current = height[l] * (r - l);
        		l++;
        	} else {
        		current = height[r] * (r - l);
        		r--;
        	}
        	if (current > best) best = current;
        }

        return best;
    }
}