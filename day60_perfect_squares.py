import math

class Solution:
    def numSquares(self, n: int) -> int:
        # DP cổ điển
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))  # 3
