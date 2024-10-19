
def bruteMissingNumber(nums):
    # 1. Create an array arr with elements from 0 to n.
    arr = [i for i in range(0, len(nums)+1)]
    # 2. Iterate over this array and check if each number exists in nums.
    for num in arr:
        # 3. Return the first number that is missing from nums.
        if num not in nums:
            return num
'''
Time Complexity: O(n^2) because for each element in arr, checking if num not in nums takes O(n).
Space Complexity: O(n) due to the extra array arr of size n + 1.

'''

def betterMissingNumber(nums):
    # 1. Initialize a dictionary map with all keys from 0 to n and values 0.
    map = {}
    for i in range(0, len(nums) + 1):
        map[i] = 0
    # 2. Mark each number present in nums by setting its value to 1.
    for num in nums:
        map[num] = 1
    # 3. Iterate through the dictionary and return the first key whose value is still 0, which indicates the missing number.
    for k, v in map.items():
        if v == 0:
            return k

'''
Time Complexity: O(n) because the dictionary is created in O(n) and we perform constant time lookups.
Space Complexity: O(n) due to the extra space used by the dictionary.

'''

def optimalMissingNumber(nums):
    expected = 0
    actual = 0
    # 1. Calculate the sum of the numbers from 0 to n
    for i in range(0, len(nums)+1):
        expected += i
    # 2. Calculate the sum of the elements in nums.
    actual = sum(nums)
    # 3. Subtract the sum of nums from the expected sum to find the missing number.
    missing = expected - actual
    return missing

'''
Time Complexity: O(n) because summing the array takes linear time.
Space Complexity: O(1) since no additional space is used except a few variables.

'''

'''
1. a^a = 0
2. a^0 = a

'''
def optimal2MissingNumber(nums):
    XOR1 = XOR2 = 0
    # 1. XOR all the numbers from 0 to n.
    for i in range(0, len(nums) + 1):
        XOR1 ^= i
    # 2. XOR all the numbers in nums.
    for i in range(0, len(nums)):
        XOR2 ^= nums[i]
    # 3. The XOR of XOR1 and XOR2 will give the missing number because XOR cancels out the numbers that appear in both sets.
    return XOR1 ^ XOR2

'''
Time Complexity: O(n) because XORing all numbers takes linear time.
Space Complexity: O(1) since only a few variables are used.

'''
