class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [n+1] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        step = [1, 2]

        for i in range(3, n+1):
            for s in step:
                if (i - s) >= 0:
                    dp[i] = (dp[i-1] + dp[i-2])
        return dp[n]

        print(dp)