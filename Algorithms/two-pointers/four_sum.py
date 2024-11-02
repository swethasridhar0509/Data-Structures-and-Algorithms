
def fourSum(nums, target):
    """
    Find all unique quadruplets in the list that sum up to the target.

    Steps:
    1. Sort the input array to facilitate duplicate handling and two-pointer technique.
    2. Use a nested loop to fix the first two elements of the quadruplet (nums[i] and nums[j]).
    3. Use two pointers (k and l) to find the remaining two elements that complete the quadruplet.
    4. If the sum of the four elements equals the target, add the quadruplet to the result list.
    5. Skip duplicates for both the second element and the pointers to ensure unique quadruplets.

    Time Complexity: O(n^3)
        - The outer loops run in O(n^2) and the two-pointer search runs in O(n).
    Space Complexity: O(n) for storing the output list of unique quadruplets.
    """
    n = len(nums)
    ans = []
    nums.sort()  # Step 1: Sort the array

    # Step 2: Fix the first element of the quadruplet
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the first element
            
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicates for the second element
            k = j + 1  # Initialize the third pointer
            l = n - 1  # Initialize the fourth pointer

            # Step 3: Use two pointers to find the other two elements
            while k < l:
                curr = nums[i] + nums[j] + nums[k] + nums[l]
                if curr == target:
                    # Step 4: Found a quadruplet that sums to target
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    l -= 1  # Move the right pointer left
                    k += 1  # Move the left pointer right
                    # Step 5: Skip duplicates for k and l
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                elif curr < target:
                    k += 1  # Move the left pointer right to increase sum
                else:
                    l -= 1  # Move the right pointer left to decrease sum

    return ans

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))  # Expected output: [[-2, -1, 0, 1], [-2, 0, 0, 2]]
