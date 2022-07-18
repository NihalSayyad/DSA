class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        left = 0
        right = len(A) - 1

        while left < right - 1:
            mid = (left + right) // 2

            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return A[mid]

            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return A[left] if A[left] >= A[right] else A[right]


sol = Solution()
A = [1, 100000, 100000]

print(sol.solve(A))