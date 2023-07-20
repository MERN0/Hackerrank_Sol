'''Given the pointer to the head node of a linked list and an integer to insert at a certain position, 
create a new node with the given integer as its  attribute, 
insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.'''


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    node = SinglyLinkedListNode(data)
    
    if llist == None:
        llist = node
    
    else:
        temp = llist
        c = 1
        
        while c<position and temp is not None:
            temp = temp.next
            c += 1
            
        store = temp.next
        temp.next = node
        node.next = store
        
    return llist
