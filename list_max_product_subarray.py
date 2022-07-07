'''
Problem: https://leetcode.com/problems/maximum-product-subarray/
Reference: NeetCode
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = max(nums)
        currMax, currMin = 1, 1
        
        for num in nums:
            if num == 0:
                currMax, currMin = 1, 1
                continue
            
            tempMax = currMax
            currMax = max(num, currMax*num, currMin*num)
            currMin = min(num, tempMax*num, currMin*num)
            
            globalMax = max(globalMax, currMax, currMin)
        
        return globalMax

    '''
    TC: O(N)
    SC: O(1)
    '''
