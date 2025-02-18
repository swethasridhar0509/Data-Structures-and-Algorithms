# 06_Space Complexity

## **Space Complexity**

- Measures the ****growth trend of the memory space occupied by an algorithm as the amount of data increases.
- Input space + additional space + output space

## Types

![image.png](image.png)

### **Constant order O(1)**

- An algorithm has **constant space complexity** if the amount of memory required remains the same regardless of the input size.
- No additional memory usage grows with the input size.
- Fixed-size variables or pointers are used, regardless of the input size.
- In-place operations.
- Examples

<aside>
- Finding the maximum element in an array
- Swapping two numbers
- Checking if a number is prime
- Reversing an array In place.

</aside>

### **Linear order O(n)**

- Space required grows linearly with the input size n
- Additional memory usage is directly proportional to the input size
- Common when creating new data structures that scale with input
- **Examples**

<aside>
- Creating a new array to store elements
- Storing intermediate results in an array
- Building a hash table from input elements

</aside>

## Time and Space Tradeoff

The choice between these approaches depends on our priorities - faster performance (time) or lower memory usage (space).

**Example** - searching for a number in an array:

- **Time-Optimized Approach:** Create a hash table to store all elements for O(1) lookup time, but this requires O(n) extra space.
- **Space-Optimized Approach:** Use linear search which requires O(1) space but takes O(n) time to find an element.