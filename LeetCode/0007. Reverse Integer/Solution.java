class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverse(Integer.parseInt(args[0])));
    }
    public int reverse(int x) {
        boolean negative = x < 0;
        x = Math.abs(x);
        String str = "";
        char[] array = ("" + x).toCharArray();
        boolean leading = true;
        for (int i = array.length - 1; i >= 0; i--) {
            if (leading && array[i] == '0') continue;
            leading = false;
            str += array[i];
        }
        if(leading) str = "0";
        long l = Long.parseLong(str);
        l = negative ? l * -1 : l;
        if (l > Math.pow(2, 31) - 1 || l < Math.pow(2, 31) * -1) return 0;
        return (int) l;
    }

    /* another solution
    public int reverse(int x) {
        if(x == Integer.MIN_VALUE) return 0;
        
        int sign = x < 0 ? -1 : 1;
        x *= sign;
        long reversed = (new Long((new StringBuilder("" + x)).reverse().toString())).longValue() * sign;
        if(reversed < Integer.MIN_VALUE || reversed > Integer.MAX_VALUE) return 0;
        return (int) reversed;
    }
    */
}