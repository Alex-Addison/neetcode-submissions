class TimeMap:

    def __init__(self):
        # store key : [(timestamp, val)]
        # timestamps will be in ascending order
        self.mem = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem.setdefault(key, [])
        self.mem[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem:
            return ''
        valueList = self.mem[key]
        print(valueList)
        left = 0
        right = len(valueList)-1
        mid = 0
        while left<=right:
            mid = (left+right)//2
            curTime = valueList[mid][0]
            if curTime == timestamp:
                return valueList[mid][1]
            elif curTime < timestamp:
                left = mid+1
            else:
                right = mid-1
        if valueList[mid][0] <= timestamp:
            return valueList[mid][1]
        elif mid>0:
            return valueList[mid-1][1]
        else:
            return ''
            
