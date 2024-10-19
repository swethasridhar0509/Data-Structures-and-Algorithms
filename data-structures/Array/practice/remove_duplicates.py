# brute solution

def removeDuplicates(nums):
    """
    Removes duplicates from the array and returns the number of unique elements.
    The first part of nums will contain the unique elements in sorted order.
    """
    # Step 1: Store unique elements in a set
    temp = set()
    for num in nums:
        temp.add(num)  # Add each element to the set, automatically removing duplicates
    
    # Step 2: Convert set to a sorted list to maintain sorted order
    temp = sorted(temp)  # Sort the set to ensure the result is in increasing order
    
    # Step 3: Overwrite the original array with the unique elements
    j = 0
    for x in temp:
        nums[j] = x  # Place each unique element back in the original array
        j += 1
    
    return len(temp)

'''
Complexity Analysis:
Time Complexity:

O(n) - to iterate through the array and add elements to the set.
O(n log n) - to sort the set (temp), where n is the number of unique elements in the array.
O(n) - to copy the unique elements back to nums.
Overall time complexity: O(n log n) due to sorting.

Space Complexity:

O(n) for storing the unique elements in the set temp.
Overall space complexity: O(n).
'''

# Optimal approach
