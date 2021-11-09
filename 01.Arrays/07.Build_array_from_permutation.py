'''
LC - 1920. Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/
'''
class Solution:
    def buildArray(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])

        return res

if __name__ == '__main__':
    nums = [0,2,1,5,3,4]
    obj1 = Solution()
    print(obj1.buildArray(nums))