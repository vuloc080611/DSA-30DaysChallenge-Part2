from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        # Thêm các khoảng kết thúc trước newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Gộp các khoảng chồng lấn
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        # Thêm các khoảng còn lại
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
