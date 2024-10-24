# Brute Force

def twoSum(self, nums, target):
    # Loop through each pair of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check if they sum up to the target
            if nums[i] + nums[j] == target:
                return [i, j]

'''
Time Complexity: O(n²) (nested loops)  
Space Complexity: O(1)
'''


# Optimized Using Hash Map

def twoSum(nums, target):
    # Create a hash map to store seen numbers
    map = {}
    
    # Loop through the numbers
    for i in range(len(nums)):
        diff = target - nums[i]
        # Check if complement (target - nums[i]) exists
        if diff in map:
            return [i, map[diff]]
        # Otherwise, store the number with its index
        map[nums[i]] = i

'''
Time Complexity: O(n) (single pass)  
Space Complexity: O(n) (hash map)
'''
