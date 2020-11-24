import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        String[] combinations = getCombinations(Arrays.asList(words));
        return null;
    }

    private String[] getCombinations(List<String> words) {
    	if (words.size() == 1) return words.toArray(new String[1]);
    	LinkedList<String> combinations = new LinkedList<>();

    	for(String word : words) {
    		List<String> copy = new LinkedList<>(words);
    		copy.remove(word);

    		for(String rest : getCombinations(copy)) {
    			combinations.add(word + rest);
    		}
    	}

    	return combinations.toArray(new String[combinations.size()]);
    }

    class TrieNode {
    	TrieNode
    }


    public static void main(String[] args) {
    	List<String> list = Arrays.asList(new String[] {"foo", "bar"});
    	Solution sol = new Solution();
    	for (String s : sol.getCombinations(list)) System.out.println(s);
    }
}