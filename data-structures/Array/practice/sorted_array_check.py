def isSorted(a) -> int:
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            return 0
    return 1

'''
TC - O(n)
SC - O(1)
'''