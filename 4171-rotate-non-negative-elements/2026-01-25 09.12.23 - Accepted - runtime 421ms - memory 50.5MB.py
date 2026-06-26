class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        dict={}
        pos=[]
        posset=set()
        newnum=[]
        for i,j in enumerate(nums):
            if j>=0:
                pos.append(i)
                posset.add(i)
                dict[i]=j
            elif j<0:
                dict[i]=j

        if len(pos)==0:
            return nums
                
        temp=k%len(pos)
        for i in range(len(nums)):
            if i in posset:
                if temp==len(pos):
                    temp=0
                newnum.append(dict[pos[temp]])
                temp+=1
            else:
                newnum.append(dict[i])
        return newnum
                
                
            
            