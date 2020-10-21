class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        
        string = str(x)
        returnstring = ""
        
        leading = 1
        for i in range(len(string)):
            num = string[(len(string) - 1) - i]
            if leading and num == 0:
                continue
            leading = 0
            returnstring += num
            
        if leading:
            return 0
        
        x = int(returnstring) * sign
        return x if x < (2 ** 31 - 1) and x > (-1 * 2 ** 31) else 0