class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s,goal=list(s),list(goal)
        n=len(s)
        for i in range(n):
            if s==goal:
                return True
            temp=s[-1]
            s.pop()
            s.insert(0,temp)
        return False