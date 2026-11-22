class Solution:
    def checkString(self, s: str) -> bool:
        flag=True
        for i in s:
            if i=="b":
                flag=False
            if i=="a" and not flag:
                return False
        return True