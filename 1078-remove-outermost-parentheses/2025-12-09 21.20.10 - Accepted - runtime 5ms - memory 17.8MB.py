class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        a=""
        k=0
        j=0
        if len(s)<1:
            return ""
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            elif s[i]==")":
                stack.pop()
            if not stack:
                j=i
                a=a+s[k+1:j]
                k=j+1
        return a