class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            if stack:
                top = stack[-1]
                while stack and top[1] < temperatures[i]:
                    stack.pop(-1)
                    result[top[0]] = i - top[0]
                    top = stack[-1] if stack else None
            stack.append((i,temperatures[i]))
        return result