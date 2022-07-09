'''
Approach: Similar to combination sum 2 changing the base case & removing duplicate check
'''

class Solution:
    
    def combination(self, idx, n, ds, k, result):
        
        # base case
        if n == 0 and len(ds) == k:
            result.append(ds.copy())
            return
        
        for i in range(idx, 10):
            
            if i > n:
                break
            
            ds.append(i)
            self.combination(i+1, n-i, ds, k, result)
            ds.remove(i)
            
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        self.combination(1, n, [], k, result)
        return result
    
'''
TC: 2^9 * k
SC: k * x
'''
