class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        count=0
        for i in range(len(capacity)):
            count+=capacity[i]
            if count>=s:
                return i+1
        return len(capacity)