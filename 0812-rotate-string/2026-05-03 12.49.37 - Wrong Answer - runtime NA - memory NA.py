class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s,goal=list(s),list(goal)
        c=goal.index(s[0])
        n=len(s)
        for i in range(n):
            if s[i]!=goal[c%n]:
                return False
            c+=1
        return True