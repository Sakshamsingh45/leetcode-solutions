class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        dict={}
        pos=[]
        temp=k
        for i,j in enumerate(nums):
            if j>=0:
                pos.append(i)
                dict[i]=j
            elif j<0:
                dict[i]=j

        for i in range(len(nums)):
            if nums[i]<0:
                pass
            else:
                if temp>=len(pos):
                       temp%=len(pos)
                nums[i]=dict[pos[temp]]
                temp+=1
        return nums