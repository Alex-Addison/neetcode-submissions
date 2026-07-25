class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for num1 in nums1:
            greaterFound = False
            for i, num2 in enumerate(nums2):
                if num2 == num1:
                    greaterFound = True
                if greaterFound and num2 > num1:
                    res.append(num2)
                    break
                if i == len(nums2)-1:
                    res.append(-1)
                    break
        return res