class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0','1','2','5','6','8','9'}
        diff = {'2','5','6','9'}
        
        count = 0
        
        for i in range(1, n+1):
            s = str(i)
            
            if any(ch not in valid for ch in s):
                continue
            
            if any(ch in diff for ch in s):
                count += 1
        
        return count