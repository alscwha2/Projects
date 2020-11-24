class Solution {
    public String longestPalindrome(String s) {
        int biggestSeen = 0;
        int biggestIndex = 0;

        int i = 0;
        while (i < s.length()) {

        	//building the center
        	int centerLength = 1;
        	while (i + centerLength < s.length() && s.charAt(i) == s.charAt(i + centerLength)) 
        		centerLength++;

        	// checking the left and right neighbors
        	int surroundingLength = 0;
        	while(true) {
        		int leftBound = i - (surroundingLength + 1);
        		int rightBound = i + centerLength + surroundingLength;

        		if(leftBound < 0 || rightBound >= s.length()) 
        			break;

        		if(s.charAt(leftBound) == s.charAt(rightBound))
        			surroundingLength++;
        		else 
        			break;
        	}

        	// update biggest seen
        	int totalLength = centerLength + 2*surroundingLength;
        	if (totalLength > biggestSeen) {
        		biggestSeen = totalLength;
        		biggestIndex = i - surroundingLength;
        	}

        	i += centerLength;
        }

        return s.substring(biggestIndex, biggestIndex + biggestSeen);
    }
}