class Solution:

    def solve(self, A):
        temp_dict = {}
        temp_dict['1'] = 0
        temp_dict['0'] = 0
        counter = 0

        for i in A:
            temp_dict[i] += 1
            if temp_dict['1'] != 0 and temp_dict['0'] != 0 and temp_dict['1'] == temp_dict['0']:
                counter +=1
                temp_dict['1'] = 0
                temp_dict['0'] = 0

        return counter


s1 = Solution()
print(s1.solve("011100"))
print(s1.solve("00011011"))

