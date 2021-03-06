class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        i = 0
        j = len(A)-1

        while i < j:
            if A[i] + A[j] <= B:
                if A[i] + A[j] == B:
                    left = 1
                    right = 1
                    multiplier = 1
                    if A[i] == A[j]:
                        multiplier = j-i

                    while i < len(A) and i < j-1 and A[i] == A[i+1]:
                        left += 1
                        i += 1
                    while j >= 0 and j > i+1 and A[j] == A[j-1]:
                        right += 1
                        j -= 1

                    count = count + (left * right) * multiplier
                    i += 1
                    j -= 1
                else:
                    i += 1
            else:
                j -= 1

        return count