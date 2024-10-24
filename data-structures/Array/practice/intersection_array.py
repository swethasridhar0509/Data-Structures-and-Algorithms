def findArrayIntersectionBrute(arr: list, brr: list):
    # Create an empty dictionary to store the frequency of elements from the first array
    map = {}
    
    # Create an empty list to store the common elements (intersection)
    inter = []

    # Traverse through the first array and count the frequency of each element
    for num in arr:
        if num not in map:
            map[num] = 1  # Add element to the dictionary with count 1 if it doesn't exist
        else:
            map[num] += 1  # Increment the count if the element is already in the dictionary

    # Traverse the second array and check if the element exists in the dictionary
    for num in brr:
        if num in map:
            if map[num] != 0:
                inter.append(num)  # If the element exists and has a count > 0, add to intersection
                map[num] -= 1  # Decrement the count in the dictionary to handle duplicates

    return inter

'''
Time Complexity:

O(n + m) where n is the length of arr and m is the length of brr.
We iterate through both arrays once, and dictionary operations (insertion and lookup) are O(1) on average.

Space Complexity:

O(n) for the dictionary, where n is the size of arr, because we store each element from arr in the dictionary.

'''


def findArrayIntersectionOptimal(arr: list, brr: list):
    # Create an empty list to store the intersection of both arrays
    inter = []
    
    # Initialize two pointers for both arrays
    i = j = 0
    
    # Traverse both arrays simultaneously until one of the arrays is fully processed
    while i < len(arr) and j < len(brr):
        # If both elements are the same, add to intersection and increment both pointers
        if arr[i] == brr[j]:
            inter.append(arr[i])
            i += 1
            j += 1
        # If arr[i] is smaller, increment i to find a match
        elif arr[i] < brr[j]:
            i += 1
        # If brr[j] is smaller, increment j to find a match
        else:
            j += 1

    return inter

'''
Time Complexity:

O(n + m), where n is the length of arr and m is the length of brr.
Each array is traversed only once with two pointers.

Space Complexity:

O(min(n, m)) for the intersection list, where n is the size of arr and m is the size of brr. We only store the common elements.
'''
