'''
Problem: https://leetcode.com/problems/subsets/
Solution: https://www.youtube.com/watch?v=AxNNVECce8c&lc=Ugx3qi5BMzALS1jIHeN4AaABAg.9WZkqb5pgqy9W_7jLu4_aF
Approach: Either take the element or do not take & then recursively call the function by increasing the index & by appending or removing the element
'''

class Solution:
    def printSubsets(self, index, lst, nums, n, result):
        
        # Base case
        if index == n:
            result.append(lst.copy()) # copy needs to be used to avoid lst changing issues
            return

        # Take the element
        lst.append(nums[index])
        self.printSubsets(index+1, lst, nums, n, result)

        # Do not take the element
        lst.remove(nums[index])
        self.printSubsets(index+1, lst, nums, n, result)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        self.printSubsets(0, [], nums, len(nums), result)
        return result
    

'''
TC: O(2^n * n) [Two choices for every index]
SC: O(n) [Depth of recursion tree]
'''