class Solution:
    def maxProduct(self, n: int) -> int:
        num1=num2=float("-inf")
        while n:
            digit=n%10
            if digit>=num1:
                num2=num1
                num1=digit
            elif num1>digit>=num2:
                num2=digit
            n//=10
        return num1*num2