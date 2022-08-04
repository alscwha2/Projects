import java.util.LinkedList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

class Solution {
	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.letterCombinations(args[0]));
	}
	public List<String> letterCombinations(String digits) {

		Map<Character, List<Character>> ref = Map.of(
			'2', Arrays.asList(new Character[] {'a', 'b', 'c'}),
			'3', Arrays.asList(new Character[] {'d', 'e', 'f'}),
			'4', Arrays.asList(new Character[] {'g', 'h','i'}),
			'5', Arrays.asList(new Character[] {'j', 'k', 'l'}),
			'6', Arrays.asList(new Character[] {'m', 'n', 'o'}),
			'7', Arrays.asList(new Character[] {'p', 'q', 'r', 's'}),
			'8', Arrays.asList(new Character[] {'t', 'u', 'v'}),
			'9', Arrays.asList(new Character[] {'w', 'x', 'y', 'z'})
		);

		LinkedList<String> list = new LinkedList<>();

		if (digits.length() > 0)
			for (char c : ref.get(digits.charAt(0))) {
				if (digits.length() == 1) 
					list.add("" + c);
				else
					for (String s : letterCombinations(digits.substring(1)))
						list.add(c + s);
			}

		return list;
	}
}