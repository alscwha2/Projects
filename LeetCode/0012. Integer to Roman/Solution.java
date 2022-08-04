class Solution {
    public String intToRoman(int num) {
        String romanString = "";
        for(int powerTen = 0; powerTen < 4; powerTen++) {
        	int digit = num % 10;
        	num = (int) Math.floor(num / 10);
        	romanString = digitToRoman(powerTen, digit) + romanString;
        }
        return romanString;
    }

    private String digitToRoman(int powerTen, int digit) {
    	String[] ones = {"I", "X", "C", "M"};
    	String[] fives = {"V", "L", "D"};

    	switch(digit) {
    		case 9:
    			return ones[powerTen] + ones[powerTen + 1];
    		case 4:
    			return ones[powerTen] + fives[powerTen];
    		default:
    			String romanDigit = Math.floor(digit / 5) == 1 ? fives[powerTen] : "";
    			while(digit-- % 5 != 0) romanDigit += ones[powerTen];
    			return romanDigit;
    	}
    }
}