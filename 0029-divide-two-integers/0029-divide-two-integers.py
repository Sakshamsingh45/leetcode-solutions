class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=1
        if dividend < 0 and divisor<0:
            sign=1
        elif dividend <0 or divisor<0:
            sign=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        ques=(dividend//divisor)*sign
        if ques>(2**31)-1:
            return 2**31-1
        elif ques<-2**31:
            return 2**31
        return ques
        