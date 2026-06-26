class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        freq={}
        for i,j in enumerate(nums):
            if j in freq:
                freq[j].append(i)
            else:
                freq[j]=[i]

        for i in range(len(nums)):
            a=freq.get(nums[i])
            if len(a)==1:
                continue
            else:
                s=0
                for j in range(len(a)):
                    if i==a[j]:
                        continue
                    else:
                        s+=abs(i-a[j])
                arr[i]=s
        return arr