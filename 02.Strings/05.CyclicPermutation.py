class Solution:
    def LPSArr(self, A):
        n = len(A)
        LPS = [0 for i in range(n)]

        for i in range(1, n):
            x = LPS[i-1]
            while(A[x] != A[i]):
                if x == 0:
                    x -= 1
                    break
                x = LPS[x-1]
            LPS[i] = x + 1

        return LPS

    def solve(self, A, B):
        newStr = A + '$' + B + B
        LPS = self.LPSArr(newStr)
        len_A = len(A)
        count = 0

        for i in range(len_A, len(LPS)):
            if LPS[i] == len_A:
                count += 1

        return count

sol = Solution()
A = "111"
B = "111"

print(sol.solve(A, B))