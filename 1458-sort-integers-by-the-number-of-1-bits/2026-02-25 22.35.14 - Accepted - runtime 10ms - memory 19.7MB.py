class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        freq={}
        for i in arr:
            count=0
            for j in bin(i)[2:]:
                if j=="1":
                    count+=1
            freq[i]=count
        return sorted(arr,key=lambda x:(freq[x],x))