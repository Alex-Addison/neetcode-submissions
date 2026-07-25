class Solution:
    def trap(self, height: List[int]) -> int:

        aqua = 0
        def collect():
            water = 0
            leftIdx = rightIdx = 0
            while rightIdx < len(height)-1:
                rightIdx += 1
                rH = height[rightIdx]
                lH = height[leftIdx]
                if rH >= lH:
                    brim = min(lH, rH)
                    for lower in range(leftIdx+1,rightIdx):
                        water += brim - height[lower]
                    leftIdx = rightIdx
            return (water, leftIdx)
            
        aqua, l = collect()
        while l != len(height)-1:
            height = height[l:][::-1]
            a , l = collect()
            aqua+=a

        return aqua