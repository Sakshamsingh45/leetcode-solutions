# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur=head
        ans= []
        while cur!=None:
            count=0
            val=0
            temp=cur.next
            while temp!=None:
                if temp.val>cur.val:
                    val=temp.val
                    break
                else:
                    count+=1
                temp=temp.next
            for i in range(count+1):
                ans.append(val)
                cur=cur.next
            cur=cur.next
            ans.append(0)
        return ans