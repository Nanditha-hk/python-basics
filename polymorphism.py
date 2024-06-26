def push(stack, val):
    stack.insert(0, val)
    print(val, "inserted")
    
def pop(stack):
    if len(stack) == 0:
        print("Stack is empty, can't delete anything")
        return 
    
    print(stack[0], "deleted")
    stack.pop(0)
    
def printStack(stack):
    if len(stack) == 0:
        print("Stack is empty, nothing to print")
        return 
    print(stack)


stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
push(stack, 60)

# 60 --> 50 --> 40 --> 30 --> 20 --> 10 


printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)
