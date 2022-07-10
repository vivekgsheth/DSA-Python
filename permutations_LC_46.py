from typing import List

class Solution:
    
    def recurPermuteOpt(self, idx, n, arr, result):
        
        # base case
        if idx == n:
            result.append(arr.copy())
            return
        
        for i in range(idx, n):
            arr[idx], arr[i] = arr[i], arr[idx]
            self.recurPermuteOpt(idx+1, n, arr, result)
            # revert back to the original arr after recursive call
            arr[idx], arr[i] = arr[i], arr[idx]

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

        result2 = []
        self.recurPermuteOpt(0, len(nums), nums, result2)
        return result2

print(Solution().permute([1,2,3]))

'''
recurPermute
TC: n! * n  [permutations * looping]
SC: O(n) + O(n) [ds + freq]
aux SC: O(n) [depth]
'''

'''
recurPermuteOpt
TC: (n!) * n [permutations * looping]
SC: O(1)
aux SC: O(n) [depth]
'''