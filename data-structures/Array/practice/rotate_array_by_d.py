def leftRotateArray(arr, k):
    """
    Left rotate the array by k positions.
    
    Steps:
    1. Normalize k: Ensure that k is within the range of the array length.
    2. Store the first k elements in a temporary array.
    3. Shift the remaining elements of the array to the left by k positions.
    4. Place the elements from the temporary array at the end of the original array.
    """
    
    N = len(arr)  # Step 1: Get the length of the array
    k = k % N     # Step 1: Normalize k to avoid unnecessary rotations
    
    # Step 2: Store the first k elements in a temporary array
    temp = arr[:k]

    # Step 3: Shift the remaining elements to the left by k positions
    for i in range(k, N):
        arr[i - k] = arr[i]
    
    # Step 4: Place the elements from the temp array at the end of the original array
    for i in range(0, len(temp)):
        arr[N - k + i] = temp[i]
    
    return arr  # Return the rotated array

def rightRotateArray(nums, k):
    """
    Right rotate the array by k positions.
    
    Steps:
    1. Normalize k: Ensure that k is within the range of the array length.
    2. Store the last k elements in a temporary array.
    3. Shift the remaining elements of the array to the right by k positions.
    4. Place the elements from the temporary array at the beginning of the original array.
    """
    
    k = k % len(nums)  # Step 1: Normalize k to avoid unnecessary rotations

    # Step 2: Store the last k elements in a temporary array
    temp = nums[-k:]
       
    # Step 3: Shift the remaining elements to the right by k positions
    for i in range(len(nums) - k - 1, -1, -1):
        nums[i + k] = nums[i]
    
    # Step 4: Place the elements from the temp array at the beginning of the original array
    for i in range(0, len(temp)):
        nums[i] = temp[i]

    return nums  # Return the rotated array
