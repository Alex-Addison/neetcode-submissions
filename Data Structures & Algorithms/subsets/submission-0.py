class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        currSet = []
        subsets = []
        maxDepth = len(nums)

        #at each step we can add the current index or not
        #hold the depth as a variable and stop at len(nums)

        def dfs(depth=0):
            if depth == maxDepth:
                subsets.append(currSet[:])
            else:
                currSet.append(nums[depth])
                dfs(depth+1)
                currSet.pop(-1)
                dfs(depth+1)
        
        dfs()
        return subsets