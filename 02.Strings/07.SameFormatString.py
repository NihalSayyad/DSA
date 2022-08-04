class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 0
        len_A = len(A)
        len_B = len(B)

        while i < len_A:
            while j < len_B and A[i] == B[j]:
                j += 1
            if j >= len_B:
                break
            i += 1

        if i != len_A or j != len_B:
            return 0

        return 1

sol = Solution()
A = "HIRE"
B = "HIRE"

print(sol.solve(A, B))