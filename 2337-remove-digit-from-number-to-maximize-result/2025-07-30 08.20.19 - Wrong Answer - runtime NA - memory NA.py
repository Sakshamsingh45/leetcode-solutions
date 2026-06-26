class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num,count=0,0
        for i in number:
            if count<1 and i==digit:
                count+=1
                continue
            else:
                num=num*10+int(i)
        return str(num)
