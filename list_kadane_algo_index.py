def find_max_sum_sublist(lst): 
    '''
    Without indexes
    '''

    global_max = float('-inf')
    local_max = 0

    for num in lst:
        local_max = max(num, local_max + num)
        global_max = max(local_max, global_max)

    # return global_max
    
    '''
    With index & actual elements
    '''
    l_result = []
    g_result = []
    global_max = float('-inf')
    local_max = 0
    l_start_idx = 0
    l_end_idx = 0
    g_start_idx = 0
    g_end_idx = 0

    for i in range(len(lst)):
        if lst[i] > (local_max + lst[i]):
            local_max = lst[i]
            l_result = [lst[i]]
            l_start_idx = i
        else:
            local_max += lst[i]
            l_result.append(lst[i])
            l_end_idx = i

        if global_max < local_max:
            global_max = local_max
            g_start_idx = l_start_idx
            g_end_idx = l_end_idx
            g_result = l_result[:] # Use slicing to avoid the same list reference issue

    print(f'start: {g_start_idx}, end: {g_end_idx}')
    print(g_result)
    print(global_max)
    return global_max

find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1])