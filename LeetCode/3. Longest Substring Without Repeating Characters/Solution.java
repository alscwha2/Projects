import java.util.Map;
import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longestLength = 0;

        Map<Character, Integer> seen = new HashMap<>();

        int beginningIndex = 0;
        for(int i = 0; i < s.length(); i++) {
        	char c = s.charAt(i);
        	if (seen.containsKey(c) && seen.get(c) >= beginningIndex)
        		beginningIndex = seen.get(c) + 1;
        	else {
        		int currentLength = i - beginningIndex + 1;
        		if (currentLength > longestLength)
        			longestLength = currentLength;
        	}
        	seen.put(c, i);
        }

        return longestLength;
    }
}