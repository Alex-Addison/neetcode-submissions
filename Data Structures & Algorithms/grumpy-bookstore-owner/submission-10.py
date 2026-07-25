class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        custCopy = customers[:]
        for minute, isGrump in enumerate(grumpy):
            if isGrump == 1:
                custCopy[minute] = 0
            else:
                customers[minute] = 0
        
        print(custCopy, customers)

        maxAdd = 0
        curr = customers[0:minutes]
        maxAdd = max(maxAdd, sum(curr))
        for i in range(minutes, len(customers)):
            print(curr)
            curr.pop(0)
            curr.append(customers[i])
            maxAdd = max(maxAdd, sum(curr))
        
        print(maxAdd, sum(custCopy))
        return sum(custCopy) + maxAdd
