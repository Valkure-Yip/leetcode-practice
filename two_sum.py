class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(0,len(nums)-1):      #range(a,b)其实是[a,b)
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y]==target:
                    return [x,y]

# 注意Python后阈值是不包含的
# [a:b]
# range(a,b)            
