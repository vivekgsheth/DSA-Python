'''
Problem: https://leetcode.com/problems/subsets-ii/submissions/
Soln: https://www.youtube.com/watch?v=RIn3gOkbhQE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=11

Approach:
- Sorting the original arr 
- Looping: idx -> n-1
- At a particular level, take only first occurence in the ds
- Each level will give all subsets of len(level)
- Increment idx by 1 at each recursive call. Here, idx will be the idx of the value which we added in ds
'''

class Solution:
    
    def subset2(self, idx, ds, n, arr, result):
        
        result.append(ds.copy())
        
        for i in range(idx, n):    
            # avoid duplicates
            if i > idx and arr[i] == arr[i-1]:
                continue
            
            ds.append(arr[i])
            self.subset2(i+1, ds, n, arr, result)
            ds.remove(arr[i])
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        # sorting will be needed in order to avoid dups later in recursion
        nums.sort()
        
        self.subset2(0, [], len(nums), nums, result)
        return result

'''
k: Average length of the data structure

TC: 2^n * n
SC: 2^n * k
aux SC: n
'''