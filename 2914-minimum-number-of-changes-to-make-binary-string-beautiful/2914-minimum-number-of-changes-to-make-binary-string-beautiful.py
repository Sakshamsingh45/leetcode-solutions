class Solution:
    def minChanges(self, s: str) -> int:
        count_b1=count_b0=0
        count=0
        for i in s:
            if i=="0":
                if count_b1 and count_b1%2!=0:
                    count+=1
                    count_b1=0
                else:
                    count_b0+=1
            else:
                if count_b0 and count_b0%2!=0:
                    count+=1
                    count_b0=0
                else:
                    count_b1+=1
        if count_b0 and count_b0%2!=0:
                count+=1
        if count_b1 and count_b1%2!=0:
                    count+=1
        return count