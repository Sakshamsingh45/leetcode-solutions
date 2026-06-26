class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=""
        a=len(digits)
        for i in range(a):
            b=b+str(digits[i])
        b=int(b)
        b=b+1
        b=str(b)
        a=len(b)
        digits=[]
        for i in range (a):
            digits.append(int(b[i]))
        return digits
        