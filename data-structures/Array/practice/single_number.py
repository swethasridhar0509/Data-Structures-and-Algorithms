
def singleNumberUsingMap(nums):

    map = {}

    # Count occurrences of each number
    for num in nums:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1

    # Find the number that occurs only once
    for k, v in map.items():
        if v == 1:
            return k
'''
Time Complexity: O(n) because you iterate through the array once to populate the hash map.
Space Complexity: O(n) due to the extra space used by the hash map.

'''

def singleNumberUsingXOR(nums):

    XOR = 0

    # XOR all elements; pairs will cancel each other out
    for num in nums:
        XOR ^= num

    return XOR

'''
Using XOR: More efficient in terms of space complexity (O(n) time, O(1) space)

'''

