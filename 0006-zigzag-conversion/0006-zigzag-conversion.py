class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=""
        i=0
        for i in range(numRows):
            j=i
            if i==0 :
                while j<len(s):
                    res+=s[j]
                    j+=(numRows-1)+(numRows-2)+1
            elif i==numRows-1:
                gap=(numRows-2)*2+2
                while j<len(s):
                    res+=s[j]
                    j+=gap
            else:
                
                while j<len(s):
                    res+=s[j]
                    j += 2 * (numRows - 1 - i) if j == i or (j - i) % (2 * (numRows - 1)) == 0 else 2 * i
            i+=1
        return res