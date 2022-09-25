'''
Problem: https://leetcode.com/problems/combination-sum-ii/submissions/
Soln: https://www.youtube.com/watch?v=G1fRTGRxXU8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=9

Approach:
- f(idx, target, ds)
- Loop from idx to n-1 
-   Optimization -> if arr[i] > target: break
-   Avoiding duplicates -> if i > idx and arr[i] == arr[i-1]: continue
-   For every i either we pick the element or not
-   ds.add(arr[i])
-   f(idx, target-arr[i], ds)
-   ds.remove(arr[i])

'''

class Solution:
    
    def combination(self, idx, target, ds, n, arr, result):
        
        # base case            
        if target == 0:
            result.append(ds.copy())
            return
        
        # looping from curr idx to end
        for i in range(idx, n):
            
            # avoid duplicates
            # `i > idx` -> It is kept to differentiate the first pick & its subsequent picks.
            # We need to pick the element first time. But we can avoid it subsequently if it is the same
            if i > idx and arr[i] == arr[i-1]:
                continue
            
            # end if target reached
            if arr[i] > target:
                break
            
            ds.append(arr[i])
            self.combination(i+1, target-arr[i], ds, n, arr, result)
            ds.remove(arr[i])
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # sorting array
        candidates.sort()
        result = []
        self.combination(0, target, [], len(candidates), candidates, result)
        return result
    
'''
k: Avg length of ds so to add the ds into result arr
x: Num of combinations

TC: 2^n * k
SC: k * x
'''
