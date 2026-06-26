# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur=head
        ans= []
        while cur:
            val=0
            temp=cur.next
            while temp:
                if temp.val>cur.val:
                    val=temp.val
                    break
                temp=temp.next
            ans.append(val)
            cur=cur.next
        return ans
