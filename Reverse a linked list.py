'''Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. 
The head pointer given may be null meaning that the initial list is empty.'''


def reverse(llist):
    # Write your code here
    prev = None
    curr = llist
    
    while curr != None:
        nxt = curr.next
        curr.next = prev
        
        prev = curr
        curr = nxt
        
    llist = prev
    return llist
