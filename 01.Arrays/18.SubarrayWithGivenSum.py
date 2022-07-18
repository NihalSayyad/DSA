class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        j = 0
        sum = A[0]
        while i <= len(A)-1 and j <= len(A) - 1:

            if sum <= B:
                if sum == B:
                    return A[i:j + 1]

                j += 1
                if j < len(A):
                    sum += A[j]
            else:
                sum -= A[i]
                i += 1

        return -1

sol = Solution()
A = [15, 2,5,6,9]
B = 7
print(sol.solve(A, B))