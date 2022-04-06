class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        PS = [0 for i in range(n)]

        PS[0] = A[0]
        for i in range(1, n):
            PS[i] = PS[i - 1] + A[i]

        maxSum = (-10 ** 3) * n

        for i in range(n):
            if i + B >= n:
                total = PS[n - 1] - PS[i - 1] + PS[(i + B - 1) % n]
                maxSum = max(maxSum, total)

            else:
                if i == 0:
                    total = PS[i + B - 1]
                    maxSum = max(maxSum, total)
                else:
                    total = PS[i + B - 1] - PS[i - 1]
                    maxSum = max(maxSum, total)

        return maxSum

sol = Solution()
#A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
#B = 48

A = [61, -533, -666, -500, 169, 724, 478]
B = 4
#A = [5, -2, 3 , 1, 2]
#B = 3

#A=[1, 2]
#B = 1

print(sol.solve(A, B))