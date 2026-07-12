class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        arr_sort=sorted(arr)
        prev=arr_sort[0]
        freq={}
        count=0
        for i,j in enumerate(arr_sort):
            if j not in freq:
                freq[j]=count+1
                count+=1
        for i in range(len(arr)):
            arr[i]=freq[arr[i]]
        return arr
                 
