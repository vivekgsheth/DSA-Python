'''
Problem: https://leetcode.com/problems/combination-sum/submissions/ 
Soln: https://www.youtube.com/watch?v=OyZFFqQtu98&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=8

Approach: Take or Not take with target manipulation

Normal patterns:

------------------------------------ Print all subsequences ------------------------------------
Base case:
    if idx == n:
        if s == sum:
            print(ds)
# Inclusion
ds.add(arr[idx])
s += arr[idx]
f()
ds.remove(arr[idx])
s -=- arr[idx]

# Exclusion
f()

------------------------------------ Print any one subsequence ------------------------------------
Base case:
    return True -> condition satisfied
    return False -> condition NOT satisfied

if f() == True:
    return True

if f() == True:
    return True

return False


------------------------------------ Count subsequences ------------------------------------
Base case:
    return 1 ->  condition satisfied
    return 0 -> condition NOT satisfied

l = f()
r = f()

return (l + r)

# Here you can loop as well from i=0 to n-1

'''

class Solution:
    def combination(self, idx, target, ds, n, arr, result):
        
        # Base case
        if idx == n:
            
            if target == 0:
                result.append(ds.copy())
            
            return
    
        # Include the element if the condition is satisfied
        if arr[idx] <= target:
            
            ds.append(arr[idx])
            
            '''
            Here we are passing `idx` in the recursive call because the question stated we can pick a number `more than once`.
            If the question states that you can pick the number `only once` then you will need to pass `idx+1`
            '''
            self.combination(idx, target-arr[idx], ds, n, arr, result)
            
            ds.remove(arr[idx])
        
        # Exclude
        self.combination(idx+1, target, ds, n, arr, result)
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        self.combination(0, target, [], len(candidates), candidates, result)
        
        return result


'''
k: average length of the data structure 
x: no of combinations

TC: 2^target * k
SC: k * x
'''
