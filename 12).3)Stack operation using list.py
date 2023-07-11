#STACK OPERATIONS USING LIST
#using list
stack=[]
def push():
    if len(stack)==n:
        print("the stack is full")
    else:
        element=(input("enter the element:"))
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("the stack is empty")
    else:
        print("the popped element is:",stack.pop())
def peek():
    if not stack:
        print("the  stack is empty")
    else:
        print("the Top of the stack is:",stack[-1])
def display():
    if not stack:
        print("the stack is empty")
    else:
        print("the content of stack are:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

#Driver code
n=int(input("entre the size of the stack:"))
while True:
    print("-------STACK OPERATIONS------")
    print("       1--->push")
    print("       2--->pop")
    print("       3--->peek")
    print("       4--->display")
    print("       5--->Exit")
    choice=int(input("entre your choice:"))
    if choice==1:
               push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        break
               
               














            







        
    
