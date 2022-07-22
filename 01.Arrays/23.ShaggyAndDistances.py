class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        seen = {}
        min_dist = len(A) + 1

        # for i in range(1, len(A)):
        #    A[i] = A[i-1] + A[i]

        for i in range(len(A)):
            if A[i] in seen:
                dist = i - A[i] + 1

                min_dist = min(dist, min_dist)

                seen[A[i]] = i
            else:
                seen[A[i]] = i

        if min_dist == len(A) + 1:
            return -1

        return min_dist

A = [ 7, 1, 3, 4, 1, 7 ]
sol = Solution()

print(sol.solve(A))