class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 0
        len_A = len(A)
        len_B = len(B)

        if A[i] != B[j]:
            return 0

        for j in range(1, len_B):
            if B[j] != B[j-1]:
                i += 1
                if i >= len_A:
                    return 0

                if A[i] != B[j]:
                    return 0

        if j != len_B-1 or i != len_A-1:
            return 0
        return 1

sol = Solution()
A = "HIRE"
B = "HIR"

print(sol.solve(A, B))