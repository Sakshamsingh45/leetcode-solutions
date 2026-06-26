def convert(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    
    result += str(count) + s[-1]
    
    return result


class Solution:
    def countAndSay(self, n: int) -> str:
        temp = "1"
        for _ in range(n - 1):
            temp = convert(temp)
        return temp