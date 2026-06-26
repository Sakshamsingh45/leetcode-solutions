class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        count=0
        while i<len(arr):
            if arr[i]%2 !=0:
                count+=1
            else:
                count=0
            i+=1
            if count==3:
                return True
        return False
