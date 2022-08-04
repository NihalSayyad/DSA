class Solution:
    # @param A : string
    # @return a strings
    def LPSArr(self, A):
        n = len(A)
        LPS = [0 for i in range(n)]

        for i in range(1, n):
            x = LPS[i - 1]
            while (A[x] != A[i]):
                if x == 0:
                    x -= 1
                    break
                x = LPS[x - 1]
            LPS[i] = x + 1
        return LPS

    def solve(self, A):
        newStr = A + '$' + A[::-1]
        LPS = self.LPSArr(newStr)

        if LPS[len(LPS) - 1] >= len(A) - 1:
            return 'YES'

        return 'NO'

sol = Solution()
A = 'abba'
print(sol.solve((A)))