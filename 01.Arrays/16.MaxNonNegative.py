class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        pref_sum = [0] * n
        if A[0] >= 0:
            pref_sum[0] = A[0]
        else:
            pref_sum[0] = -1

        max_sum = pref_sum[0]

        for i in range(1, n):
            if A[i] < 0:
                pref_sum[i] = -1
            else:
                if pref_sum[i-1] == -1:
                    pref_sum[i] = A[i]
                else:
                    pref_sum[i] = pref_sum[i - 1] + A[i]

            max_sum = max(max_sum, pref_sum[i])

        if max_sum == -1:
            return []

        size = 0

        idx_start = 0
        idx_end = 0
        start = 0
        end = 0
        for i in range(n):
            if pref_sum[i] == max_sum:
                end = i
                if size < (end - start + 1):
                    idx_start = start
                    idx_end = end
                    size = (end - start + 1)

            if pref_sum[i] == -1:
                start = i + 1

        return A[idx_start:idx_end + 1]

sol = Solution()
A = [1,2,3,4,-1,2,3,-1,1,2,3,4]
print(sol.maxset(A))