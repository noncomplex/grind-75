# linear traverse
# check cases of non-overlap because if newInterval > all
# then we know to add that interval and if < we know to add
# newInterval + rest
# if overlap in someway get the min and max for start and end
# edge case for empty and no intervals > newInterval at the end

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans += intervals[i:]
                return ans
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        ans.append(newInterval)
        return ans
