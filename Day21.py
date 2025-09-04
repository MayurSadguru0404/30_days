def insertAtBottom(stack, x):
    if not stack:   
        stack.append(x)
        return
    top = stack.pop()
    insertAtBottom(stack, x)
    stack.append(top)

def reverseStack(stack):
    if not stack:   
        return
    top = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top)
  
stack = [1, 2, 3, 4]
reverseStack(stack)
print("Reversed Stack:", stack)
