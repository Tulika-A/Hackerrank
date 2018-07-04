"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

buffer = []
def has_cycle(head):
    if(head.next == None):
        return False
    #elif head.next in buffer:
        #return True
    else:
        #buffer.append(head.data)
        #has_cycle(head.next)
        return True
