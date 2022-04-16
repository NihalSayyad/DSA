#class Solution:
	# @param A : string
	# @param B : string
	# @return a strings

class Solution:
    def addBinary(self, A, B):
        A = A[::-1]
        B = B[::-1]
        lenA = len(A)
        lenB = len(B)
        c = 0
        n = max(lenA, lenB)
        pos = 0
        out = ""
        while pos < n or c != 0:
            if pos >= n:
                val = c % 2
                c = c//2
                out += str(val)
            else:
                if pos > lenA-1:
                    val = int(B[pos]) + c
                    c = val//2
                    val = val%2
                    out += str(val)
                elif pos > lenB-1:
                    val = int(A[pos]) + c
                    c = val//2
                    val = val % 2
                    out += str(val)
                else:
                    val = int(A[pos]) + int(B[pos]) + c
                    c = val//2
                    val = val %2
                    out += str(val)
            pos += 1

        return out[::-1]

sol = Solution()
A = "1"
B = "1"
print(sol.addBinary(A, B))