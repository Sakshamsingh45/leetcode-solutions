class Solution:
    def gcd(num1,num2):
        while num2:
            num1,num2=num1,num1%num2
        return num1
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefixgcd=[]
        for i in nums:
            mx=max(i,mx)
            prefixgcd.append(gcd(i,mx))
        prefixgcd.sort()
        i,j=0,len(nums)-1
        sm=0
        while i<j:
            sm+=gcd(prefixgcd[i],prefixgcd[j])
            i+=1
            j-=1
        return sm