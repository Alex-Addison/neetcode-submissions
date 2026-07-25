class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s[::-1] == s:
            return True
        
        for i in range(len(s)):
            removed = s[0:i]+s[i+1:len(s)]
            #print(removed)
            if removed[::-1] == removed: 
                return True
        return False