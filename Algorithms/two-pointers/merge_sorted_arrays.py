from typing import List

def merge(nums1, m, nums2, n):
    """
    Merges two sorted arrays nums1 and nums2 into nums1 as a single sorted array.
    
    Steps:
    1. Initialize three pointers:
       - i for the last valid element in nums1 (m - 1).
       - j for the last element in nums2 (n - 1).
       - k for the last position in nums1 (m + n - 1).
    2. While both arrays have elements to process:
       - Compare the elements at pointers i and j.
       - Place the larger element at position k and move the respective pointer.
    3. If any elements remain in nums2, copy them over to nums1.
       (No need to copy from nums1, as they are already in place.)
    """
    
    # Step 1: Initialize pointers
    i = m - 1  # Pointer for last valid element in nums1
    j = n - 1  # Pointer for last element in nums2
    k = m + n - 1  # Pointer for the last position in nums1

    # Step 2: Merge the arrays from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Step 3: If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    # No need to handle remaining elements in nums1 because they are already in place

# Time Complexity (TC): O(m + n)
# The algorithm processes each element in nums1 and nums2 exactly once.

# Space Complexity (SC): O(1)
# The merging is done in place, so no additional space is used apart from variables for pointers.
