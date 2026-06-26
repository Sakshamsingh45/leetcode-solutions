class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        finalsum=0
        for i in nums:
            if i<=5:
                continue
            count=2
            sum=i+1
            left,right=2,i-1
            while left<right:
                if i%left==0:
                    count+=1
                    sum+=left
                if i%right==0:
                    count+=1
                    sum+=right
                right-=1
                left+=1
                if count>4:
                    sum=0
                    break
            if count<4:
                sum=0
                continue
            finalsum+=sum
        return finalsum

