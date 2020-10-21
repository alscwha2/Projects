class Solution {
	public int romanToInt(String s) {
		Map<String, Integer> numerals = Map.of(
			"I", new Integer(1),
			"V", new Integer(5),
			"X", new Integer(10),
			"L", new Integer(50),
			"C", new Integer(100),
			"D", new Integer(500),
			"M", new Integer(1000)
		);

		String first = null;
		String second = null;

		int value = 0;

		for(int i = 0; i < s.length(); i++) {
			if (first == null) {
				first = "" + s.charAt(i);
				continue;
			}

			second = "" + s.charAt(i);
			if (numerals.get(second) > numerals.get(first)) {
				value += numerals.get(second) - numerals.get(first);
				first = null;
			} else {
				value += numerals.get(first);
				first = second;
			}
			second = null;
		}

		return first == null ? value : value + numerals.get(first);
	}
}