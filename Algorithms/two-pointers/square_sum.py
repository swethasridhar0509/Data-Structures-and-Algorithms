def judgeSquareSum(c):
    """
    Determine if there exist non-negative integers i and j such that i^2 + j^2 = c.

    Steps:
    1. Initialize two pointers, i starting from 0 and j from the square root of c.
    2. Calculate the sum of squares of i and j (`curr = i^2 + j^2`).
    3. If `curr` equals c, return True (indicating such a pair exists).
    4. If `curr` is greater than c, decrease j (to try to reduce `curr`).
    5. If `curr` is less than c, increase i (to try to increase `curr`).
    6. Repeat until pointers meet or a solution is found. If no solution, return False.

    Time Complexity: O(√c)
        - The loop runs from 0 up to √c in the worst case, making it O(√c).
    Space Complexity: O(1)
        - Only a constant amount of extra space is used.
    """
    
    i = 0
    j = int(c ** 0.5)  # Step 1: Initialize pointers

    # Step 2: Use two-pointer technique to check combinations
    while i <= j:
        curr = (i * i) + (j * j)  # Calculate the sum of squares
        if curr == c:  # Step 3: Check if the sum equals c
            return True
        elif curr > c:  # Step 4: If sum is too large, decrease j
            j -= 1
        else:  # Step 5: If sum is too small, increase i
            i += 1

    return False  # Return False if no valid pair found
