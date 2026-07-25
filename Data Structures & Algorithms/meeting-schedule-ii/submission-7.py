"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x : x.start)
        days = 0
        while intervals:
            #start the day with the earlist start time
            lastEnd = intervals[0].end
            intervals.pop(0)
            currDay = []
            for interval in intervals:
                if interval.start>=lastEnd:
                    lastEnd=interval.end
                    currDay.append(interval)
            for interval in currDay:
                intervals.remove(interval)
            days += 1
        return days
