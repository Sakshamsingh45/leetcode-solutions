class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev=alt=0
        for i in gain:
            prev=i+prev
            alt=prev if alt<prev else alt
        return alt