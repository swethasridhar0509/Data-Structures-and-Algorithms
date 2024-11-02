def bruteThreeSum(nums):
    """
    Brute force approach to find all unique triplets that sum to zero.

    Steps:
    1. Use three nested loops to generate all triplet combinations.
    2. For each triplet (nums[i], nums[j], nums[k]), check if their sum equals zero.
    3. If the sum is zero, sort the triplet and add it to the answer list if it's unique.

    Time Complexity: O(n^3 * log 3)
    Space Complexity: O(n^2) for storing unique triplets in the result list.
    """
    ans = []
    n = len(nums)
    
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = sorted([nums[i], nums[j], nums[k]])
                    if triplets not in ans:
                        ans.append(triplets)
    return ans

def optThreeSum(nums):
    """
    Optimized approach using a hash map to find unique triplets that sum to zero.

    Steps:
    1. Iterate through each number as the first element of the triplet.
    2. For each first element, define a target as -nums[i].
    3. Use a hash map to check if two numbers in the remaining array sum to the target.
    4. If a valid pair is found, add the sorted triplet to the result list if it is unique.

    Time Complexity: O(n^2 * log 3)
    Space Complexity: O(n^2) for storing unique triplets in the result list.
    """
    i = j = 0
    ans = []
    n = len(nums)
    for i in range(0, n):
        target = 0 - nums[i]
        map = {}
        for j in range(i + 1, n):
            diff = target - nums[j]
            if diff in map:
                triplet = sorted([nums[i], nums[j], diff])
                if triplet not in ans:
                    ans.append(triplet)
            else:
                map[nums[j]] = j
    return ans

def threeSum(nums):
    """
    Optimal approach using sorting and two pointers to find unique triplets that sum to zero.

    Steps:
    1. Sort the array to handle duplicates and enable two-pointer approach.
    2. Iterate through each element as the first element of the triplet.
    3. For each first element, use two pointers to find pairs in the remaining array
       that sum to the target (negative of the first element).
    4. Skip duplicate values while iterating to ensure only unique triplets are added.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2) for storing unique triplets in the result list.
    """

    ans = []
    n = len(nums)
    nums.sort()
    for i in range(0, n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        j = i + 1
        k = n - 1

        while j < k:
            if nums[j] + nums[k] == target:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                j += 1

        return ans