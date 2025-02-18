# 05_Time Complexity

## Time Complexity

- Time complexity ≠ Time taken to execute the algorithm.
- The growth trend of the algorithm’s runtime as the size of the input data increases.

## Calculating Time Complexity

1. Identify the Basic Operations that contribute to the running time. (loops, assignment).
2. Count how many times the operations are executed relative to the input.
3. Express the time as a function.
4. Simplify.

## Type of time complexity

### O(1) - constant time

- The algorithm or operation takes the **same amount of time regardless of the size of the input**.
- The number of steps does not depend on n, the input size.
- **Examples**

<aside>
- Accessing an array element by index
- Push/pop operations on a stack

</aside>

```python
def constant_time_a(items):
	print(items[0])

# size of items can be 1 or 1000.
# fuction would require one step.
```

```python
def constant_time_b(items):
	for _ in range(10000):
		print(0)
'''
Although it has a loop for 10000 times and a long runtime,
it is still independent of the input. 
Hence, constant time.
'''
```

## O(n) - linear time

- Linear order indicates the number of operations grows linearly with the input data size n.
- If the input doubles, the runtime roughly doubles.
- Each element in the input is typically processed **once**.
- **Examples**

<aside>
- Traversing an array or list
- Finding the maximum/minimum element in an unsorted array

</aside>

```python
def linear_time(items):
	for item in items:
		print(item)
# 10 items - print operation for 10 times
# 100 items - print operation for 100 times.
```

```python
def concatenate_lists(lst1, lst2):
    for item in lst1:  # Runs n times
        print(item)
    for item in lst2:  # Runs m times
        print(item)
# time complexity - O(n + m)
```

## O(n²) - quadratic time

- The runtime grows **proportionally to the square of the input size n.**
- Usually involves nested iterations over the input, and pairs.
- **Examples**

<aside>
- Bubble Sort
- Selection Sort
- Comparing each element with every other element in an array

</aside>

```python
def quadratic_time(items):
    for i in items:        # n times
        for j in items:    # n times for each i
            print(i, j)    
# For n items, operation occurs n * n = n² times
```

```python
def quadratic_time(list1, list2):
    for x in list1:             # Outer loop runs n times
        for y in list2:         # Inner loop runs m times
            print((x, y))       # Total: n * m operations
```