class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        count=0
        for i in arr1:
            low,high=0,len(arr2)
            while low<high:
                mid=(low+high)//2
                if arr2[mid]>=i:
                    high=mid
                else:
                    low=mid+1

            if low == len(arr2):
                if  i - arr2[low-1] > d:
                    count += 1

            elif low == 0 and arr2[low] - i > d:
                    count += 1

            elif arr2[low] - i > d and i - arr2[low-1] > d:
                count += 1
        return count