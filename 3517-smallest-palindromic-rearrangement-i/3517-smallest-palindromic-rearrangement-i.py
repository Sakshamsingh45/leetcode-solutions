class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq={}
        ans=""
        flag=False
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in range(97,123,1):
            if chr(i) in freq:
                if freq[chr(i)]%2==0:
                    ans+=chr(i)*(freq[chr(i)]//2)
                else:
                    char=chr(i)
                    fr=freq[char]//2
                    ans+=char*fr
                    flag=True
        if flag:
            return ans+char+ans[::-1]
        return ans+ans[::-1]
        