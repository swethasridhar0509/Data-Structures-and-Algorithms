def findMaxConsecutiveOnes(nums):
    max_ones = 0  # To store the maximum count of consecutive 1's
    count = 0     # To store the current count of consecutive 1's

    for num in nums:
        if num == 0:
            count = 0  # Reset the count when a 0 is encountered
        else:
            count += 1  # Increment the count when a 1 is encountered
            max_ones = max(count, max_ones)  # Update the maximum count of consecutive 1's
    return max_ones
