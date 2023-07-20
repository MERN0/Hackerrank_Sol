''A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed 
from the front and new elements to be added to the rear. 
This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue 
(i.e., the one that has been waiting the longest) is always the first one to be removed.'''



# Enter your code here. Read input from STDIN. Print output to STDOUT

q = int(input())
stack_push = []
stack_dele = []

for i in range(q):
    t = list(input().split())
    
    #enqueue
    if t[0] == '1':
        stack_push.append(t[1])
        
    #dequeue
    if t[0] == '2':
        if not stack_dele:
            while stack_push:
                stack_dele.append(stack_push.pop())
        stack_dele.pop()
        
    #pop
    if t[0] == '3':
        if not stack_dele:
            while stack_push:
                stack_dele.append(stack_push.pop())
        print(stack_dele[-1])
                
