# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        mx_arr=[]
        while cur is not None:
            mx_arr.append(cur.val)
            cur=cur.next
        mx=float("-inf")
        for i in range(-1,-len(mx_arr)-1,-1):
            mx=max(mx,mx_arr[i])
            mx_arr[i]=mx
        dummy=ListNode(None,head)
        prev=dummy
        cur=head
        count=0
        while count<len(mx_arr):
            if cur==None or cur.val==mx_arr[count]:
                cur=cur.next
                prev=prev.next
            else:
                prev.next=cur.next
                cur.next=None
                cur=prev.next
            count+=1
        return dummy.next
