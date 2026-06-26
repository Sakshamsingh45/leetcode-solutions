class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_n="0"
        if int(num)< 100:
            return ""
        else:
            for i in range (len(num)-2):
                if num[i]==num[i+1] and num[i+1]==num[i+2]:
                    a=num[i]+num[i+1]+num[i+2]
                    if a>=max_n:
                        max_n=num[i]+num[i+1]+num[i+2]

        return max_n if max_n != "0" else ""
        