class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 0
        A.sort()
        n = len(A)
        count = 0

        while i < n and j < n:
            if abs(A[i] - A[j]) <= B:
                if i != j and abs(A[i] - A[j]) == B:
                    count += 1
                    i += 1
                else:
                    j += 1
            else:
                i += 1

        return count

sol = Solution()
A = [ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ]
B = 3
print(sol.solve(A, B))