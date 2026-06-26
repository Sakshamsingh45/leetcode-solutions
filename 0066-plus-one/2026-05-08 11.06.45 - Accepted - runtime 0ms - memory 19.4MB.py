class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(-1,-len(digits)-1,-1):
            s=digits[i]+carry
            carry=0 if s<10 else 1
            d=s%10
            digits[i]=d
        if carry:
            digits.insert(0,carry)
        return digits