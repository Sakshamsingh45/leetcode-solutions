class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=float("inf")
        for i in nums:
            b=0
            while i!=0:
                digit=i%10
                b+=digit
                i//=10
            m=b if m>b else m
        return m
