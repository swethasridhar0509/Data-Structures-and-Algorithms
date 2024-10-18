def brute_third_largest(arr):
    arr = list(set(arr))
    arr.sort()
    if arr < 3:
        return -1
    return arr[-3]

def better_third_largest(arr):
    
    maximum = s_max = t_max = float('-inf')
    for idx in range(0, len(arr)):
        if arr[idx] > maximum:
            maximum = arr[idx]
    for idx in range(0, len(arr)):
        if arr[idx] != maximum and arr[idx] > s_max:
            s_max = arr[idx]
    
    for idx in range(0, len(arr)):
        if arr[idx] != maximum and arr[idx] != s_max and arr[idx] > t_max:
            t_max = arr[idx]
    
    return -1 if t_max == float('-inf') else t_max

def optimal_third_largest(arr):
        
        if len(arr) < 3:
            return -1
        maximum = s_max = t_max =  float('-inf')
        
        for num in arr:
            if num > maximum:
                t_max = s_max
                s_max = maximum
                maximum = num
            elif num > s_max and num != maximum:
                t_max = s_max
                s_max = num
            elif num > t_max and num < s_max:
                t_max = num
        
        return -1 if t_max == float('-inf') else t_max 

'''
Brute Force: O(n log n) TC, O(1) SC.
Better Approach: O(n) TC, O(1) SC.
Optimal Approach: O(n) TC, O(1) SC (single-pass and most efficient).

'''