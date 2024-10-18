def leftRotateArray(arr):

    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp

    return arr 

def rightRotateArray(arr):

    temp = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        arr[i + 1] = arr[i]
    arr[0] = temp

    return arr

'''
Time complexity - O(N)
Space complexity - O(1)

'''



