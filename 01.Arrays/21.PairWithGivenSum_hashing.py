class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        i = 0
        j = len(A) - 1
        map = {}
        count = 0

        for i in range(len(A)):
            if B - A[i] in map:
                count += map[B - A[i]]

            if A[i] not in map:
                map[A[i]] = 0
            map[A[i]] += 1

        return count % (10 ** 9 + 7)

sol = Solution()
A = []