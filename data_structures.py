# --- Arrays ---
class MyArray:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def __str__(self):
        return str(self.data)

# --- Matrices ---
class MyMatrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def get_value(self, row, col):
        return self.matrix[row][col]

    def __str__(self):
        return '\n'.join(str(row) for row in self.matrix)
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)
class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        return self.queue[0] if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
if __name__ == "__main__":
    # Test MyArray
    print("Array:")
    arr = MyArray()
    arr.insert(10)
    arr.insert(20)
    arr.delete(10)
    print(arr)

    # Test MyMatrix
    print("\nMatrix:")
    mat = MyMatrix(2, 3)
    mat.set_value(0, 1, 5)
    print(mat)

    # Test Stack
    print("\nStack:")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack)
    stack.pop()
    print(stack)

    # Test Queue
    print("\nQueue:")
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    queue.dequeue()
    print(queue)

    # Test Linked List
    print("\nSingly Linked List:")
    sll = SinglyLinkedList()
    sll.insert_front(3)
    sll.insert_front(2)
    sll.insert_front(1)
    sll.traverse()
    sll.delete_value(2)
    sll.traverse()
