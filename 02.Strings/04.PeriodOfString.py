class Solution:
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

        LPS = self.LPSArr(A)
        period = 0
        if LPS[len(LPS)-1] == 0:
            period = len(LPS)
        else:
            period = len(LPS) - max(LPS)

        return period

sol = Solution()
A = "abcdabcdabce"
print(sol.solve(A))
