class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend<0 and divisor<0:
            return (dividend//divisor)
        if dividend < 0:
            dividend = dividend*-1
            return -(dividend//divisor)
        if divisor <0:
            divisor = divisor *-1
            return -( dividend//divisor)
        return dividend//divisor
        