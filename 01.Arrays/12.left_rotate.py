class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        out = [[] for i in range(len(B))]
        for i in range(len(B)):
            leftRotated = [num for num in A]

            B[i] = B[i] % n

            for j in range(i):
                temp = leftRotated[0]
                for k in range(1, len(leftRotated)):
                    leftRotated[k - 1] = leftRotated[k]
                leftRotated[n - 1] = temp

            for element in leftRotated:
                out[i].append(element)
            # print(out)

        return out

sol = Solution()
A = [1,2,3,4,5]
B = [2,3]
sol.solve(A,B)