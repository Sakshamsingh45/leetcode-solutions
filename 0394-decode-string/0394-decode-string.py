class Solution:
    def decodeString(self, s: str) -> str:
        def num(idx):
            nm=""
            while s[idx]!="[":
                    nm+=s[idx]
                    idx+=1
            return nm
        def alph(idx):
            word=""
            while idx<len(s) and s[idx]!="]" and s[idx]!="[" and not("1"<=s[idx]<="9"):
                word+=s[idx]
                idx+=1
            return word
            
        ans=""
        i=0
        while i<len(s):
            if "1"<=s[i]<="9":
                stack=["["]
                nums=[]
                alpha=[""]
                nums.append(num(i))
                i+=len(nums[-1])+1
                word=""
                while stack and i<len(s):
                    if s[i]=="]":
                        word=int(nums[-1])*alpha[-1]
                        stack.pop()
                        nums.pop()
                        alpha.pop()
                        i+=1
                        if stack:
                             alpha[-1]+=word
                        else:
                            ans+=word
                    elif s[i]=="[":
                        stack.append(s[i])
                        alpha.append("")
                        i+=1
                    elif "1"<=s[i]<="9":
                        nums.append(num(i))
                        i+=len(nums[-1])
                        continue
                    else:
                        wd=alph(i)
                        i+=len(wd)
                        alpha[-1]+=wd
                
            else:
                ans+=s[i]
                i+=1
        return ans
