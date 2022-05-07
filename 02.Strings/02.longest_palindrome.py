class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)

        max_len = 0
        max_substr = ""
        for i in range(n):
            for j in range(i, n):
                string = A[i:j + 1]
                if string == string[::-1] and ((j - i + 1) > max_len):
                    max_substr = A[i:j+1]
                    max_len = (j - i + 1)

        return max_substr

sol = Solution()
A = 'abb'
print(sol.longestPalindrome(A))