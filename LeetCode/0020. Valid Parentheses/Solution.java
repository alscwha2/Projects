import java.util.Arrays;
import java.util.Map;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
    	Map<String, String> map = Map.of(
		")", "(",
		"}", "{",
		"]", "["
		);
        
        Stack<String> stack = new Stack();
        for(String token : Arrays.asList(s.split(""))) {
        	if (map.values().contains(token)) stack.push(token);
        	else if (stack.isEmpty()) return false;
        	else if (!map.get(token).equals(stack.pop())) return false;
        }

        return stack.isEmpty();
    }
}