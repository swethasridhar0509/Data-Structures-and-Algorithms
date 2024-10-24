'''
union - common & unique elements
a = [1, 1, 2, 2, 3]
b = [1, 2, 3, 4]
a union b = [1, 2, 3, 4]
'''

def findUnionbySet(a, b):
    # Create an empty set to store unique elements
    union = set()
    
    # Add all elements from array 'a' to the set
    for i in range(0, len(a)):
        union.add(a[i])
    
    # Add all elements from array 'b' to the set
    for i in range(0, len(b)):
        union.add(b[i])
    
    # Convert the set to a sorted list
    union = sorted(union)
    
    return union

'''
Time complexity
1. Inserting into a set takes O(1) on average.
2. So, iterating through both arrays takes O(n + m), where n and m are the sizes of arrays a and b.
3. Sorting the set takes O((n + m) * log(n + m)).
 
Space complexity
The space complexity is O(n + m) due to the storage in the set.

 '''

def findUnionbyDict(a, b):
    # Create an empty dictionary to store unique elements
    union = {}
    
    # Add all elements from array 'a' to the dictionary
    for i in range(0, len(a)):
        if a[i] not in union:
            union[a[i]] = True
    
    # Add all elements from array 'b' to the dictionary
    for i in range(0, len(b)):
        if b[i] not in union:
            union[b[i]] = True
    
    # Convert the dictionary keys to a sorted list
    union = sorted(union.keys())
    
    return union
'''
Time Complexity:

Inserting into a dictionary takes O(1) on average.
So, iterating through both arrays takes O(n + m).
Sorting the dictionary keys takes O((n + m) * log(n + m)).

Space Complexity:

The space complexity is O(n + m) for storing elements in the dictionary.
'''

def findUnionOptimal(a, b):
    A = len(a)
    B = len(b)
    union = []
    
    i = j = 0
    
    # Traverse both arrays using two pointers
    while i < A and j < B:
        if a[i] <= b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1
    
    # Add remaining elements from array 'b'
    while j < B:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    
    # Add remaining elements from array 'a'
    while i < A:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    
    return union

'''
Time Complexity:

Since we are iterating through both arrays once, the time complexity is O(n + m).
No additional sorting is required.
Space Complexity:

The space complexity is O(n + m) due to the storage of the result in the union list.
'''