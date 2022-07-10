from typing import List

class Solution:
    
    def recurPermute(self, ds: list, freq: List[bool], n, arr, result):
        
        # base case
        if len(ds) == n:
            result.append(ds.copy())
            return
        
        for i in range(0, n):
            if not freq[i]:
                ds.append(arr[i])
                freq[i] = 1
                self.recurPermute(ds, freq, n, arr, result)
                ds.remove(arr[i])
                freq[i] = 0
            
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        freq = [0 for i in range(len(nums))]
        self.recurPermute([], freq, len(nums), nums, result)
        return result

print(Solution().permute([1,2,3]))

'''
TC: n! * n  [permutations * looping]
SC: O(n) + O(n) [ds + freq]
aux SC: O(n) [depth]
'''