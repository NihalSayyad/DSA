class Solution:
    def longestPalindrome(self,A):
        n = len(A)
        max_len = 0
        max_substr= ""
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            if max_len < 1:
                max_substr = A[i]
                max_len = 1
            if i+1 <= n-1:
                if A[i] == A[i+1]:
                    dp[i][i+1] = 1
                    if max_len < 2:
                        max_len =2
                        max_substr = A[i:i+2]

        for length in range(3,n+1):
            for i in range(n):
                if i+length > n:
                    break
                end = i + length-1
                if A[i] == A[end] and dp[i + 1][end - 1] == 1:
                    dp[i][end] = 1
                    if length > max_len:
                        max_len = length
                        max_substr = A[i:end + 1]

        print(dp)
        return max_substr

sol = Solution()
print(sol.longestPalindrome('abb'))
