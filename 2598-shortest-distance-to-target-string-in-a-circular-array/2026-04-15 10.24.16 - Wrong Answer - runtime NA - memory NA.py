class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        mind=n
        for i in range(startIndex,startIndex+n):
            j=i%n
            if words[j]==target:
                mind=min(mind,abs(startIndex-j),n-abs(startIndex-i))
        return -1 if mind==n else mind
            