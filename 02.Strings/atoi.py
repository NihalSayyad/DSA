import sys


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):

        MAX = 2**31 - 1
        # MIN = sys.minsize
        num = 0
        before = True
        sign = 1

        for i in range(len(A)):
            if A[i] == ' ' and before:
                continue
            elif A[i] == ' ' and not before:
                break
            elif A[i] == '-' or A[i] == '+':
                if A[i] == '-':
                    sign = -1
            elif ord(A[i]) < ord('0') or ord(A[i]) > ord('9'):
                break
            else:
                before = False
                num = num * 10 + (ord(A[i]) - ord('0'))
                print(MAX)
                if num > MAX:
                    if sign == -1:
                        return -MAX -1
                    else:
                        return MAX
        return num * sign

sol = Solution()
A = "5121478262 8070067M75 X199R 547 8C0A11 93I630 4P4071 029W433619 M3 5 14703818 776366059B9O43393"
print(sol.atoi(A))