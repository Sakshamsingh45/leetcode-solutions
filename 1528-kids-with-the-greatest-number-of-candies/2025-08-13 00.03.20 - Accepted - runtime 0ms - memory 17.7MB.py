class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lis=[]
        max_can=max(candies)
        for i in candies:
            if i + extraCandies >= max_can:
                lis.append(True)
            else:
                lis.append(False)
        return lis