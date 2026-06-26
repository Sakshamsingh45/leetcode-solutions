class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        minl=letters[0]
        for i in letters:
            if i<target or i==target:
                continue
            else:
                minl=i
                break
        return minl

