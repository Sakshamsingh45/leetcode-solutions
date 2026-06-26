class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans=float("inf")
        for i in range(len(nums)-2):
            flag=False
            for j in range(i+1,len(nums)):
                if nums[j]!=nums[i]:
                    continue
                if flag:
                    break
                for k in range(j+1,len(nums)):
                    if nums[j]!=nums[k]:
                        continue
                    flag=True
                    temp=abs(i-j)+abs(j-k)+abs(i-k)
                    if temp<ans:
                        ans=temp
        return ans if ans!=float("inf") else -1

