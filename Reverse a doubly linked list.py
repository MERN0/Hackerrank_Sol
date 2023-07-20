'''Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. 
That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Note: The head node might be NULL to indicate that the list is empty.'''


def reverse(llist):
    # Write your code here
    prev_node = None
    current_node = llist

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        current_node.prev = next_node
        
        prev_node = current_node
        current_node = next_node

    llist = prev_node
    return llist
