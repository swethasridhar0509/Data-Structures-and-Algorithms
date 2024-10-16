'''

This Python code defines a custom `Array` class that simulates a fixed-size array. It includes methods for common array operations:

- Initialization: Sets a maximum capacity and creates an internal array with `None` values.
- Insert: Adds elements at a specified index, shifting existing elements if needed.
- Delete: Removes elements from a specified index, shifting elements to maintain order.
- Access (Get/Update): Retrieves or modifies elements at a given index with bounds checking.
- Linear Search: Searches for a value and returns its index or -1 if not found.
- Utility Methods: Includes checks for array fullness and emptiness, and provides a string representation for easy display.

This implementation demonstrates the basics of array operations and error handling, providing a foundational understanding of how arrays work.

'''

class Array:

    def __init__(self, capacity):
        self.capacity = capacity
        self.curr_size = 0
        self.array = [None] * capacity

    def traverse(self):
        if self.isEmpty():
            return 'Array is empty'
        
        for i in range(self.curr_size):
            print(self.array[i])

    def search(self, search_val):
        for i in range(0, self.curr_size):
            if self.array[i] == search_val:
                return i
        return -1
    
    def access(self, index):
        if not self.valid_index(index):
            raise IndexError("Index out of bounds.")
        return self.array[index]
    
    def insert(self, index, data):
        
        # 1. Check for space in array.
        if self.isFull():
            raise OverflowError("Array is Full.")
        
        # 2. Check for index validity.
        if not self.valid_index(index, 1):
            raise IndexError("Index out of bounds.")
        
        # 3. shift elements.
        for i in range(self.curr_size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        
        # 4. insert.
        self.array[index] = data

        # 5. Update size.
        self.curr_size += 1
        

    def delete(self, index):

        if not self.valid_index(index):
            raise IndexError("Index out of bounds.")
        
        # shift elements
        for i in range(index + 1, self.curr_size):
            self.array[i - 1] = self.array[i]
        
        # update size
        self.array[self.curr_size - 1] = None
        self.curr_size -= 1
    
    def __str__(self):
        return str(self.array[:self.curr_size])
    
    def isFull(self):
        return self.curr_size == self.capacity
    
    def isEmpty(self):
        return self.curr_size == 0
    
    def valid_index(self, index, action_id = 0):

        # For insert operation - (0 - size(insertion at last)) is valid.
        if action_id == 1:
            return index >= 0 and index <= self.curr_size
        else:
            return index >= 0 and index < self.curr_size
        

if __name__ == '__main__':
    array = Array(7)
    array.insert(0, 10)
    array.insert(1, 20)
    array.insert(2, 30)
    print("Array after inserts:", array)

    array.delete(1)
    print("Array after deletion:", array)

    index = array.search(30)
    print("Index of 30:", index)

    print("Element at index 0:", array.access(0))
    array.traverse()
