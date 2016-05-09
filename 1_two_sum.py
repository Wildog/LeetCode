class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [i, d[diff]]
            d[nums[i]] = i
        return None

if __name__ == '__main__':
    print(Solution().twoSum([3,2,4], 6))
