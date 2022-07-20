class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        i = 0
        j = len(A) - 1
        k = 0

        while k < len(A) and k < j:
            if A[k] == 0:
                A[k], A[i] = A[i], A[k]
                k += 1
                i += 1

            elif A[k] == 1:
                k += 1

            else:
                A[k], A[j] = A[j], A[k]
                j -= 1

        return A

A = [2, 0, 0, 1, 0, 0, 2, 2, 1]

sol = Solution()
print(sol.sortColors(A))