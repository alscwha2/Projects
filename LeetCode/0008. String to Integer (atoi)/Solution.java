class Solution {
	public static void main(String[] args) {
		System.out.println((new Solution()).myAtoi(args[0]));
	}
    public int myAtoi(String s) {
    	//delete whitespace
        s = s.trim();
        if(s.equals("")) return 0;

        //deal with first digit
        int sign = 1;
       	char first = s.charAt(0);
       	if (first == '-' || first == '+') {
       		if(first == '-')sign = -1;
       		s = s.substring(1);
       	} else if (!Character.isDigit(first)) return 0;

       	//loop through
       	long returnlong = 0;
        for(int i = 0; i < s.length(); i++) {
        	if(Character.isDigit(s.charAt(i))) {
        		returnlong *= 10;
        		returnlong += Character.getNumericValue(s.charAt(i));

        		//bounds check. doing it here to prevent LONG overflow
        		if (returnlong > Integer.MAX_VALUE) {
        			if (sign == -1) return Integer.MIN_VALUE;
        			if (sign == 1) return Integer.MAX_VALUE;
        		}
        	} else break;
        }
        return (int) returnlong * sign;
    }
}