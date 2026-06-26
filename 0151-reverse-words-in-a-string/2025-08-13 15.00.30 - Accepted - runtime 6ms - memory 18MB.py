class Solution:
    def reverseWords(self, s: str) -> str:
        a = ''
        s = s.strip()
        end = len(s)
        count = 0
        j = len(s) - 1  # start from last char
        
        while j >= 0:
            if s[j] != " ":
                count += 1
            elif count > 0:
                # append the current word
                a += s[j+1:j+1+count] + " "
                end -= count
                count = 0
            # skip extra spaces
            j -= 1
        
        # add last word (first in original order)
        if count > 0:
            a += s[j+1:j+1+count]
        
        return a
