def brute_second_largest(arr):
    arr.sort()
    for i in range(len(arr)-2, -1, -1):
        if arr[i] != arr[-1]:
            return arr[i]
    return -1

def better_second_largest(arr):
    
    maximum = s_max = float('-inf')
    for idx in range(0, len(arr)):
        if arr[idx] > maximum:
            maximum = arr[idx]
    for idx in range(0, len(arr)):
        if arr[idx] != maximum and arr[idx] > s_max:
            s_max = arr[idx]
    
    return -1 if s_max == float('-inf') else s_max

def optimal_second_largest(arr):
        
        if len(arr) < 2:
            return -1
        maximum = s_max = float('-inf')
        
        for num in arr:
            if num > maximum:
                s_max = maximum
                maximum = num
            elif num > s_max and num != maximum:
                s_max = num
        
        return -1 if s_max == float('-inf') else s_max 

'''
Brute Force: O(n log n) TC, O(1) SC.
Better Approach: O(n) TC, O(1) SC.
Optimal Approach: O(n) TC, O(1) SC (single-pass and most efficient).

'''