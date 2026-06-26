class Solution:
    def minPartitions(self, n: str) -> int:
        no=float("-inf")
        for i in n:
            a=int(i)
            if a>no:
                no=a
        return no