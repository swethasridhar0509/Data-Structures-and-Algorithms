def countTriplet(arr):
    """
    Count the number of triplets (arr[j], arr[k], arr[i]) such that arr[j] + arr[k] = arr[i].

    Steps:
    1. Sort the input array to facilitate two-pointer technique.
    2. Iterate through each element (arr[i]) as the potential largest element of the triplet.
    3. Use two pointers (j and k) to find pairs (arr[j], arr[k]) such that their sum equals arr[i].
    4. If a valid pair is found, increment the count and adjust both pointers.
    5. If the sum of arr[j] and arr[k] is greater than arr[i], move the right pointer (k) to the left.
    6. If the sum is less than arr[i], move the left pointer (j) to the right.

    Time Complexity: O(n^2)
        - The outer loop runs in O(n), and the inner two-pointer search runs in O(n).
    Space Complexity: O(1)
        - Uses constant space for variables, aside from the input storage.
    """
    n = len(arr)
    arr.sort()  # Step 1: Sort the array
    count = 0
    
    # Step 2: Iterate through each element as the largest in the triplet
    for i in range(n):
        j = 0  # Left pointer
        k = i - 1  # Right pointer, starting before i
        
        # Step 3: Use two pointers to find pairs that sum to arr[i]
        while j < k:
            if arr[i] == arr[j] + arr[k]:  # Step 4: Valid pair found
                count += 1
                j += 1  # Move left pointer right
                k -= 1  # Move right pointer left
            elif arr[j] + arr[k] > arr[i]:  # Step 5: Decrease sum
                k -= 1
            else:  # Step 6: Increase sum
                j += 1

    return count
