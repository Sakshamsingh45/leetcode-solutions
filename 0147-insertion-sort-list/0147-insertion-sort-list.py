# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(None,head)
        cur=head.next
        prev=head
        while cur!=None:
            st=dummy
            flag=True
            while st.next!=cur:
                if st.next and st.next.val<=cur.val:
                    st=st.next
                else:
                    prev.next=cur.next
                    st.next,cur.next=cur,st.next
                    flag=False
                    break
            if flag:
                prev=cur
                cur=cur.next
            else:
                cur=prev.next
        return dummy.next
