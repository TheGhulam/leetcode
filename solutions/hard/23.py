#Problem 23: Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Edge cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # Initialize the heap
        heap = []
        
        # Add the first node from each list to the heap
        # We need to add index to handle same values
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i, lst))
        
        # Create a dummy node for the result
        dummy = ListNode(0)
        current = dummy
        
        # Process nodes from heap until empty
        while heap:
            val, i, node = heappop(heap)
            
            # Add next node from the same list to heap
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            
            # Add current minimal node to result
            current.next = node
            current = current.next
        
        return dummy.next