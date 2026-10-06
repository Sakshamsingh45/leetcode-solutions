class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        open_count=0
        close_count=0
        flag=False
        for i in s:
            if i=="(":
                open_count+=1
                flag=True
            elif i==")":
                if flag:
                    open_count-=1
                elif not flag:
                    close_count+=1
                if open_count==0:
                    flag=False
                
        return open_count+close_count