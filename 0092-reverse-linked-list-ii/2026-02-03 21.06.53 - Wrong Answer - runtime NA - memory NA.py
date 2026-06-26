class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left >= right:
            return head

        dummy = ListNode(0, head)

        prev = dummy
        l = head
        for i in range(left-1):
            prev=prev.next
            l=l.next
        r=l
        for i in range(right-left):
            r=r.next
        rnext=r.next
        cur=l
        p=rnext
        while cur!=rnext:
            next=cur.next
            cur.next=p
            p=cur
            cur=next
        prev.next=p
        return head