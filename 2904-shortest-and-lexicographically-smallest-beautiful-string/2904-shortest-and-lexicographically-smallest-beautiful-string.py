class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        arr=[]
        count=0
        for r in range(len(s)):
            if s[r]=="1":
                count+=1
            while count>k:
                if s[l]=="1":
                    count-=1
                l+=1
            if count==k:
                while s[l]=="0":
                    l+=1
                st=s[l:r+1]
                if arr:
                    if len(arr[-1])>len(st):
                        arr=[]
                        arr.append(st)
                    elif len(arr[-1]) == len(st):
                        if arr[-1]>st:
                            arr[-1]=st
                else:
                    arr.append(st)
        return arr[-1] if arr else ""