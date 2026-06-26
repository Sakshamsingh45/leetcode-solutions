class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=x
        self=0
        if(x<0 or x==0):
            return False
        else:
            while(x>0):
                a=x%10
                self=(10*self)+a
                x=x//10
            return b==self
