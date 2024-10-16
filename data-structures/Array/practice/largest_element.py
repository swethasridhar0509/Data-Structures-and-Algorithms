def brute_largest_element(arr):
    arr.sort()
    return arr[-1]

def opt_largest_element(arr):    
    maximum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]    
    return maximum

def test_largest_element_functions():
    test_cases = [
        ([3, 5, 2, 8, 7], 8),       # General case
        ([1], 1),                   # Single element
        ([-1, -4, -3, -2], -1),     # All negative numbers
        ([4, -2, 5, -1, 3], 5),     # Mixed positive and negative numbers
        ([2, 7, 7, 3, 5], 7),       # Duplicate maximum values
    ]

    for arr, expected in test_cases:
        assert brute_largest_element(arr) == expected, f"Failed on {arr} with brute_largest_element"
        assert opt_largest_element(arr) == expected, f"Failed on {arr} with opt_largest_element"
    
    print("All tests passed.")

test_largest_element_functions()

'''

1. brute_largest_element
- Time Complexity (TC): (O(n log n)) due to sorting the array.
- Space Complexity (SC): (O(1)) with in-place sorting.

2. opt_largest_element
- Time Complexity (TC): (O(n)) as it iterates through the array once.
- Space Complexity (SC): (O(1)) as it uses only a single variable (maximum), regardless of input size.

'''

