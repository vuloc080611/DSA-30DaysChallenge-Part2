from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Dùng bit mask: ones, twos
        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,3,2]))  # 3
