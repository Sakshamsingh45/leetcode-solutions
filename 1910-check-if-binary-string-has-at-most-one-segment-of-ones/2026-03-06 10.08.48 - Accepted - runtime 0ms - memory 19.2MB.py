class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag=False
        for i in s:
            if i=="0":
                flag=True
            if flag and i=="1":
                return False
        return True