'''Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. 
Either head pointer may be null meaning that the corresponding list is empty.'''


def mergeLists(head1, head2):
    temp = SinglyLinkedListNode(None)
    curr = temp
    
    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2= head2.next
        curr = curr.next
    
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
        
    return temp.next
