class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #creates a set with nums
        longest = 0        #stores the longest streak

        #since sets are ordered, num-1 == nums[i-1]
        for num in numSet:
            if (num - 1) not in numSet: #only initiate loop if element hasnt been used before
                length = 1
                while (num + length) in numSet: #num + length is the next numbers
                    length += 1
                longest = max(length, longest)
        return longest