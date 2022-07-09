'''
Soln: https://www.youtube.com/watch?v=eQCS_v3bw0Q&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=7

Approach: Take & Not take approach along with handling sum as a variable in recursive calls
'''

# Printing all subsequences
def all_subseq(idx, ds, s, k, arr, n, result):

    if idx == n: 
        if s == k:
            result.append(ds.copy())
        return
    
    # Include
    ds.append(arr[idx])
    s += arr[idx]
    all_subseq(idx+1, ds, s, k, arr, n, result)

    ds.remove(arr[idx])
    s -= arr[idx]

    # Exclude
    all_subseq(idx+1, ds, s, k, arr, n, result)


# Printing only 1 subsequence

def one_subseq(idx, ds, s, k, arr, n, result) -> bool:

    if idx >= n: 

        # Condition satisfied
        if s == k:
            result.append(ds.copy())
            return True

        # Condition not satisfied
        return False
    
    # Include
    ds.append(arr[idx])
    s += arr[idx]

    if one_subseq(idx+1, ds, s, k, arr, n, result) == True:
        return True

    ds.remove(arr[idx])
    s -= arr[idx]

    # Exclude
    if one_subseq(idx+1, ds, s, k, arr, n, result) == True:
        return True

    return False

def count_subseq(idx, s, k, arr, n) -> int:

    if idx == n: 

        # Condition satisfied
        if s == k:
            return 1

        # Condition NOT satisfied
        return 0
    
    # Include
    s += arr[idx]

    include = count_subseq(idx+1, s, k, arr, n)

    s -= arr[idx]

    # Exclude
    exclude = count_subseq(idx+1, s, k, arr, n)

    return include + exclude

arr = [1,2,1]
k = 2

result = []
all_subseq(0, [], 0, k, arr, len(arr), result)
print(result)

result = []
one_subseq(0, [], 0, k, arr, len(arr), result)
print(result)

print(count_subseq(0, 0, k, arr, len(arr)))
