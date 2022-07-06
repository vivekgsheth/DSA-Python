def max_min(lst):
    
    # Approach 1: Use two pointers & it will work for all types of nums
    # Cons: 
    # TC: O(n), SC: O(n)
    result = []
    start_idx = 0
    end_idx = len(lst)-1
    while start_idx < end_idx:
        result.append(lst[end_idx])
        end_idx -= 1

        result.append(lst[start_idx])
        start_idx += 1
        
        
    if start_idx == end_idx:
        result.append(lst[start_idx])

    # return result

    # Approach 2: Use modulus operator (Multiplication & Remainder elements)
    # Cons: Will not work for negative nums
    # TC: O(2n), SC: O(1)
    n = len(lst)
    min_idx = 0
    max_idx = n - 1
    max_ele = n + 1

    for i in range(n):
        # Even idx -> max_idx as we want there max elements
        if i%2 == 0:
            lst[i] = lst[i] + (lst[max_idx] % max_ele) * max_ele
            max_idx -= 1

        # Odd idx -> min_idx as we want min elements
        else:
            lst[i] = lst[i] + (lst[min_idx] % max_ele) * max_ele
            min_idx += 1

    print(lst)

    for i in range(n):
        lst[i] = lst[i] // max_ele

    return lst






