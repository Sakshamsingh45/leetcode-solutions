class Solution:
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        ans=gcd(nums[0],nums[-1])
        return ans
