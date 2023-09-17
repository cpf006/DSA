# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        last_node = None
        while current_node:
            place_holder = current_node.next
            current_node.next = last_node
            last_node = current_node
            current_node = place_holder

        return last_node
'''
Not much notes here. Some mistakes I made at first were 
setting the while condition to if current_node.next was not None.

Also returning current_node instead of last_node
'''
