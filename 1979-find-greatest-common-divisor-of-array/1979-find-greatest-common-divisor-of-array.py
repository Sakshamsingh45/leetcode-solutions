class Solution:
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        mn,mx=min(nums),max(nums)
        ans=gcd(mn,mx)
        return ans

