class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count=0
        freqb={}
        freqa={}
        for j in nums:
            freqa[j]=freqa.get(j,0)+1
        for i in nums:
            freqa[i]=freqa.get(i,0)-1
            if freqa.get(i*2,0)>0 and freqb.get(i*2,0)>0:
                count+=freqa.get(i*2)*freqb.get(i*2)
            freqb[i]=freqb.get(i,0)+1
        return count

        