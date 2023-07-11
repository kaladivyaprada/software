#Queue Operations using list
#using list
q=[]
def Enqueue(item):
    q.append(item)
def Dequeue():
    if not q:
        print("THE QUEUE IS EMPTY")
    else:
        print("THE DELETED QUEUE IS :",q.pop(0))
def Display():
    if not q:
        print("THE QUEUE IS EMPTY")
    else:
        print("THE CONTENTS of QUEUE IS:")
        for i in range(len(q)):
            print(q[i])
        print()
#driver code
while True:
    print("-------QUEUE OPERATIONS------")
    print("    1-->Enqueue")
    print("    2-->Dequeue")
    print("    3-->Display")
    print("    4-->Exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        item=int(input("enter the element:"))
        Enqueue(item)
    elif ch==2:
        Dequeue()
    elif ch==3:
        Display()
    elif ch==4:
        break
        
        












        





        
        
        
