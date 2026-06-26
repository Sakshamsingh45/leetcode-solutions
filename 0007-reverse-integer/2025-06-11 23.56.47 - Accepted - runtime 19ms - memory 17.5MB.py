class Solution:
    def reverse(self, x: int) -> int:
        neg=0
        if x <0:
            x=-x
            neg=1
        a=str(x)
        x="".join(reversed(a))
        if int(x)>(2**31)-1:
            return 0
        if neg==1:
            return -int(x)
        return int(x)

        


        