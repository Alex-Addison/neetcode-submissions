class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lefts = 0
        wildcards = 0
        for char in s:
            if char == '(':
                lefts+=1
            elif char == '*':
                wildcards += 1
            else:
                if lefts > 0:
                    lefts-=1
                elif wildcards > 0:
                    wildcards-=1
                else:
                    return False
        wildcards = 0
        rights = 0
        for char in s[::-1]:
            if char == ')':
                rights+=1
            elif char == '*':
                wildcards += 1
            else:
                if rights > 0:
                    rights-=1
                elif wildcards > 0:
                    wildcards-=1
                else:
                    return False
        return True