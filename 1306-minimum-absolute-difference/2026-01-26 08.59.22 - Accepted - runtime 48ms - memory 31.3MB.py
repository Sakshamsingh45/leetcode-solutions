class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff=float("inf")
        md=[]
        for i in range(len(arr)-1):
            dif=arr[i+1]-arr[i]
            if dif<diff:
                md=[]
                diff=dif
            elif dif==diff:
                pass
            else:
                continue
            md.append([arr[i],arr[i+1]])
        return md
        






        