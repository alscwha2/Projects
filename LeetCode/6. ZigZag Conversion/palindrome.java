class palindrome {
	public static void main(String[] args) {
		palindrome palindrome = new palindrome();
		System.out.println(palindrome.longestPalindrome("aba"));
	}

    public String longestPalindrome(String s) {
        System.out.println(s);
        String longest = "";
        int length = 0;
        
        
        int pointer = 0;
        int counter = 0;
        int buffer = 1;
        boolean stillcounting = true;

        for(pointer = 0; pointer < s.length(); pointer++) {
        	System.out.println(pointer);
            //taking care of counting the middle of the palandrome
            if(stillcounting) {
                if(pointer + 1 < s.length()) {
                    if(s.charAt(pointer + 1) == s.charAt(pointer)) {
                        counter++;
                        continue;
                    } else {
                        stillcounting = false;
                    }
                } else {
                    int currentlength = 1 + counter;
                    return currentlength > length ? s.substring(pointer - counter, pointer + 1) : longest;
                }
            }
            System.out.println(pointer);
            
            // reading from both sides
            int beginningIndex = pointer - counter - buffer;
            int endingIndex = pointer + buffer;
            System.out.println("beginningIndex: " + beginningIndex + " endingIndex: " + endingIndex);
            if(beginningIndex >= 0 && endingIndex < s.length() && s.charAt(beginningIndex) == s.charAt(endingIndex)) {
                buffer++;
                pointer--;
            } else {
                System.out.println("pointer: " + pointer +" buffer: " + buffer + " counter: " + counter);
                int currentlength = 2 * (buffer - 1) + counter + 1;
                if(currentlength > length) {
                    length = currentlength;
                    longest = s.substring(beginningIndex + 1, endingIndex);
                }
                
                //reseting
                buffer = 1;
                stillcounting = true;
                counter = 0;
            }
        }
        
        return longest;
    }
}