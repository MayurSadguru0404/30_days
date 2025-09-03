class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)

def sort_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        
        sort_stack(stack)
        sorted_insert(stack, temp)

def sorted_insert(stack, element):
    if stack.is_empty() or element >= stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.push(temp)

if __name__ == "__main__":
    s1 = Stack()
    s1.push(3)
    s1.push(1)
    s1.push(4)
    s1.push(2)
    print("Original stack:", s1)
    sort_stack(s1)
    print("Sorted stack:", s1)

    s2 = Stack()
    s2.push(5)
    s2.push(7)
    s2.push(9)
    print("\nOriginal stack:", s2)
    sort_stack(s2)
    print("Sorted stack:", s2)

    s3 = Stack()
    s3.push(10)
    s3.push(-5)
    s3.push(20)
    s3.push(-5)
    s3.push(15)
    print("\nOriginal stack:", s3)
    sort_stack(s3)
    print("Sorted stack:", s3)
