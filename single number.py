class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result
        
