class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        gIdx = 0
        cookies = 0

        for size in s:
            if gIdx<len(g) and g[gIdx] <= size:
                gIdx+=1
                cookies+=1

        return cookies