class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in words:
            count=0
            for j in i:
                count+=weights[ord(j)-97]
            ans+=chr(122-count%26)
        return ans
         