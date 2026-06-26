# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        val=set()
        temp=headA
        while temp!=None:
            val.add(id(temp))
            temp=temp.next
        temp=headB
        while temp!=None:
            if id(temp) in val:
                return temp
            temp=temp.next
        return None
        
        