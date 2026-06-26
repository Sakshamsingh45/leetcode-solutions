class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend <= -2**31 or dividend >= 2**31 - 1:
            if dividend <-2**31:
                return -2**31
            else:
                return 2**31-1
        if dividend<0 and divisor<0:
            return (dividend//divisor)
        if dividend <0 or divisor <0:
            return (dividend//divisor )+1
        return dividend//divisor
        