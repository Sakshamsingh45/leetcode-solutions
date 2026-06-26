class Solution:
    def minOperations(self, s: str) -> int:
        count=0
        prev=s[0]
        for i in range(1,len(s)):
            cur=s[i]
            if prev==cur:
                count+=1
                if cur=="1":
                    prev="0"
                else:
                    prev="1"
                continue
            prev=cur
        return count