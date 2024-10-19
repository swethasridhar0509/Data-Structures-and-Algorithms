
def moveZeroes(nums):
    """
    Moves all zeros to the end of the array while maintaining the order of non-zero elements.
    """
    zero_ptr = -1  # Initialize pointer to store the index of the first zero

    # First loop: Find the first zero
    for idx in range(len(nums)):
        if nums[idx] == 0:
            zero_ptr = idx
            break
    
    # If there are no zeros in the array, return early
    if zero_ptr == -1:
        return

    # Second loop: Move non-zero elements to the front by swapping with zeros
    for i in range(zero_ptr + 1, len(nums)):
        if nums[i] != 0:
            # Swap non-zero element with the zero at zero_ptr
            nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
            zero_ptr += 1  # Move zero_ptr to the next zero

'''
Time Complexity:

The first loop to find the first zero runs in O(n), where n is the length of the array.
The second loop also runs in O(n), as we traverse the array to swap non-zero elements with zeros.
Overall time complexity is O(n), as both loops combined make a single pass over the array.

Space Complexity:

The solution is O(1) in terms of space since it only uses a few extra variables (zero_ptr, idx, and i), and it modifies the array in-place without requiring additional space.
'''