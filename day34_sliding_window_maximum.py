from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = []
        for i, num in enumerate(nums):
            # Loại bỏ phần tử ngoài cửa sổ
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            # Loại bỏ các phần tử nhỏ hơn num từ cuối deque
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            # Ghi nhận max khi đủ k phần tử
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
