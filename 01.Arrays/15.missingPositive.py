class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        missing = 1
        for i in range(len(A)):
            if A[i] <= 0 or A[i] == i + 1 or A[i] > n:
                if A[i] == i+1:
                    missing += 1
                continue

            A[A[i] - 1],A[i] = A[i], A[A[i] - 1]

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return missing

sol = Solution()
A = [1 ]
print(sol.firstMissingPositive(A))