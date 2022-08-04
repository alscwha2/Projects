class Solution {
	public static void main(String[] args) {
		System.out.println((new Solution()).isPalindrome(Integer.parseInt(args[0])));
	}
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int power = (int) Math.floor(Math.log10(x));
        int place = 0;
        while(power > place) {
        	int big = (int) Math.floor(x / Math.pow(10, power) % 10);
        	int small = (int) Math.floor(x / Math.pow(10, place) % 10);
        	System.out.println(big);
        	System.out.println(small);
            if (big != small) return false;
            power--;
            place++;
        }
        
        return true;
    }
}