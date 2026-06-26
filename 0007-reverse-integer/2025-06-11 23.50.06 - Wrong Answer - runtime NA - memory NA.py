class Solution:
    def reverse(self, x: int) -> int:
        neg=0
        if x <0:
            x=-x
            neg=1
        a=str(x)
        x="".join(reversed(a))
        if neg==1:
            return -int(x)

        return int(x)

        


        