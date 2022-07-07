def find_second_maximum(lst):
    # Write your code here

    if not lst and len(lst) == 0:
        return None

    max_val = lst[0]
    max_val_ind = 0
    for i in range(0, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_val_ind = i

    second_max_val = float('-inf')
    for i in range(0, len(lst)):
        if i == max_val_ind:
            continue
        
        if lst[i] >= second_max_val:
            second_max_val = lst[i]
        
    return second_max_val