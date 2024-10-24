class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class SinglyLinkedList:

    def __init__(self, node):
        self.head = node 
        self.tail = self.head 
    
    # array to Linked List
    def arrToList(self, arr):
        self.head = Node(arr[0])
        curr = self.head 

        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            curr.next = newNode
            self.tail = newNode
            curr = curr.next 
        return self.head 
    
    # LL to array
    def listToArr(self):
        arr = []
        curr = self.head 
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next 
        return arr
    
    def getHeadValue(self):
        if self.head:
            return self.head.data
        else:
            return -1

    def linkedListTraverse(self):
        if self.head is None:
            print('List is Empty')
            return 
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next 
        print(None)            

    
    def insertAtBeg(self,data):
        
        # Step 1: Create a new Node
        newNode = Node(data)
        # Step 2: Set next of new_node to the current head
        newNode.next = self.head
        # Step 3: Set new_node as the head
        self.head = newNode
    
    def insertAtLast(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = node

    def insertAtMiddle(self, position, data):
        node = Node(data)
        if not self.head:
            return
        curr = self.head
        for _ in range(position - 1):
            curr = curr.next 
        node.next = curr.next
        curr.next = node 




if __name__ == "__main__":
    
    # Node1 = Node(10)
    linkedlist = SinglyLinkedList(None)
    # print('current head value:', linkedlist.getHeadValue())
    # linkedlist.insertAtBeg(20)
    print('current head value:', linkedlist.getHeadValue())
    linkedlist.insertAtLast(30)
    linkedlist.insertAtLast(40)
    linkedlist.insertAtLast(50)
    linkedlist.insertAtMiddle(2, 100)
    linkedlist.insertAtMiddle(3, 200)
    linkedlist.insertAtMiddle(4, 60)
    linkedlist.linkedListTraverse()
    print('current head value:', linkedlist.getHeadValue())
            