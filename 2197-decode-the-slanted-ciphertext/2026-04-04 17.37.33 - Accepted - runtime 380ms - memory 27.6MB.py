class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        col=len(encodedText)//rows
        ans=""
        for i in range(col):
            count=i
            for j in range(rows):
                if count<len(encodedText):
                    ans+=encodedText[count]
                count+=(col+1)
        return ans.rstrip()
