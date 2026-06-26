class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=[0]*(len(arr)+1)

        for i in arr:
            d[i]+=1
        max1=-1
        for j in range(1,len(d)):
            if d[j]==j:
                max1=d[j]

        return max1

        