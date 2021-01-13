size=int(input("enter size"))
stk=[]
top=0
def push(element):
    global top
    if(top>=size):
        print("stack is full")
    else:
        stk.append(element)
        top=top+1
def pop():
    global top
    if(top<=0):
        print("empty stack")
    else:
        top=top-1
        print(stk[top],"is popped")
        # for i in range(0, top):
        #     print(stk[i])
        #display()

def display():
    for i in range(0,top):
        print(stk[i])


n=1
while(n!=0):
    option=int(input("enter operation 1) push 2) Pop 3) display"))
    if(option==1):
        element=int(input("insert value"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    n=int(input("do u want to continue press 0 for exit 1 for continue"))
