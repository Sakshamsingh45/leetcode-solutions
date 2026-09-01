# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lc_min=lcmax=0
        mn_dis=float("inf")
        mx_dis=float("-inf")
        prev=head
        first=last=0
        cur=head.next
        flag=True
        i=1
        while cur.next:
            if (prev.val<cur.val and cur.val>cur.next.val )or( prev.val>cur.val and cur.val<cur.next.val):
                if last:
                    mn_dis=min(mn_dis,i-last)
                if not first:
                    first=i
                mx_dis=max(mx_dis,i-first)
                flag=False
                last=i
            prev=cur
            cur=cur.next
            i+=1
            
        if flag or first==last:
            return [-1,-1]
        else:
            return [mn_dis,mx_dis]