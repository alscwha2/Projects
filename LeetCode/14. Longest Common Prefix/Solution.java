class Solution {
	public String longestCommonPrefix(String[] strs) {
		if(strs.length == 0) return "";

		String prefix = "";

		for(int index = 0; index < strs[0].length(); index++) {
			char character = strs[0].charAt(index);

			for(String str : strs) 
				if(str.length() <= index || str.charAt(index) != character) 
					return prefix;
			
			prefix += character;
		}

		return prefix;
	}
}