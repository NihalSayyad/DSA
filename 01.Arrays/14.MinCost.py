class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        minCost = inf

        for i in range(1, len(A)):
            left = []
            right = []
            for j in range(i - 1, -1, -1):
                if A[j] < A[i]:
                    left.append(j)
            for k in range(i + 1, len(A)):
                if A[k] > A[i]:
                    right.append(k)

            if len(right) > 0 and len(left) > 0:
                for l in left:
                    for r in right:
                        cost = B[l] + B[i] + B[r]
                        minCost = min(minCost, cost)

        return minCost

sol = Solution()
A = [ 1, 3, 5 ]
B = [ 1, 2, 3 ]

print(sol.solve(A, B))