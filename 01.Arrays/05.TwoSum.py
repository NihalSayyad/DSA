#LC - 1. Two Sum

class Solution:
    def twoSum(self, nums, target):
        mapDict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in mapDict:
                return [mapDict[val], i]
            else:
                mapDict[nums[i]] = i
        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    obj1 = Solution()
    print(obj1.twoSum(nums, target))