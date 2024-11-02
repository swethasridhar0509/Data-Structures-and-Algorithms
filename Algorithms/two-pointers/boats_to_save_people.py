def numRescueBoats(people, limit):
    # Step 1: Sort the array of people's weights
    people.sort()
    
    # Step 2: Initialize two pointers
    i = 0  # Pointer for the lightest person
    j = len(people) - 1  # Pointer for the heaviest person
    count = 0  # Count of boats needed

    # Step 3: Use a while loop to iterate until all people are assigned to boats
    while i <= j:
        curr = people[i] + people[j]  # Calculate the current combined weight
        
        # Step 4: Check if the lightest and heaviest can share a boat
        if curr <= limit:
            count += 1  # Increment boat count since they can share a boat
            i += 1  # Move the pointer for the lightest person up
            j -= 1  # Move the pointer for the heaviest person down
        else:
            count += 1  # Heaviest person goes alone in a boat
            j -= 1  # Move the pointer for the heaviest person down

    # Step 5: Return the total count of boats needed
    return count

'''
This solution employs a greedy algorithm, which operates on the principle of making the best local choice at each step with the hope of finding the global optimum. In this case, the algorithm aims to minimize the number of boats needed to transport all people by:

1. Sorting the weights of the people to facilitate efficient pairing.
2. Pairing the lightest and heaviest people: The algorithm attempts to place the heaviest remaining person on the same boat as the lightest person that can still fit within the weight limit. This greedy choice allows the algorithm to utilize the available capacity of the boats as fully as possible, thus minimizing the total number of boats required.
3. If the lightest person cannot be paired with the heaviest (due to weight constraints), the heavier person is assigned to a boat alone.

Complexity Analysis:

Time Complexity: 
    O(nlogn) due to the sorting step, where n is the number of people.
Space Complexity: 
    O(1) as we use a constant amount of extra space for pointers and counters.

'''
