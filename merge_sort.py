from errno import EIDRM


def merge_sort(lst):

    if len(lst) <= 1:
        return
    
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    left_ind = 0
    right_ind = 0
    main_ind = 0

    while left_ind < len(left) and right_ind < len(right):

        if left[left_ind] < right[right_ind]:
            lst[main_ind] = left[left_ind]
            left_ind += 1
        
        else:
            lst[main_ind] = right[right_ind]
            right_ind += 1

        main_ind += 1

    # For all the remaining values

    while left_ind < len(left):
        lst[main_ind] = left[left_ind]
        left_ind += 1
        main_ind += 1

    while right_ind < len(right):
        lst[main_ind] = right[right_ind]
        right_ind += 1
        main_ind += 1

    print(lst)
    return lst

print(merge_sort([9,2,3,6,-1,0,100,9000]))
